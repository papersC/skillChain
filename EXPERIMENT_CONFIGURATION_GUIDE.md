# SkillChain DX - Experiment Configuration Documentation Guide

## 📄 Document Overview

**File**: `results/SkillChain_DX_Experiment_Configuration.docx`

This comprehensive configuration document provides complete specifications for all experimental parameters, settings, and configurations used in the SkillChain DX research project. It serves as the definitive reference for reproducibility, validation, and future research extensions.

---

## 📋 Document Structure

### **Section 1: System Configuration**
Complete hardware and software environment specifications including:
- **Hardware Requirements**: CPU, RAM, storage, GPU specifications
- **Software Dependencies**: Python packages with exact versions
- **Model Configuration**: Embedding model parameters and specifications
  - Model: all-MiniLM-L6-v2
  - Embedding dimension: 384
  - Model size: 22.7 MB
  - Max sequence length: 256 tokens

### **Section 2: Dataset Configuration**
Detailed specifications for all three datasets:

#### **2.1 Job Roles Dataset**
- Total records: 15 job roles
- Fields: role_id, role_name, description, required_skills
- Domains: Data Science, Engineering, Management, Analytics
- Skill count: 5-12 skills per role

#### **2.2 Training Courses Dataset**
- Total records: 25 training courses
- Fields: course_id, course_name, provider, skills_taught, duration, difficulty
- Providers: Coursera, edX, Udacity, LinkedIn Learning, Pluralsight
- Duration: 4-40 hours
- Difficulty: Beginner, Intermediate, Advanced

#### **2.3 Employees Dataset**
- Total records: 10 employee profiles
- Fields: employee_id, name, current_role, completed_courses, years_experience
- Experience range: 2-10 years
- Roles: Data Analyst, Engineer, Scientist, Manager

---

### **Section 3: Experiment Configurations**
Detailed parameter specifications for all 6 experiments:

#### **Experiment 1: Similarity Threshold Analysis**
- **Objective**: Determine optimal similarity threshold
- **Thresholds tested**: 50%, 60%, 70%, 75%, 80%, 85%, 90%
- **Total comparisons**: 150 (10 employees × 15 roles)
- **Metrics**: Avg recommendations, qualified employees, avg top score
- **Hypothesis**: 70-75% threshold provides optimal balance

#### **Experiment 2: Skill Gap Progression**
- **Objective**: Track skill development through training
- **Test subject**: Employee EMP001 (Data Analyst)
- **Target role**: Data Strategy Officer
- **Progression stages**: 4 (Initial + 3 courses)
- **Courses**: Data Governance, Leadership, Business Intelligence
- **Expected improvement**: +10-15% similarity score
- **Expected gap reduction**: 5 gaps → 1-2 gaps

#### **Experiment 3: Blockchain Performance**
- **Objective**: Evaluate blockchain credential operations
- **Operations**: Issue credentials, Verify credentials
- **Credential counts**: 10, 50, 100, 500
- **Hash algorithm**: SHA-256
- **Metrics**: Execution time (ms), throughput (ops/sec)
- **Expected throughput**: >1000 ops/sec for verification
- **Expected complexity**: Linear O(n)

#### **Experiment 4: Embedding Model Comparison**
- **Objective**: Compare sentence-transformer models
- **Models tested**: 
  - all-MiniLM-L6-v2 (22.7 MB)
  - all-MiniLM-L12-v2 (33.4 MB)
  - paraphrase-MiniLM-L6-v2 (22.7 MB)
- **Metrics**: Avg similarity, std dev, inference time, model size
- **Expected winner**: all-MiniLM-L6-v2 (speed/accuracy balance)
- **Accuracy tolerance**: ±2% acceptable

#### **Experiment 5: Scalability Analysis**
- **Objective**: Evaluate system scalability
- **Employee counts**: 10, 50, 100
- **Role counts**: 15, 50, 100
- **Scenarios**: 6 combinations
- **Comparison range**: 150 to 10,000
- **Expected complexity**: O(n×m)
- **Expected R²**: >0.95 (linear correlation)

#### **Experiment 6: Score Distribution Analysis**
- **Objective**: Analyze statistical distribution
- **Sample size**: 150 comparisons
- **Statistics**: Mean, median, std dev, quartiles
- **Distribution tests**: Histogram, box plot, Q-Q plot
- **Expected mean**: 60-70%
- **Expected std dev**: 10-20%
- **Hypothesis**: Right-skewed distribution

---

### **Section 4: Algorithm Configurations**

#### **4.1 Skill Matching Algorithm**
- **Similarity metric**: Cosine similarity
- **Embedding method**: Sentence-BERT (all-MiniLM-L6-v2)
- **Text preprocessing**: Lowercase, whitespace normalization
- **Skill aggregation**: Concatenate with space separator
- **Normalization**: L2 normalization (automatic)
- **Batch processing**: Enabled (batch size: 32)
- **Score range**: 0.0 to 1.0 (converted to 0-100%)
- **Top-K recommendations**: K=5

#### **4.2 Skill Gap Analysis Algorithm**
- **Gap detection**: Set difference (required - possessed)
- **Skill extraction**: Parse comma-separated lists
- **Matching strategy**: Exact string match (case-insensitive)
- **Gap prioritization**: By frequency in high-similarity roles
- **Course recommendation**: Match gap skills to course skills
- **Recommendation limit**: Top 3 courses per gap skill

#### **4.3 Blockchain Credential Algorithm**
- **Hash function**: SHA-256
- **Hash input**: JSON string of credential data
- **Credential ID format**: CRED_XXXX (sequential)
- **Timestamp format**: ISO 8601
- **Previous hash**: SHA-256 of previous credential
- **Genesis block**: Hash of zeros
- **Ledger storage**: In-memory list (production: database)
- **Verification**: Recompute hash and compare

---

### **Section 5: Evaluation Metrics**

#### **5.1 Recommendation Quality Metrics**
| Metric | Formula/Method | Target Value |
|--------|---------------|--------------|
| Average Similarity Score | Mean of all scores | 60-70% |
| Top Match Score | Highest per employee | >80% |
| Recommendations per Employee | Count above threshold | 3-5 |
| Score Standard Deviation | Std dev of all scores | 10-20% |
| Coverage | % with ≥1 recommendation | 100% |
| Precision@K | Relevant in top K | >70% |

#### **5.2 Performance Metrics**
| Metric | Measurement | Target |
|--------|------------|--------|
| Inference Time | time.time() | <100ms per batch |
| Comparison Time | Cosine similarity | <1ms per pair |
| Total Processing | End-to-end | <5s for 150 pairs |
| Throughput | Ops per second | >1000 ops/sec |
| Memory Usage | Peak RAM | <500 MB |
| Model Load Time | Initial load | <5 seconds |

#### **5.3 Scalability Metrics**
| Metric | Measurement | Target |
|--------|------------|--------|
| Complexity Class | Big-O analysis | O(n×m) |
| Linear Correlation (R²) | Regression | >0.95 |
| Per-Comparison Time | Total/comparisons | 50-100 μs |
| Scalability Factor | 10× data increase | <10× time |
| Extrapolated Performance | 1000×100 | <10 seconds |

---

### **Section 6: Visualization Configurations**

#### **General Plotting Parameters**
- Figure size: 6 inches width
- DPI: 300 (publication quality)
- Font: DejaVu Sans, 10-12pt
- Color palette: Seaborn default (colorblind-friendly)
- Grid: Light gray, alpha=0.3
- File format: PNG with tight layout

#### **Plot-Specific Settings**
- **Heatmap**: YlOrRd colormap, 0-100% range, annotations enabled
- **Bar Chart**: Horizontal, steelblue color, value labels enabled
- **Line Plot**: Markers enabled, grid on, legend positioned
- **Scatter Plot**: Alpha=0.6, regression line when applicable

---

### **Section 7: Reproducibility Guidelines**

Complete step-by-step instructions for:
1. **Environment Setup**: Python installation, package installation
2. **Data Preparation**: File placement, format verification
3. **Experiment Execution**: Command-line instructions
4. **Random Seed Configuration**: All seeds set to 42
5. **Expected Outputs**: List of all generated files

---

### **Section 8: Validation Criteria**

Comprehensive validation checklists for:
- **Data Validation**: Record counts, missing values, formats
- **Model Validation**: Loading, dimensions, score ranges
- **Results Validation**: Expected ranges for all metrics

---

### **Section 9: Appendix**

Additional resources including:
- **File Structure**: Complete project directory tree
- **Key Dependencies**: Full requirements.txt
- **Troubleshooting**: Common issues and solutions
- **Contact Information**: Support resources
- **Version History**: Document changelog

---

## 🎯 Purpose and Use Cases

This configuration document is designed for:

### **1. Reproducibility**
- Exact specifications enable independent verification
- All parameters documented for replication
- Random seeds ensure deterministic results

### **2. Validation**
- Validation criteria for all components
- Expected ranges for all metrics
- Quality assurance checklists

### **3. Extension**
- Clear baseline for future research
- Parameter modification guidelines
- Scalability projections

### **4. Peer Review**
- Complete transparency for reviewers
- Detailed methodology documentation
- Justification for all design choices

### **5. Production Deployment**
- Configuration templates for real systems
- Performance benchmarks
- Scalability guidelines

---

## 📊 Key Highlights

✅ **Complete Specifications**: Every parameter documented  
✅ **Reproducible**: Step-by-step instructions included  
✅ **Validated**: Validation criteria for all components  
✅ **Professional**: Publication-quality formatting  
✅ **Comprehensive**: 9 sections, 50+ pages of detail  

---

## 🚀 Quick Start

1. **Open the document**: `results/SkillChain_DX_Experiment_Configuration.docx`
2. **Review Section 1**: Verify your environment matches specifications
3. **Follow Section 7**: Execute reproducibility guidelines
4. **Validate with Section 8**: Confirm results match expected ranges

---

## 📁 Related Documents

- **Research Paper**: `results/SkillChain_DX_Implementation_Results.docx`
- **Results Summary**: `EXPERIMENTAL_RESULTS_SUMMARY.md`
- **Figures Guide**: `FIGURES_INCLUDED.md`
- **Quick Start**: `QUICK_START_GUIDE.md`

---

## ✨ Document Features

- **50+ detailed tables** with specifications
- **Professional formatting** with consistent styling
- **Complete parameter coverage** for all experiments
- **Validation checklists** for quality assurance
- **Troubleshooting guide** for common issues
- **Version tracking** for document updates

---

**Generated**: 2026-01-12  
**Version**: 1.0  
**Status**: Production-Ready  
**Format**: Microsoft Word (.docx)  
**Pages**: ~50 pages  
**Purpose**: Complete experimental configuration reference

