"""
SkillChain DX - Experimental Visualizations
Publication-quality figures for research journal
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from typing import Dict, List
from pathlib import Path


class ExperimentVisualizer:
    """Generate publication-quality visualizations for experiments"""

    def __init__(self):
        """Initialize visualizer with publication settings"""
        # Set HIGH RESOLUTION publication-quality defaults
        # Minimum 1000 pixels = 300 DPI * 3.33 inches, so we use larger figures
        self.dpi = 300
        plt.rcParams['figure.dpi'] = self.dpi
        plt.rcParams['savefig.dpi'] = self.dpi
        plt.rcParams['font.size'] = 12
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['axes.labelsize'] = 14
        plt.rcParams['axes.titlesize'] = 16
        plt.rcParams['xtick.labelsize'] = 11
        plt.rcParams['ytick.labelsize'] = 11
        plt.rcParams['legend.fontsize'] = 11
        plt.rcParams['figure.facecolor'] = 'white'
        plt.rcParams['axes.facecolor'] = 'white'
        plt.rcParams['savefig.facecolor'] = 'white'

        # Color palette
        self.colors = sns.color_palette("husl", 8)

        # Minimum figure size to ensure 1000+ pixels at 300 DPI
        # 1000 pixels / 300 DPI = 3.33 inches minimum
        # Using 4+ inches for safety margin
        self.min_fig_width = 14  # 14 * 300 = 4200 pixels
        self.min_fig_height = 10  # 10 * 300 = 3000 pixels
        
    def plot_exp1_threshold_analysis(self, results: Dict, output_path: str):
        """
        Visualize Experiment 1: Threshold Analysis
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(self.min_fig_width, self.min_fig_height))
        
        thresholds = results['threshold']
        
        # Plot 1: Average recommendations vs threshold
        ax1.plot(thresholds, results['avg_recommendations'], 
                marker='o', linewidth=2, markersize=8, color=self.colors[0])
        ax1.set_xlabel('Similarity Threshold (%)')
        ax1.set_ylabel('Avg. Recommendations per Employee')
        ax1.set_title('(a) Recommendation Count vs Threshold')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(45, 95)
        
        # Plot 2: Qualified employees vs threshold
        ax2.plot(thresholds, results['qualified_employees'],
                marker='s', linewidth=2, markersize=8, color=self.colors[1])
        ax2.set_xlabel('Similarity Threshold (%)')
        ax2.set_ylabel('Number of Qualified Employees')
        ax2.set_title('(b) Qualified Employees vs Threshold')
        ax2.grid(True, alpha=0.3)
        ax2.set_xlim(45, 95)
        
        # Plot 3: Average top score vs threshold
        ax3.plot(thresholds, results['avg_top_score'],
                marker='^', linewidth=2, markersize=8, color=self.colors[2])
        ax3.set_xlabel('Similarity Threshold (%)')
        ax3.set_ylabel('Average Top Match Score (%)')
        ax3.set_title('(c) Top Match Quality vs Threshold')
        ax3.grid(True, alpha=0.3)
        ax3.set_xlim(45, 95)
        
        # Plot 4: Combined view
        ax4_twin = ax4.twinx()
        line1 = ax4.plot(thresholds, results['avg_recommendations'],
                        marker='o', linewidth=2, label='Avg. Recommendations',
                        color=self.colors[0])
        line2 = ax4_twin.plot(thresholds, results['qualified_employees'],
                             marker='s', linewidth=2, label='Qualified Employees',
                             color=self.colors[1])
        
        ax4.set_xlabel('Similarity Threshold (%)')
        ax4.set_ylabel('Avg. Recommendations', color=self.colors[0])
        ax4_twin.set_ylabel('Qualified Employees', color=self.colors[1])
        ax4.set_title('(d) Combined Analysis')
        ax4.tick_params(axis='y', labelcolor=self.colors[0])
        ax4_twin.tick_params(axis='y', labelcolor=self.colors[1])
        ax4.grid(True, alpha=0.3)
        ax4.set_xlim(45, 95)
        
        # Combined legend
        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax4.legend(lines, labels, loc='upper right')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
        print(f"✓ Saved: {output_path} (High Resolution: {self.min_fig_width*self.dpi}x{self.min_fig_height*self.dpi} pixels)")
        plt.close()

    def plot_exp2_skill_progression(self, results: Dict, output_path: str):
        """
        Visualize Experiment 2: Skill Gap Progression
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(self.min_fig_width, 7))
        
        stages = results['stage']
        x_pos = np.arange(len(stages))
        
        # Plot 1: Similarity score progression
        ax1.plot(x_pos, results['similarity_score'],
                marker='o', linewidth=2.5, markersize=10,
                color=self.colors[3], label='Similarity Score')
        ax1.fill_between(x_pos, results['similarity_score'], alpha=0.3, color=self.colors[3])
        ax1.set_xticks(x_pos)
        ax1.set_xticklabels(stages, rotation=15, ha='right')
        ax1.set_ylabel('Similarity Score (%)')
        ax1.set_title('(a) Skill Match Progression')
        ax1.set_ylim(0, 100)
        ax1.grid(True, alpha=0.3, axis='y')
        ax1.legend()
        
        # Add value labels
        for i, score in enumerate(results['similarity_score']):
            ax1.text(i, score + 2, f'{score:.1f}%', ha='center', fontsize=9, fontweight='bold')
        
        # Plot 2: Skill gaps reduction
        ax2.bar(x_pos, results['skill_gaps'], color=self.colors[4], alpha=0.7, edgecolor='black')
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(stages, rotation=15, ha='right')
        ax2.set_ylabel('Number of Skill Gaps')
        ax2.set_title('(b) Skill Gap Reduction')
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for i, gaps in enumerate(results['skill_gaps']):
            ax2.text(i, gaps + 0.2, str(gaps), ha='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
        print(f"✓ Saved: {output_path} (High Resolution)")
        plt.close()

    def plot_exp3_blockchain_performance(self, results: Dict, output_path: str):
        """
        Visualize Experiment 3: Blockchain Performance
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(self.min_fig_width, self.min_fig_height))
        
        df = pd.DataFrame(results)
        issue_df = df[df['operation'] == 'Issue']
        verify_df = df[df['operation'] == 'Verify']
        
        # Plot 1: Execution time comparison
        width = 0.35
        x = np.arange(len(issue_df))
        ax1.bar(x - width/2, issue_df['time_ms'], width, label='Issue', color=self.colors[0], alpha=0.8)
        ax1.bar(x + width/2, verify_df['time_ms'], width, label='Verify', color=self.colors[1], alpha=0.8)
        ax1.set_xlabel('Number of Credentials')
        ax1.set_ylabel('Execution Time (ms)')
        ax1.set_title('(a) Execution Time Comparison')
        ax1.set_xticks(x)
        ax1.set_xticklabels(issue_df['num_credentials'])
        ax1.legend()
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Plot 2: Throughput comparison
        ax2.bar(x - width/2, issue_df['throughput'], width, label='Issue', color=self.colors[0], alpha=0.8)
        ax2.bar(x + width/2, verify_df['throughput'], width, label='Verify', color=self.colors[1], alpha=0.8)
        ax2.set_xlabel('Number of Credentials')
        ax2.set_ylabel('Throughput (ops/sec)')
        ax2.set_title('(b) Throughput Comparison')
        ax2.set_xticks(x)
        ax2.set_xticklabels(issue_df['num_credentials'])
        ax2.legend()
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Plot 3: Scalability - Issue operations
        ax3.plot(issue_df['num_credentials'], issue_df['time_ms'],
                marker='o', linewidth=2, markersize=8, color=self.colors[0])
        ax3.set_xlabel('Number of Credentials')
        ax3.set_ylabel('Execution Time (ms)')
        ax3.set_title('(c) Issue Operation Scalability')
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: Scalability - Verify operations
        ax4.plot(verify_df['num_credentials'], verify_df['time_ms'],
                marker='s', linewidth=2, markersize=8, color=self.colors[1])
        ax4.set_xlabel('Number of Credentials')
        ax4.set_ylabel('Execution Time (ms)')
        ax4.set_title('(d) Verify Operation Scalability')
        ax4.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
        print(f"✓ Saved: {output_path} (High Resolution)")
        plt.close()

    def plot_exp4_model_comparison(self, results: Dict, output_path: str):
        """
        Visualize Experiment 4: Model Comparison
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(self.min_fig_width, self.min_fig_height))

        df = pd.DataFrame(results)
        x_pos = np.arange(len(df))

        # Plot 1: Average similarity scores
        bars1 = ax1.bar(x_pos, df['avg_similarity'], color=self.colors[2], alpha=0.7, edgecolor='black')
        ax1.errorbar(x_pos, df['avg_similarity'], yerr=df['std_similarity'],
                    fmt='none', ecolor='black', capsize=5, capthick=2)
        ax1.set_xticks(x_pos)
        ax1.set_xticklabels(df['model'], rotation=15, ha='right')
        ax1.set_ylabel('Average Similarity Score (%)')
        ax1.set_title('(a) Model Similarity Scores')
        ax1.grid(True, alpha=0.3, axis='y')

        # Add value labels
        for i, (avg, std) in enumerate(zip(df['avg_similarity'], df['std_similarity'])):
            ax1.text(i, avg + std + 1, f'{avg:.1f}±{std:.1f}', ha='center', fontsize=8)

        # Plot 2: Inference time
        bars2 = ax2.bar(x_pos, df['inference_time_ms'], color=self.colors[3], alpha=0.7, edgecolor='black')
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(df['model'], rotation=15, ha='right')
        ax2.set_ylabel('Inference Time (ms)')
        ax2.set_title('(b) Model Inference Speed')
        ax2.grid(True, alpha=0.3, axis='y')

        # Add value labels
        for i, time_val in enumerate(df['inference_time_ms']):
            ax2.text(i, time_val + 1, f'{time_val:.1f}', ha='center', fontsize=9)

        # Plot 3: Model size
        bars3 = ax3.bar(x_pos, df['model_size_mb'], color=self.colors[4], alpha=0.7, edgecolor='black')
        ax3.set_xticks(x_pos)
        ax3.set_xticklabels(df['model'], rotation=15, ha='right')
        ax3.set_ylabel('Model Size (MB)')
        ax3.set_title('(c) Model Size Comparison')
        ax3.grid(True, alpha=0.3, axis='y')

        # Add value labels
        for i, size in enumerate(df['model_size_mb']):
            ax3.text(i, size + 0.5, f'{size:.1f}', ha='center', fontsize=9)

        # Plot 4: Efficiency (similarity per ms)
        efficiency = df['avg_similarity'] / df['inference_time_ms']
        bars4 = ax4.bar(x_pos, efficiency, color=self.colors[5], alpha=0.7, edgecolor='black')
        ax4.set_xticks(x_pos)
        ax4.set_xticklabels(df['model'], rotation=15, ha='right')
        ax4.set_ylabel('Efficiency (Score/ms)')
        ax4.set_title('(d) Model Efficiency')
        ax4.grid(True, alpha=0.3, axis='y')

        # Add value labels
        for i, eff in enumerate(efficiency):
            ax4.text(i, eff + 0.05, f'{eff:.2f}', ha='center', fontsize=9)

        plt.tight_layout()
        plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
        print(f"✓ Saved: {output_path} (High Resolution)")
        plt.close()

    def plot_exp5_scalability(self, results: Dict, output_path: str):
        """
        Visualize Experiment 5: Scalability Analysis
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(self.min_fig_width, self.min_fig_height))

        df = pd.DataFrame(results)

        # Plot 1: Computation time vs total comparisons
        scatter1 = ax1.scatter(df['total_comparisons'], df['computation_time_ms'],
                              s=100, c=df['num_employees'], cmap='viridis', alpha=0.7, edgecolors='black')
        ax1.set_xlabel('Total Comparisons')
        ax1.set_ylabel('Computation Time (ms)')
        ax1.set_title('(a) Scalability: Time vs Comparisons')
        ax1.grid(True, alpha=0.3)
        cbar1 = plt.colorbar(scatter1, ax=ax1)
        cbar1.set_label('Employees')

        # Plot 2: Time per comparison
        ax2.plot(df['total_comparisons'], df['time_per_comparison_us'],
                marker='o', linewidth=2, markersize=8, color=self.colors[6])
        ax2.set_xlabel('Total Comparisons')
        ax2.set_ylabel('Time per Comparison (μs)')
        ax2.set_title('(b) Per-Comparison Efficiency')
        ax2.grid(True, alpha=0.3)

        # Plot 3: 3D surface-like view (employees vs roles)
        pivot_time = df.pivot_table(values='computation_time_ms',
                                    index='num_employees',
                                    columns='num_roles',
                                    aggfunc='first')

        sns.heatmap(pivot_time, annot=True, fmt='.1f', cmap='YlOrRd',
                   ax=ax3, cbar_kws={'label': 'Time (ms)'})
        ax3.set_xlabel('Number of Roles')
        ax3.set_ylabel('Number of Employees')
        ax3.set_title('(c) Computation Time Heatmap')

        # Plot 4: Linear scalability check
        ax4.scatter(df['total_comparisons'], df['computation_time_ms'],
                   s=100, alpha=0.7, color=self.colors[0], edgecolors='black', label='Actual')

        # Fit linear model
        z = np.polyfit(df['total_comparisons'], df['computation_time_ms'], 1)
        p = np.poly1d(z)
        x_line = np.linspace(df['total_comparisons'].min(), df['total_comparisons'].max(), 100)
        ax4.plot(x_line, p(x_line), 'r--', linewidth=2, label=f'Linear Fit')

        ax4.set_xlabel('Total Comparisons')
        ax4.set_ylabel('Computation Time (ms)')
        ax4.set_title('(d) Linear Scalability Analysis')
        ax4.legend()
        ax4.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
        print(f"✓ Saved: {output_path} (High Resolution)")
        plt.close()

    def plot_exp6_distribution(self, results: Dict, output_path: str):
        """
        Visualize Experiment 6: Score Distribution
        """
        fig = plt.figure(figsize=(self.min_fig_width, 12))
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

        ax1 = fig.add_subplot(gs[0, :2])
        ax2 = fig.add_subplot(gs[0, 2])
        ax3 = fig.add_subplot(gs[1, :2])
        ax4 = fig.add_subplot(gs[1, 2])
        ax5 = fig.add_subplot(gs[2, :])

        all_scores = results['all_scores']
        top_scores = results['top_scores']
        stats = results['statistics']

        # Plot 1: Histogram of all scores
        ax1.hist(all_scores, bins=30, color=self.colors[0], alpha=0.7, edgecolor='black')
        ax1.axvline(stats['mean'], color='red', linestyle='--', linewidth=2, label=f'Mean: {stats["mean"]:.1f}%')
        ax1.axvline(stats['median'], color='green', linestyle='--', linewidth=2, label=f'Median: {stats["median"]:.1f}%')
        ax1.set_xlabel('Similarity Score (%)')
        ax1.set_ylabel('Frequency')
        ax1.set_title('(a) Distribution of All Similarity Scores')
        ax1.legend()
        ax1.grid(True, alpha=0.3, axis='y')

        # Plot 2: Box plot
        ax2.boxplot(all_scores, vert=True)
        ax2.set_ylabel('Similarity Score (%)')
        ax2.set_title('(b) Box Plot')
        ax2.grid(True, alpha=0.3, axis='y')

        # Plot 3: Top scores distribution
        ax3.hist(top_scores, bins=15, color=self.colors[1], alpha=0.7, edgecolor='black')
        ax3.axvline(np.mean(top_scores), color='red', linestyle='--', linewidth=2,
                   label=f'Mean: {np.mean(top_scores):.1f}%')
        ax3.set_xlabel('Top Match Score (%)')
        ax3.set_ylabel('Frequency')
        ax3.set_title('(c) Distribution of Top Match Scores')
        ax3.legend()
        ax3.grid(True, alpha=0.3, axis='y')

        # Plot 4: Cumulative distribution
        sorted_scores = np.sort(all_scores)
        cumulative = np.arange(1, len(sorted_scores) + 1) / len(sorted_scores) * 100
        ax4.plot(sorted_scores, cumulative, linewidth=2, color=self.colors[2])
        ax4.set_xlabel('Similarity Score (%)')
        ax4.set_ylabel('Cumulative Percentage (%)')
        ax4.set_title('(d) Cumulative Distribution')
        ax4.grid(True, alpha=0.3)

        # Plot 5: Employee-wise statistics
        emp_df = pd.DataFrame(results['employee_data'])
        x_pos = np.arange(len(emp_df))

        ax5.bar(x_pos - 0.2, emp_df['roles_above_70'], 0.4,
               label='Roles >70%', color=self.colors[2], alpha=0.7)
        ax5.bar(x_pos + 0.2, emp_df['roles_above_80'], 0.4,
               label='Roles >80%', color=self.colors[3], alpha=0.7)
        ax5.set_xticks(x_pos)
        ax5.set_xticklabels(emp_df['employee_id'], rotation=45)
        ax5.set_xlabel('Employee ID')
        ax5.set_ylabel('Number of Qualifying Roles')
        ax5.set_title('(e) High-Match Roles per Employee')
        ax5.legend()
        ax5.grid(True, alpha=0.3, axis='y')

        plt.savefig(output_path, dpi=self.dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
        print(f"✓ Saved: {output_path} (High Resolution)")
        plt.close()

