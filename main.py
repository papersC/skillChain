"""
SkillChain DX - Main Execution Script
Demonstrates all components for the Applied Sciences paper
"""

import sys
import time
import pandas as pd
import numpy as np
from pathlib import Path

# Import custom modules
from src.skill_inference import SkillInferenceEngine
from src.visualization import SkillChainVisualizer
from src.blockchain_verification import CredentialLedger


def print_section(title: str):
    """Print formatted section header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80 + "\n")


def main():
    """Main execution function"""
    
    start_time = time.time()
    
    # Create results directory
    Path('results').mkdir(exist_ok=True)
    
    print_section("SKILLCHAIN DX - APPLIED DEMONSTRATION")
    print("A Blockchain-Enabled AI System for Workforce Skill Development")
    print("Applied Sciences Journal - Demonstration Implementation\n")
    
    # =========================================================================
    # COMPONENT 1: Load Datasets
    # =========================================================================
    print_section("COMPONENT 1: Dataset Loading")
    
    print("Loading synthetic datasets...")
    job_roles = pd.read_csv('data/job_roles.csv')
    courses = pd.read_csv('data/training_courses.csv')
    employees = pd.read_csv('data/employees.csv')
    
    print(f"✓ Job Roles: {len(job_roles)} records")
    print(f"✓ Training Courses: {len(courses)} records")
    print(f"✓ Employees: {len(employees)} records")
    
    # =========================================================================
    # COMPONENT 2: AI Skill Inference
    # =========================================================================
    print_section("COMPONENT 2: AI Skill Inference & Role Matching")
    
    # Initialize skill inference engine
    engine = SkillInferenceEngine(model_name='all-MiniLM-L6-v2')
    engine.load_data('data/job_roles.csv', 'data/training_courses.csv', 'data/employees.csv')
    
    # Generate recommendations for all employees
    print("\nGenerating role recommendations...")
    recommendations = engine.generate_recommendations_report('results/recommendations_report.json')
    
    # Display example recommendation
    print("\n--- EXAMPLE RECOMMENDATION ---")
    example_emp = 'EMP001'
    example_data = recommendations[example_emp]
    print(f"Employee: {example_data['name']}")
    print(f"Current Role: {example_data['current_role']}")
    print(f"\nTop 3 Recommended Roles:")
    for i, rec in enumerate(example_data['top_recommendations'][:3], 1):
        print(f"  {i}. {rec['role_title']} - Match: {rec['similarity_percentage']:.1f}%")
    
    # Skill gap analysis
    print(f"\nSkill Gap Analysis for Top Recommendation:")
    gap_analysis = example_data['skill_gap_analysis']
    print(f"  Target Role: {gap_analysis['target_role']}")
    print(f"  Current Match: {gap_analysis['similarity_score']:.1f}%")
    print(f"  Skills to Acquire: {gap_analysis['gap_count']}")
    if gap_analysis['skill_gaps']:
        print(f"  Missing Skills: {', '.join(gap_analysis['skill_gaps'][:5])}")
    
    # =========================================================================
    # COMPONENT 3: Blockchain Credential Verification
    # =========================================================================
    print_section("COMPONENT 3: Blockchain Credential Verification")
    
    # Initialize credential ledger
    ledger = CredentialLedger('data/credential_ledger.json')
    
    print("Issuing credentials for employee course completions...\n")
    
    # Issue credentials for sample employees
    sample_credentials = [
        ('EMP001', 'TC001', 'Python for Data Analysis', '2024-03-15'),
        ('EMP001', 'TC002', 'Advanced SQL for Data Scientists', '2024-05-20'),
        ('EMP003', 'TC003', 'Machine Learning Specialization', '2024-06-10'),
        ('EMP005', 'TC022', 'Tableau Advanced Analytics', '2024-08-01'),
    ]
    
    for emp_id, course_id, course_name, completion_date in sample_credentials:
        ledger.issue_credential(emp_id, course_id, course_name, completion_date)
    
    # Verify a credential
    print("\n--- CREDENTIAL VERIFICATION DEMO ---")
    print("Verifying: EMP001 completed 'Python for Data Analysis'")
    verification = ledger.verify_credential(
        'EMP001', 'TC001', 'Python for Data Analysis', '2024-03-15'
    )
    print(f"Result: {'✓ VERIFIED' if verification['verified'] else '✗ NOT VERIFIED'}")
    print(f"Hash: {verification['hash'][:32]}...")
    
    # Test invalid credential
    print("\nVerifying: EMP001 completed 'Fake Course' (should fail)")
    verification_fail = ledger.verify_credential(
        'EMP001', 'TC999', 'Fake Course', '2024-01-01'
    )
    print(f"Result: {'✓ VERIFIED' if verification_fail['verified'] else '✗ NOT VERIFIED'}")
    print(f"Message: {verification_fail['message']}")
    
    # Generate verification report
    ledger.generate_verification_report('results/verification_report.json')
    
    # =========================================================================
    # COMPONENT 4: Visualization & Analysis
    # =========================================================================
    print_section("COMPONENT 4: Generating Visualizations")
    
    visualizer = SkillChainVisualizer()
    
    # Create similarity matrix for heatmap
    print("Creating similarity heatmap...")
    similarity_matrix = []
    employee_names = []
    
    for emp_id in employees['employee_id'].head(5):  # Top 5 employees
        emp_data = employees[employees['employee_id'] == emp_id].iloc[0]
        employee_names.append(emp_data['name'])
        
        similarities = engine.compute_role_similarity(emp_id)
        similarity_matrix.append(similarities['similarity_percentage'].head(10).values)
    
    similarity_df = pd.DataFrame(
        similarity_matrix,
        columns=job_roles['role_title'].head(10).tolist()
    )
    
    visualizer.plot_similarity_heatmap(
        similarity_df,
        employee_names,
        job_roles['role_title'].head(10).tolist(),
        'results/similarity_heatmap.png'
    )
    
    # Create bar chart
    print("Creating recommendations bar chart...")
    visualizer.plot_top_recommendations_bar(
        recommendations,
        'results/top_recommendations_bar.png'
    )
    
    # Create similarity table
    print("Creating similarity table...")
    top_recs = engine.get_top_recommendations('EMP001', top_n=5)
    visualizer.create_similarity_table('EMP001', top_recs, 'results/similarity_table.csv')
    
    # =========================================================================
    # COMPONENT 5: Performance Metrics
    # =========================================================================
    print_section("COMPONENT 5: Validation & Performance Metrics")
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Dataset Size:")
    print(f"  - Job Roles: {len(job_roles)}")
    print(f"  - Training Courses: {len(courses)}")
    print(f"  - Employees: {len(employees)}")
    print(f"\nTools Used:")
    print(f"  - AI Model: sentence-transformers (all-MiniLM-L6-v2)")
    print(f"  - Similarity Metric: Cosine Similarity")
    print(f"  - Blockchain: SHA-256 Hashing + Local Ledger")
    print(f"\nExecution Time: {execution_time:.2f} seconds")
    print(f"Credentials Issued: {len(ledger.ledger['credentials'])}")
    print(f"Recommendations Generated: {len(recommendations)}")
    
    # =========================================================================
    # Summary
    # =========================================================================
    print_section("DEMONSTRATION COMPLETE")
    
    print("Generated Outputs:")
    print("  ✓ results/recommendations_report.json")
    print("  ✓ results/verification_report.json")
    print("  ✓ results/similarity_heatmap.png")
    print("  ✓ results/top_recommendations_bar.png")
    print("  ✓ results/similarity_table.csv")
    print("  ✓ data/credential_ledger.json")
    print("\nAll components successfully demonstrated!")
    print("Ready for Applied Sciences paper integration.\n")


if __name__ == "__main__":
    main()

