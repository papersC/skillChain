"""
SkillChain DX - AI Skill Inference Module
Uses sentence transformers for skill matching and role recommendations
"""

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
from typing import List, Dict, Tuple
import re


class SkillInferenceEngine:
    """AI-powered skill extraction and matching engine"""
    
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Initialize the skill inference engine
        
        Args:
            model_name: Sentence transformer model to use
        """
        print(f"Loading sentence transformer model: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.job_roles = None
        self.courses = None
        self.employees = None
        
    def load_data(self, job_roles_path: str, courses_path: str, employees_path: str):
        """Load datasets from CSV files"""
        print("Loading datasets...")
        self.job_roles = pd.read_csv(job_roles_path)
        self.courses = pd.read_csv(courses_path)
        self.employees = pd.read_csv(employees_path)
        print(f"Loaded {len(self.job_roles)} job roles, {len(self.courses)} courses, {len(self.employees)} employees")
        
    def extract_skills(self, text: str) -> List[str]:
        """
        Extract skills from text using simple pattern matching
        
        Args:
            text: Text containing skills
            
        Returns:
            List of extracted skills
        """
        # Simple extraction: split by common delimiters
        skills = re.split(r'[,;]', text.lower())
        skills = [s.strip() for s in skills if s.strip()]
        return skills
    
    def get_employee_skills(self, employee_id: str) -> str:
        """
        Get aggregated skills for an employee based on completed courses
        
        Args:
            employee_id: Employee identifier
            
        Returns:
            Concatenated skill description
        """
        employee = self.employees[self.employees['employee_id'] == employee_id].iloc[0]
        completed_course_ids = [c.strip() for c in employee['completed_courses'].split(',')]
        
        # Get skills from all completed courses
        employee_skills = []
        for course_id in completed_course_ids:
            course = self.courses[self.courses['course_id'] == course_id]
            if not course.empty:
                skills = course.iloc[0]['skills_taught']
                employee_skills.append(skills)
        
        return ', '.join(employee_skills)
    
    def compute_role_similarity(self, employee_id: str) -> pd.DataFrame:
        """
        Compute similarity between employee skills and all job roles
        
        Args:
            employee_id: Employee identifier
            
        Returns:
            DataFrame with role recommendations sorted by similarity
        """
        # Get employee skills
        employee_skills = self.get_employee_skills(employee_id)
        
        # Create embeddings
        employee_embedding = self.model.encode([employee_skills])
        role_embeddings = self.model.encode(self.job_roles['required_skills'].tolist())
        
        # Compute cosine similarity
        similarities = cosine_similarity(employee_embedding, role_embeddings)[0]
        
        # Create results dataframe
        results = self.job_roles.copy()
        results['similarity_score'] = similarities
        results['similarity_percentage'] = (similarities * 100).round(2)
        results = results.sort_values('similarity_score', ascending=False)
        
        return results[['role_id', 'role_title', 'required_skills', 'similarity_percentage']]
    
    def get_top_recommendations(self, employee_id: str, top_n: int = 3) -> pd.DataFrame:
        """
        Get top N role recommendations for an employee
        
        Args:
            employee_id: Employee identifier
            top_n: Number of recommendations to return
            
        Returns:
            DataFrame with top recommendations
        """
        all_recommendations = self.compute_role_similarity(employee_id)
        return all_recommendations.head(top_n)
    
    def identify_skill_gaps(self, employee_id: str, target_role_id: str) -> Dict:
        """
        Identify skill gaps between employee and target role
        
        Args:
            employee_id: Employee identifier
            target_role_id: Target role identifier
            
        Returns:
            Dictionary with skill gap analysis
        """
        # Get employee skills
        employee_skills_text = self.get_employee_skills(employee_id)
        employee_skills = set(self.extract_skills(employee_skills_text))
        
        # Get target role skills
        target_role = self.job_roles[self.job_roles['role_id'] == target_role_id].iloc[0]
        required_skills = set(self.extract_skills(target_role['required_skills']))
        
        # Compute gaps
        skill_gaps = required_skills - employee_skills
        matching_skills = employee_skills & required_skills
        
        # Get similarity score
        similarities = self.compute_role_similarity(employee_id)
        similarity_score = similarities[similarities['role_id'] == target_role_id]['similarity_percentage'].values[0]
        
        return {
            'employee_id': employee_id,
            'target_role': target_role['role_title'],
            'target_role_id': target_role_id,
            'similarity_score': similarity_score,
            'matching_skills': list(matching_skills),
            'skill_gaps': list(skill_gaps),
            'gap_count': len(skill_gaps)
        }
    
    def generate_recommendations_report(self, output_path: str = 'results/recommendations_report.json'):
        """Generate comprehensive recommendations report for all employees"""
        report = {}
        
        for _, employee in self.employees.iterrows():
            emp_id = employee['employee_id']
            emp_name = employee['name']
            current_role = employee['current_role']
            
            # Get top 3 recommendations
            top_recs = self.get_top_recommendations(emp_id, top_n=3)
            
            # Get skill gaps for top recommendation
            top_role_id = top_recs.iloc[0]['role_id']
            skill_gaps = self.identify_skill_gaps(emp_id, top_role_id)
            
            report[emp_id] = {
                'name': emp_name,
                'current_role': current_role,
                'top_recommendations': top_recs.to_dict('records'),
                'skill_gap_analysis': skill_gaps
            }
        
        # Save report (convert numpy types to Python types)
        def convert_to_python_types(obj):
            """Convert numpy types to Python native types"""
            if isinstance(obj, dict):
                return {k: convert_to_python_types(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_to_python_types(item) for item in obj]
            elif isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            else:
                return obj

        report_converted = convert_to_python_types(report)

        with open(output_path, 'w') as f:
            json.dump(report_converted, f, indent=2)
        
        print(f"Recommendations report saved to {output_path}")
        return report

