"""
SkillChain DX - Setup and Run Script
Automated setup and execution of comprehensive experiments
"""

import subprocess
import sys
from pathlib import Path


def print_header(title):
    """Print formatted header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80 + "\n")


def check_python_version():
    """Check if Python version is compatible"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required. Current version: {version.major}.{version.minor}")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def install_dependencies():
    """Install required dependencies"""
    print_header("INSTALLING DEPENDENCIES")
    
    print("Installing packages from requirements.txt...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet"
        ])
        print("✓ All dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def verify_data_files():
    """Verify that required data files exist"""
    print_header("VERIFYING DATA FILES")
    
    required_files = [
        'data/job_roles.csv',
        'data/training_courses.csv',
        'data/employees.csv'
    ]
    
    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✓ {file_path}")
        else:
            print(f"❌ Missing: {file_path}")
            all_exist = False
    
    return all_exist


def create_directories():
    """Create necessary directories"""
    print_header("CREATING DIRECTORIES")
    
    directories = ['results', 'data']
    for dir_name in directories:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✓ {dir_name}/")
    
    return True


def run_experiments():
    """Run the comprehensive experimental suite"""
    print_header("RUNNING COMPREHENSIVE EXPERIMENTS")
    
    print("This will take approximately 2-5 minutes...")
    print("(First run downloads AI model ~90MB)\n")
    
    try:
        subprocess.check_call([sys.executable, "run_comprehensive_experiments.py"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Experiments failed: {e}")
        return False


def main():
    """Main setup and execution function"""
    
    print_header("SKILLCHAIN DX - AUTOMATED SETUP AND EXECUTION")
    print("This script will:")
    print("  1. Check Python version")
    print("  2. Install dependencies")
    print("  3. Verify data files")
    print("  4. Create directories")
    print("  5. Run comprehensive experiments")
    print("  6. Generate DOCX documentation")
    
    input("\nPress Enter to continue...")
    
    # Step 1: Check Python version
    if not check_python_version():
        print("\n❌ Setup failed: Incompatible Python version")
        return False
    
    # Step 2: Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed: Could not install dependencies")
        return False
    
    # Step 3: Create directories
    if not create_directories():
        print("\n❌ Setup failed: Could not create directories")
        return False
    
    # Step 4: Verify data files
    if not verify_data_files():
        print("\n❌ Setup failed: Missing required data files")
        print("\nPlease ensure the following files exist:")
        print("  - data/job_roles.csv")
        print("  - data/training_courses.csv")
        print("  - data/employees.csv")
        return False
    
    # Step 5: Run experiments
    print_header("READY TO RUN EXPERIMENTS")
    print("All prerequisites satisfied!")
    
    proceed = input("\nProceed with experimental suite? (y/n): ")
    if proceed.lower() != 'y':
        print("\nExecution cancelled by user.")
        return False
    
    if not run_experiments():
        print("\n❌ Experiments failed")
        return False
    
    # Success!
    print_header("✓ SETUP AND EXECUTION COMPLETED SUCCESSFULLY")
    
    print("Generated outputs:")
    print("  📄 results/SkillChain_DX_Implementation_Results.docx")
    print("  📊 results/exp1_threshold_analysis.png")
    print("  📊 results/exp2_skill_progression.png")
    print("  📊 results/exp3_blockchain_performance.png")
    print("  📊 results/exp4_model_comparison.png")
    print("  📊 results/exp5_scalability.png")
    print("  📊 results/exp6_distribution.png")
    print("  📊 results/similarity_heatmap.png")
    print("  📊 results/top_recommendations_bar.png")
    print("  📋 results/experimental_results.json")
    print("  📋 results/recommendations_report.json")
    print("  📋 results/verification_report.json")
    
    print("\n✓ Ready for Applied Sciences journal submission!")
    print("\nNext steps:")
    print("  1. Open results/SkillChain_DX_Implementation_Results.docx")
    print("  2. Review experimental results and visualizations")
    print("  3. Integrate into your research paper")
    print("  4. See EXPERIMENTAL_GUIDE.md for detailed usage instructions")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

