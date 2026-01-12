"""
SkillChain DX - Comprehensive Experimental Suite
Runs all experiments and generates publication-ready documentation
"""

import sys
import time
from pathlib import Path

# Import custom modules
from src.skill_inference import SkillInferenceEngine
from src.visualization import SkillChainVisualizer
from src.blockchain_verification import CredentialLedger
from src.experiments import SkillChainExperiments
from src.experiment_visualizations import ExperimentVisualizer
from src.docx_generator import ResearchPaperGenerator


def print_header(title: str):
    """Print formatted header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80 + "\n")


def main():
    """Main execution function for comprehensive experiments"""
    
    overall_start = time.time()
    
    print_header("SKILLCHAIN DX - COMPREHENSIVE EXPERIMENTAL SUITE")
    print("Research Paper Implementation and Results Generation")
    print("Applied Sciences Journal Submission\n")
    
    # Create results directory
    Path('results').mkdir(exist_ok=True)
    
    # =========================================================================
    # PHASE 1: Initialize System Components
    # =========================================================================
    print_header("PHASE 1: System Initialization")
    
    print("Initializing AI Skill Inference Engine...")
    engine = SkillInferenceEngine(model_name='all-MiniLM-L6-v2')
    engine.load_data('data/job_roles.csv', 'data/training_courses.csv', 'data/employees.csv')
    
    print("Initializing Blockchain Credential Ledger...")
    ledger = CredentialLedger('data/credential_ledger.json')
    
    print("Initializing Visualization Modules...")
    visualizer = SkillChainVisualizer()
    exp_visualizer = ExperimentVisualizer()
    
    print("Initializing Experimental Framework...")
    experiments = SkillChainExperiments(engine, ledger, visualizer)
    
    print("\n✓ All components initialized successfully")
    
    # =========================================================================
    # PHASE 2: Run Comprehensive Experiments
    # =========================================================================
    print_header("PHASE 2: Running Comprehensive Experiments")
    
    # Experiment 1: Threshold Analysis
    exp1_results = experiments.experiment_1_similarity_threshold_analysis()
    exp_visualizer.plot_exp1_threshold_analysis(
        exp1_results, 
        'results/exp1_threshold_analysis.png'
    )
    
    # Experiment 2: Skill Progression
    exp2_results = experiments.experiment_2_skill_gap_progression()
    exp_visualizer.plot_exp2_skill_progression(
        exp2_results,
        'results/exp2_skill_progression.png'
    )
    
    # Experiment 3: Blockchain Performance
    exp3_results = experiments.experiment_3_blockchain_performance()
    exp_visualizer.plot_exp3_blockchain_performance(
        exp3_results,
        'results/exp3_blockchain_performance.png'
    )
    
    # Experiment 4: Model Comparison
    exp4_results = experiments.experiment_4_model_comparison()
    exp_visualizer.plot_exp4_model_comparison(
        exp4_results,
        'results/exp4_model_comparison.png'
    )
    
    # Experiment 5: Scalability
    exp5_results = experiments.experiment_5_scalability_analysis()
    exp_visualizer.plot_exp5_scalability(
        exp5_results,
        'results/exp5_scalability.png'
    )
    
    # Experiment 6: Distribution Analysis
    exp6_results = experiments.experiment_6_recommendation_distribution()
    exp_visualizer.plot_exp6_distribution(
        exp6_results,
        'results/exp6_distribution.png'
    )
    
    # Save all experimental results
    experiments.save_all_results('results/experimental_results.json')
    
    print("\n✓ All experiments completed successfully")
    
    # =========================================================================
    # PHASE 3: Generate Additional Visualizations
    # =========================================================================
    print_header("PHASE 3: Generating Additional Visualizations")
    
    # Generate basic visualizations from main system
    print("Creating similarity heatmap...")
    import pandas as pd
    import numpy as np
    
    similarity_matrix = []
    employee_names = []
    
    for emp_id in engine.employees['employee_id'].head(10):
        emp_data = engine.employees[engine.employees['employee_id'] == emp_id].iloc[0]
        employee_names.append(emp_data['name'])
        
        similarities = engine.compute_role_similarity(emp_id)
        similarity_matrix.append(similarities['similarity_percentage'].head(15).values)
    
    similarity_df = pd.DataFrame(
        similarity_matrix,
        columns=engine.job_roles['role_title'].head(15).tolist()
    )
    
    visualizer.plot_similarity_heatmap(
        similarity_df,
        employee_names,
        engine.job_roles['role_title'].head(15).tolist(),
        'results/similarity_heatmap.png'
    )
    
    # Generate recommendations report
    print("Generating recommendations report...")
    recommendations = engine.generate_recommendations_report('results/recommendations_report.json')
    
    visualizer.plot_top_recommendations_bar(
        recommendations,
        'results/top_recommendations_bar.png'
    )
    
    # Generate blockchain verification report
    print("Generating blockchain verification report...")
    
    # Issue sample credentials
    sample_credentials = [
        ('EMP001', 'TC001', 'Python for Data Analysis', '2024-03-15'),
        ('EMP001', 'TC002', 'Advanced SQL for Data Scientists', '2024-05-20'),
        ('EMP003', 'TC003', 'Machine Learning Specialization', '2024-06-10'),
        ('EMP005', 'TC022', 'Tableau Advanced Analytics', '2024-08-01'),
        ('EMP007', 'TC010', 'Data Engineering with Apache Spark', '2024-07-15'),
    ]
    
    for emp_id, course_id, course_name, completion_date in sample_credentials:
        ledger.issue_credential(emp_id, course_id, course_name, completion_date)
    
    ledger.generate_verification_report('results/verification_report.json')
    
    print("\n✓ All visualizations generated successfully")
    
    # =========================================================================
    # PHASE 4: Generate Comprehensive DOCX Documentation
    # =========================================================================
    print_header("PHASE 4: Generating Research Paper Documentation")
    
    # Prepare all results for document generation
    all_results = experiments.results
    
    # Generate DOCX document
    doc_generator = ResearchPaperGenerator()
    output_path = doc_generator.generate_document(
        all_results,
        'results/SkillChain_DX_Implementation_Results.docx'
    )
    
    # =========================================================================
    # PHASE 5: Summary and Statistics
    # =========================================================================
    print_header("PHASE 5: Execution Summary")
    
    overall_time = time.time() - overall_start
    
    print("EXPERIMENTAL RESULTS SUMMARY")
    print("-" * 80)
    print(f"Total Execution Time: {overall_time:.2f} seconds ({overall_time/60:.2f} minutes)")
    print(f"\nDataset Statistics:")
    print(f"  - Job Roles: {len(engine.job_roles)}")
    print(f"  - Training Courses: {len(engine.courses)}")
    print(f"  - Employees: {len(engine.employees)}")
    print(f"  - Total Comparisons: {len(engine.employees) * len(engine.job_roles)}")
    print(f"\nExperiments Conducted: 6")
    print(f"  1. Similarity Threshold Analysis (7 thresholds tested)")
    print(f"  2. Skill Gap Progression (4 stages simulated)")
    print(f"  3. Blockchain Performance (8 scenarios tested)")
    print(f"  4. Model Comparison (3 models evaluated)")
    print(f"  5. Scalability Analysis (6 scale scenarios)")
    print(f"  6. Distribution Analysis (150 comparisons analyzed)")
    
    print(f"\nGenerated Outputs:")
    print(f"  ✓ results/SkillChain_DX_Implementation_Results.docx (Main Document)")
    print(f"  ✓ results/experimental_results.json (Raw Data)")
    print(f"  ✓ results/recommendations_report.json")
    print(f"  ✓ results/verification_report.json")
    print(f"  ✓ results/exp1_threshold_analysis.png")
    print(f"  ✓ results/exp2_skill_progression.png")
    print(f"  ✓ results/exp3_blockchain_performance.png")
    print(f"  ✓ results/exp4_model_comparison.png")
    print(f"  ✓ results/exp5_scalability.png")
    print(f"  ✓ results/exp6_distribution.png")
    print(f"  ✓ results/similarity_heatmap.png")
    print(f"  ✓ results/top_recommendations_bar.png")
    
    print(f"\n{'='*80}")
    print(f"  ✓ COMPREHENSIVE EXPERIMENTAL SUITE COMPLETED SUCCESSFULLY")
    print(f"  ✓ Ready for Applied Sciences Journal Submission")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()

