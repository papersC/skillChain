"""
SkillChain DX - Setup Verification Script
Verifies that all required files and dependencies are in place
"""

import sys
from pathlib import Path


def print_header(title):
    """Print formatted header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80 + "\n")


def check_file(file_path, description):
    """Check if a file exists"""
    if Path(file_path).exists():
        print(f"✓ {description}")
        return True
    else:
        print(f"❌ MISSING: {description}")
        print(f"   Expected: {file_path}")
        return False


def check_directory(dir_path, description):
    """Check if a directory exists"""
    if Path(dir_path).exists() and Path(dir_path).is_dir():
        print(f"✓ {description}")
        return True
    else:
        print(f"❌ MISSING: {description}")
        print(f"   Expected: {dir_path}")
        return False


def check_python_packages():
    """Check if required Python packages are installed"""
    required_packages = [
        ('pandas', 'Data manipulation'),
        ('numpy', 'Numerical computing'),
        ('sklearn', 'Machine learning (scikit-learn)'),
        ('sentence_transformers', 'AI embeddings'),
        ('matplotlib', 'Plotting'),
        ('seaborn', 'Statistical visualization'),
        ('docx', 'DOCX generation (python-docx)'),
    ]
    
    all_installed = True
    for package, description in required_packages:
        try:
            __import__(package)
            print(f"✓ {description} ({package})")
        except ImportError:
            print(f"❌ MISSING: {description} ({package})")
            all_installed = False
    
    return all_installed


def main():
    """Main verification function"""
    
    print_header("SKILLCHAIN DX - SETUP VERIFICATION")
    
    all_checks_passed = True
    
    # Check documentation files
    print_header("Documentation Files")
    all_checks_passed &= check_file('README.md', 'Main README')
    all_checks_passed &= check_file('START_HERE.md', 'Quick start guide')
    all_checks_passed &= check_file('EXPERIMENTAL_GUIDE.md', 'Experimental guide')
    all_checks_passed &= check_file('PAPER_INTEGRATION_GUIDE.md', 'Paper integration guide')
    all_checks_passed &= check_file('POLICY_INSIGHTS.md', 'Policy insights')
    
    # Check data files
    print_header("Data Files")
    all_checks_passed &= check_directory('data', 'Data directory')
    all_checks_passed &= check_file('data/job_roles.csv', 'Job roles dataset')
    all_checks_passed &= check_file('data/training_courses.csv', 'Training courses dataset')
    all_checks_passed &= check_file('data/employees.csv', 'Employees dataset')
    
    # Check source code files
    print_header("Source Code Files")
    all_checks_passed &= check_directory('src', 'Source directory')
    all_checks_passed &= check_file('src/skill_inference.py', 'AI skill inference engine')
    all_checks_passed &= check_file('src/visualization.py', 'Basic visualizations')
    all_checks_passed &= check_file('src/blockchain_verification.py', 'Blockchain verification')
    all_checks_passed &= check_file('src/experiments.py', 'Comprehensive experiments')
    all_checks_passed &= check_file('src/experiment_visualizations.py', 'Experiment visualizations')
    all_checks_passed &= check_file('src/docx_generator.py', 'DOCX document generator')
    
    # Check execution scripts
    print_header("Execution Scripts")
    all_checks_passed &= check_file('main.py', 'Basic demo script')
    all_checks_passed &= check_file('run_comprehensive_experiments.py', 'Comprehensive experimental suite')
    all_checks_passed &= check_file('setup_and_run.py', 'Automated setup script')
    all_checks_passed &= check_file('requirements.txt', 'Python dependencies')
    
    # Check Python version
    print_header("Python Environment")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    else:
        print(f"❌ Python version: {version.major}.{version.minor}.{version.micro}")
        print(f"   Required: Python 3.8+")
        all_checks_passed = False
    
    # Check Python packages
    print_header("Python Packages")
    packages_installed = check_python_packages()
    all_checks_passed &= packages_installed
    
    if not packages_installed:
        print("\nTo install missing packages, run:")
        print("  pip install -r requirements.txt")
    
    # Check results directory
    print_header("Output Directory")
    if not Path('results').exists():
        print("ℹ️  Results directory will be created when experiments run")
        Path('results').mkdir(exist_ok=True)
        print("✓ Created results/ directory")
    else:
        print("✓ Results directory exists")
    
    # Final summary
    print_header("VERIFICATION SUMMARY")
    
    if all_checks_passed:
        print("✅ ALL CHECKS PASSED!")
        print("\nYour SkillChain DX setup is complete and ready to run.")
        print("\nNext steps:")
        print("  1. Read START_HERE.md for quick start guide")
        print("  2. Run: python setup_and_run.py")
        print("  3. Review generated DOCX in results/")
        print("\n" + "="*80)
        return True
    else:
        print("❌ SOME CHECKS FAILED")
        print("\nPlease address the missing items above before running experiments.")
        print("\nCommon fixes:")
        print("  - Install packages: pip install -r requirements.txt")
        print("  - Ensure all files are extracted from the archive")
        print("  - Check Python version (3.8+ required)")
        print("\n" + "="*80)
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

