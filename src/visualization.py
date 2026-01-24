"""
SkillChain DX - Visualization Module
Generate charts and tables for the research paper
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Dict, List
import json


class SkillChainVisualizer:
    """Generate visualizations for SkillChain DX analysis"""

    def __init__(self, style: str = 'seaborn-v0_8-darkgrid'):
        """Initialize visualizer with HIGH RESOLUTION plotting settings"""
        plt.style.use('default')
        sns.set_palette("husl")

        # High resolution settings (min 1000 pixels = 300 DPI * 3.33 inches)
        self.dpi = 300
        plt.rcParams['figure.dpi'] = self.dpi
        plt.rcParams['savefig.dpi'] = self.dpi
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.labelsize'] = 14
        plt.rcParams['axes.titlesize'] = 16
        plt.rcParams['xtick.labelsize'] = 11
        plt.rcParams['ytick.labelsize'] = 11
        plt.rcParams['figure.facecolor'] = 'white'
        plt.rcParams['savefig.facecolor'] = 'white'
        
    def plot_similarity_heatmap(self, similarity_matrix: pd.DataFrame, 
                                employee_names: List[str],
                                role_titles: List[str],
                                output_path: str = 'results/similarity_heatmap.png'):
        """
        Create heatmap of employee-role similarity scores
        
        Args:
            similarity_matrix: Matrix of similarity scores
            employee_names: List of employee names
            role_titles: List of role titles
            output_path: Path to save the figure
        """
        # High resolution: 16x10 inches at 300 DPI = 4800x3000 pixels
        plt.figure(figsize=(16, 10))

        sns.heatmap(similarity_matrix,
                   annot=True, 
                   fmt='.1f',
                   cmap='YlOrRd',
                   xticklabels=role_titles,
                   yticklabels=employee_names,
                   cbar_kws={'label': 'Similarity Score (%)'},
                   vmin=0,
                   vmax=100)
        
        plt.title('Employee-Role Skill Similarity Matrix', fontsize=18, fontweight='bold', pad=20)
        plt.xlabel('Job Roles', fontsize=14, fontweight='bold')
        plt.ylabel('Employees', fontsize=14, fontweight='bold')
        plt.xticks(rotation=45, ha='right', fontsize=11)
        plt.yticks(rotation=0, fontsize=11)
        plt.tight_layout()
        plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
        print(f"Heatmap saved to {output_path} (High Resolution: 4800x3000 pixels)")
        plt.close()
        
    def plot_top_recommendations_bar(self, recommendations: Dict,
                                    output_path: str = 'results/top_recommendations_bar.png'):
        """
        Create bar chart showing top recommendations for each employee
        
        Args:
            recommendations: Dictionary with employee recommendations
            output_path: Path to save the figure
        """
        # High resolution: 14x10 inches at 300 DPI = 4200x3000 pixels
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Prepare data
        employees = []
        roles = []
        scores = []
        
        for emp_id, data in recommendations.items():
            emp_name = data['name']
            top_rec = data['top_recommendations'][0]  # Get top recommendation
            
            employees.append(f"{emp_name}\n({data['current_role']})")
            roles.append(top_rec['role_title'])
            scores.append(top_rec['similarity_percentage'])
        
        # Create bar chart
        y_pos = np.arange(len(employees))
        bars = ax.barh(y_pos, scores, color=sns.color_palette("viridis", len(employees)))
        
        # Customize
        ax.set_yticks(y_pos)
        ax.set_yticklabels(employees, fontsize=12)
        ax.set_xlabel('Similarity Score (%)', fontsize=14, fontweight='bold')
        ax.set_title('Top Role Recommendations by Employee', fontsize=18, fontweight='bold', pad=20)
        ax.set_xlim(0, 100)

        # Add value labels and role names
        for i, (bar, role, score) in enumerate(zip(bars, roles, scores)):
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height()/2,
                   f'{score:.1f}%\n→ {role}',
                   ha='left', va='center', fontsize=11, fontweight='bold')

        plt.tight_layout()
        plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
        print(f"Bar chart saved to {output_path} (High Resolution)")
        plt.close()
        
    def plot_skill_gap_analysis(self, skill_gaps: Dict,
                               output_path: str = 'results/skill_gap_analysis.png'):
        """
        Create visualization of skill gaps for selected employees
        
        Args:
            skill_gaps: Dictionary with skill gap data
            output_path: Path to save the figure
        """
        # High resolution: 16x8 inches at 300 DPI = 4800x2400 pixels
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Extract data
        employees = list(skill_gaps.keys())
        gap_counts = [skill_gaps[emp]['gap_count'] for emp in employees]
        similarity_scores = [skill_gaps[emp]['similarity_score'] for emp in employees]
        
        # Plot 1: Skill gap counts
        colors1 = sns.color_palette("Reds_r", len(employees))
        ax1.bar(range(len(employees)), gap_counts, color=colors1)
        ax1.set_xticks(range(len(employees)))
        ax1.set_xticklabels(employees, rotation=45, ha='right', fontsize=12)
        ax1.set_ylabel('Number of Missing Skills', fontsize=14, fontweight='bold')
        ax1.set_title('Skill Gaps for Target Roles', fontsize=16, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)

        # Plot 2: Current similarity scores
        colors2 = sns.color_palette("Greens", len(employees))
        ax2.bar(range(len(employees)), similarity_scores, color=colors2)
        ax2.set_xticks(range(len(employees)))
        ax2.set_xticklabels(employees, rotation=45, ha='right', fontsize=12)
        ax2.set_ylabel('Similarity Score (%)', fontsize=14, fontweight='bold')
        ax2.set_title('Current Match with Target Role', fontsize=16, fontweight='bold')
        ax2.set_ylim(0, 100)
        ax2.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
        print(f"Skill gap analysis saved to {output_path} (High Resolution)")
        plt.close()
        
    def create_similarity_table(self, employee_id: str, 
                               recommendations: pd.DataFrame,
                               output_path: str = 'results/similarity_table.csv'):
        """
        Create formatted similarity table for paper
        
        Args:
            employee_id: Employee identifier
            recommendations: DataFrame with recommendations
            output_path: Path to save the table
        """
        # Format for paper presentation
        table = recommendations.copy()
        table = table.rename(columns={
            'role_id': 'Role ID',
            'role_title': 'Role Title',
            'similarity_percentage': 'Match Score (%)'
        })
        
        table = table[['Role ID', 'Role Title', 'Match Score (%)']]
        table.to_csv(output_path, index=False)
        print(f"Similarity table saved to {output_path}")
        return table

