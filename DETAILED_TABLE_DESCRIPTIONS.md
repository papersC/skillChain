# Detailed Table Descriptions - SkillChain DX Experiment Configuration Document

## 📋 Complete Reference Guide to All Tables

This document provides detailed descriptions of every table in the **SkillChain_DX_Experiment_Configuration.docx** file, explaining the purpose, structure, and content of each table.

---

## 📊 Table of Contents

- [Section 1: System Configuration Tables](#section-1-system-configuration-tables)
- [Section 2: Dataset Configuration Tables](#section-2-dataset-configuration-tables)
- [Section 3: Experiment Configuration Tables](#section-3-experiment-configuration-tables)
- [Section 4: Algorithm Configuration Tables](#section-4-algorithm-configuration-tables)
- [Section 5: Evaluation Metrics Tables](#section-5-evaluation-metrics-tables)
- [Section 6: Visualization Configuration Tables](#section-6-visualization-configuration-tables)
- [Section 7: Reproducibility Tables](#section-7-reproducibility-tables)
- [Section 8: Validation Criteria Tables](#section-8-validation-criteria-tables)
- [Section 9: Appendix Tables](#section-9-appendix-tables)

---

# Section 1: System Configuration Tables

## Table 1.1: Hardware Environment Specifications

**Location**: Section 1.1 - Hardware Environment  
**Dimensions**: 6 rows × 2 columns  
**Style**: Light Grid Accent 1

### Purpose
Documents the minimum and recommended hardware requirements for running all SkillChain DX experiments, ensuring reproducibility across different computing environments.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Component | Text | Hardware component name (Processor, RAM, Storage, etc.) |
| 2 | Specification | Text | Detailed specification or requirement |

### Row-by-Row Content

**Row 1 (Header)**
- Component: "Component"
- Specification: "Specification"

**Row 2: Processor**
- Component: "Processor"
- Specification: "Intel Core i5/i7 or equivalent (2.0+ GHz)"
- **Rationale**: Sufficient for CPU-based transformer inference without GPU acceleration

**Row 3: RAM**
- Component: "RAM"
- Specification: "8 GB minimum, 16 GB recommended"
- **Rationale**: 8GB handles small datasets; 16GB recommended for scalability experiments

**Row 4: Storage**
- Component: "Storage"
- Specification: "10 GB available space (SSD recommended)"
- **Rationale**: Includes model files (~500MB), datasets (~5MB), and results (~100MB)

**Row 5: GPU**
- Component: "GPU"
- Specification: "Not required (CPU-only inference)"
- **Rationale**: Sentence-transformers efficient enough for CPU; GPU optional for speed

**Row 6: Network**
- Component: "Network"
- Specification: "Internet connection for model downloads"
- **Rationale**: First-time model download from HuggingFace (~23MB for all-MiniLM-L6-v2)

### Key Insights
- System designed for accessibility (no GPU required)
- Modest hardware requirements enable wide adoption
- SSD recommended but not required (affects I/O speed only)

---

## Table 1.2: Software Environment Specifications

**Location**: Section 1.2 - Software Environment  
**Dimensions**: 11 rows × 3 columns  
**Style**: Light Grid Accent 1

### Purpose
Provides exact versions of all software dependencies to ensure deterministic, reproducible results across different installations.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Component | Text | Software package or library name |
| 2 | Version | Text | Exact version number or range |
| 3 | Purpose | Text | Role in the system |

### Row-by-Row Content

**Row 1 (Header)**
- Component: "Component"
- Version: "Version"
- Purpose: "Purpose"

**Row 2: Python**
- Component: "Python"
- Version: "3.8+"
- Purpose: "Core programming language"
- **Why this version**: Python 3.8+ required for modern type hints and f-strings

**Row 3: sentence-transformers**
- Component: "sentence-transformers"
- Version: "2.2.2"
- Purpose: "Embedding model framework"
- **Why this version**: Stable release with all-MiniLM-L6-v2 support; newer versions compatible

**Row 4: pandas**
- Component: "pandas"
- Version: "2.1.4"
- Purpose: "Data manipulation and analysis"
- **Why this version**: Latest stable with CSV handling improvements

**Row 5: numpy**
- Component: "numpy"
- Version: "1.26.2"
- Purpose: "Numerical computations"
- **Why this version**: Required for array operations and cosine similarity

**Row 6: matplotlib**
- Component: "matplotlib"
- Version: "3.8.2"
- Purpose: "Visualization and plotting"
- **Why this version**: Latest with improved subplot handling

**Row 7: seaborn**
- Component: "seaborn"
- Version: "0.13.0"
- Purpose: "Statistical visualizations"
- **Why this version**: Enhanced heatmap and distribution plot features

**Row 8: scikit-learn**
- Component: "scikit-learn"
- Version: "1.3.2"
- Purpose: "Similarity metrics"
- **Why this version**: Provides cosine_similarity function

**Row 9: python-docx**
- Component: "python-docx"
- Version: "1.1.0"
- Purpose: "Document generation"
- **Why this version**: Latest stable for .docx creation

**Row 10: hashlib**
- Component: "hashlib"
- Version: "Standard library"
- Purpose: "SHA-256 hashing"
- **Why this version**: Built-in, no installation needed

**Row 11: json**
- Component: "json"
- Version: "Standard library"
- Purpose: "Data serialization"
- **Why this version**: Built-in, no installation needed

### Key Insights
- All versions tested and verified compatible
- Mix of cutting-edge (pandas 2.1.4) and stable (sentence-transformers 2.2.2)
- Two standard library modules (no external dependencies)

---

## Table 1.3: Model Configuration Specifications

**Location**: Section 1.3 - Model Configuration  
**Dimensions**: 8 rows × 2 columns  
**Style**: Light Grid Accent 1

### Purpose
Documents all parameters of the primary embedding model (all-MiniLM-L6-v2) used for semantic similarity computation.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Model parameter name |
| 2 | Value | Text | Parameter value or specification |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value: "Value"

**Row 2: Model Name**
- Parameter: "Model Name"
- Value: "sentence-transformers/all-MiniLM-L6-v2"
- **Significance**: HuggingFace identifier for automatic download

**Row 3: Architecture**
- Parameter: "Architecture"
- Value: "BERT-based transformer (6 layers)"
- **Significance**: Lightweight variant of BERT; 6 layers vs 12 in BERT-base

**Row 4: Embedding Dimension**
- Parameter: "Embedding Dimension"
- Value: "384"
- **Significance**: Each text encoded as 384-dimensional vector; balance of expressiveness and efficiency

**Row 5: Max Sequence Length**
- Parameter: "Max Sequence Length"
- Value: "256 tokens"
- **Significance**: Maximum input length; skill lists typically 20-50 tokens

**Row 6: Model Size**
- Parameter: "Model Size"
- Value: "22.7 MB"
- **Significance**: Compact size enables fast loading and deployment

**Row 7: Training Data**
- Parameter: "Training Data"
- Value: "MS MARCO, NLI datasets (1B+ pairs)"
- **Significance**: Pre-trained on massive semantic similarity datasets

**Row 8: Inference Speed**
- Parameter: "Inference Speed"
- Value: "~50ms per batch (10 sequences)"
- **Significance**: Fast enough for real-time recommendations

### Key Insights
- Optimized for semantic similarity tasks
- Small size (22.7 MB) vs high performance
- Pre-trained on 1B+ sentence pairs

---

# Section 2: Dataset Configuration Tables

## Table 2.1: Job Roles Dataset Specifications

**Location**: Section 2.1 - Job Roles Dataset  
**Dimensions**: 6 rows × 2 columns  
**Style**: Light Grid Accent 1

### Purpose
Specifies the structure and content of the job roles dataset, which defines the target positions for employee recommendations.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Attribute | Text | Dataset attribute name |
| 2 | Specification | Text | Detailed specification |

### Row-by-Row Content

**Row 1 (Header)**
- Attribute: "Attribute"
- Specification: "Specification"

**Row 2: Total Records**
- Attribute: "Total Records"
- Specification: "15 job roles"
- **Rationale**: Sufficient diversity for testing; manageable for analysis

**Row 3: Fields**
- Attribute: "Fields"
- Specification: "role_id, role_name, description, required_skills"
- **Rationale**: Minimal schema for role definition and skill matching

**Row 4: Skill Format**
- Attribute: "Skill Format"
- Specification: "Comma-separated text strings"
- **Rationale**: Simple, human-readable format; easy to parse

**Row 5: Domains Covered**
- Attribute: "Domains Covered"
- Specification: "Data Science, Engineering, Management, Analytics"
- **Rationale**: Represents common organizational functions

**Row 6: Skill Count Range**
- Attribute: "Skill Count Range"
- Specification: "5-12 skills per role"
- **Rationale**: Realistic range for professional positions

### Key Insights
- 15 roles provide good test coverage
- 4 domains represent typical organization
- 5-12 skills per role matches real job descriptions

---

## Table 2.2: Training Courses Dataset Specifications

**Location**: Section 2.2 - Training Courses Dataset  
**Dimensions**: 7 rows × 2 columns  
**Style**: Light Grid Accent 1

### Purpose
Defines the training courses dataset used for skill gap remediation recommendations.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Attribute | Text | Dataset attribute name |
| 2 | Specification | Text | Detailed specification |

### Row-by-Row Content

**Row 1 (Header)**
- Attribute: "Attribute"
- Specification: "Specification"

**Row 2: Total Records**
- Attribute: "Total Records"
- Specification: "25 training courses"
- **Rationale**: Diverse course catalog for gap remediation

**Row 3: Fields**
- Attribute: "Fields"
- Specification: "course_id, course_name, provider, skills_taught, duration, difficulty"
- **Rationale**: Complete course metadata for informed recommendations

**Row 4: Skill Format**
- Attribute: "Skill Format"
- Specification: "Comma-separated text strings"
- **Rationale**: Consistent with job roles format

**Row 5: Providers**
- Attribute: "Providers"
- Specification: "Coursera, edX, Udacity, LinkedIn Learning, Pluralsight"
- **Rationale**: Major MOOC platforms with enterprise offerings

**Row 6: Duration Range**
- Attribute: "Duration Range"
- Specification: "4-40 hours"
- **Rationale**: From short courses to comprehensive programs

**Row 7: Difficulty Levels**
- Attribute: "Difficulty Levels"
- Specification: "Beginner, Intermediate, Advanced"
- **Rationale**: Enables difficulty-appropriate recommendations

### Key Insights
- 25 courses cover wide skill range
- 5 major providers ensure availability
- Duration and difficulty enable personalized recommendations

---

## Table 2.3: Employees Dataset Specifications

**Location**: Section 2.3 - Employees Dataset  
**Dimensions**: 6 rows × 2 columns  
**Style**: Light Grid Accent 1

### Purpose
Describes the employee profiles dataset representing the workforce seeking role recommendations.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Attribute | Text | Dataset attribute name |
| 2 | Specification | Text | Detailed specification |

### Row-by-Row Content

**Row 1 (Header)**
- Attribute: "Attribute"
- Specification: "Specification"

**Row 2: Total Records**
- Attribute: "Total Records"
- Specification: "10 employee profiles"
- **Rationale**: Sufficient for statistical analysis (150 comparisons with 15 roles)

**Row 3: Fields**
- Attribute: "Fields"
- Specification: "employee_id, name, current_role, completed_courses, years_experience"
- **Rationale**: Captures current state and learning history

**Row 4: Course History**
- Attribute: "Course History"
- Specification: "Comma-separated course IDs"
- **Rationale**: Links to training courses dataset

**Row 5: Experience Range**
- Attribute: "Experience Range"
- Specification: "2-10 years"
- **Rationale**: Represents early-career to mid-career professionals

**Row 6: Roles Represented**
- Attribute: "Roles Represented"
- Specification: "Data Analyst, Engineer, Scientist, Manager"
- **Rationale**: Diverse starting points for mobility analysis

### Key Insights
- 10 employees × 15 roles = 150 comparisons
- 2-10 years experience represents growth-focused workforce
- Course history enables progression tracking

---

# Section 3: Experiment Configuration Tables

## Table 3.1: Experiment 1 - Similarity Threshold Analysis

**Location**: Section 3.1 - Experiment 1
**Dimensions**: 9 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Defines all parameters for the threshold analysis experiment, which determines the optimal similarity threshold for generating high-quality recommendations.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Experiment parameter name |
| 2 | Value/Range | Text | Parameter value or range tested |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value/Range: "Value/Range"

**Row 2: Thresholds Tested**
- Parameter: "Thresholds Tested"
- Value/Range: "50%, 60%, 70%, 75%, 80%, 85%, 90%"
- **Rationale**: Wide range from permissive (50%) to strict (90%)
- **Increment Logic**: 10% steps initially, then 5% steps in critical 70-90% range

**Row 3: Number of Thresholds**
- Parameter: "Number of Thresholds"
- Value/Range: "7"
- **Rationale**: Sufficient granularity without excessive computation

**Row 4: Employees Evaluated**
- Parameter: "Employees Evaluated"
- Value/Range: "10 (all employees)"
- **Rationale**: Complete dataset coverage

**Row 5: Roles Evaluated**
- Parameter: "Roles Evaluated"
- Value/Range: "15 (all roles)"
- **Rationale**: All possible recommendations considered

**Row 6: Total Comparisons**
- Parameter: "Total Comparisons"
- Value/Range: "150 (10 × 15)"
- **Rationale**: Exhaustive pairwise comparison

**Row 7: Metrics Collected**
- Parameter: "Metrics Collected"
- Value/Range: "Avg recommendations, qualified employees, avg top score"
- **Rationale**: Balances quantity (recommendations) and quality (top score)

**Row 8: Expected Outcome**
- Parameter: "Expected Outcome"
- Value/Range: "Identify threshold balancing quantity and quality"
- **Rationale**: Too low = noise; too high = missed opportunities

**Row 9: Hypothesis**
- Parameter: "Hypothesis"
- Value/Range: "70-75% threshold provides optimal balance"
- **Rationale**: Based on preliminary testing and literature review

### Key Insights
- 7 thresholds tested across 50-90% range
- 150 total comparisons per threshold (1,050 total evaluations)
- Hypothesis: 70-75% optimal (validated in results)

### Experimental Design Rationale
- **Why 50% minimum**: Below 50% similarity indicates poor match
- **Why 90% maximum**: 90%+ similarity rare in cross-role comparisons
- **Why 5% increments in 70-90%**: Critical decision zone requires finer granularity

---

## Table 3.2: Experiment 2 - Skill Gap Progression

**Location**: Section 3.2 - Experiment 2
**Dimensions**: 10 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Specifies parameters for tracking an employee's skill development journey through targeted training courses.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Experiment parameter name |
| 2 | Value/Range | Text | Parameter value or specification |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value/Range: "Value/Range"

**Row 2: Test Subject**
- Parameter: "Test Subject"
- Value/Range: "Employee EMP001 (Data Analyst)"
- **Rationale**: Representative employee with clear upskilling path

**Row 3: Target Role**
- Parameter: "Target Role"
- Value/Range: "Data Strategy Officer"
- **Rationale**: Logical career progression requiring new skills

**Row 4: Progression Stages**
- Parameter: "Progression Stages"
- Value/Range: "4 (Initial, +1 course, +2 courses, +3 courses)"
- **Rationale**: Tracks incremental improvement

**Row 5: Courses Added**
- Parameter: "Courses Added"
- Value/Range: "Data Governance, Leadership, Business Intelligence"
- **Rationale**: Courses specifically address identified skill gaps

**Row 6: Metrics Tracked**
- Parameter: "Metrics Tracked"
- Value/Range: "Similarity score, skill gaps, courses completed"
- **Rationale**: Quantifies improvement and gap closure

**Row 7: Measurement Interval**
- Parameter: "Measurement Interval"
- Value/Range: "After each course completion"
- **Rationale**: Captures incremental progress

**Row 8: Expected Improvement**
- Parameter: "Expected Improvement"
- Value/Range: "+10-15% similarity score"
- **Rationale**: Based on skill overlap analysis

**Row 9: Expected Gap Reduction**
- Parameter: "Expected Gap Reduction"
- Value/Range: "5 gaps → 1-2 gaps"
- **Rationale**: Courses target 3-4 critical gaps

**Row 10: Hypothesis**
- Parameter: "Hypothesis"
- Value/Range: "Targeted courses yield measurable improvements"
- **Rationale**: Validates skill-based recommendation approach

### Key Insights
- Single employee deep-dive (case study approach)
- 4 measurement points track progression
- Expected 10-15% improvement validates training ROI

### Experimental Design Rationale
- **Why EMP001**: Has clear skill gaps and logical progression path
- **Why 3 courses**: Sufficient to demonstrate trend without overfitting
- **Why these courses**: Directly address top 3 skill gaps

---

## Table 3.3: Experiment 3 - Blockchain Performance

**Location**: Section 3.3 - Experiment 3
**Dimensions**: 11 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Defines parameters for evaluating blockchain credential system performance and scalability.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Experiment parameter name |
| 2 | Value/Range | Text | Parameter value or range |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value/Range: "Value/Range"

**Row 2: Operations Tested**
- Parameter: "Operations Tested"
- Value/Range: "Issue credentials, Verify credentials"
- **Rationale**: Two core blockchain operations

**Row 3: Credential Counts**
- Parameter: "Credential Counts"
- Value/Range: "10, 50, 100, 500"
- **Rationale**: Logarithmic scale from small to enterprise

**Row 4: Number of Scenarios**
- Parameter: "Number of Scenarios"
- Value/Range: "8 (4 counts × 2 operations)"
- **Rationale**: Complete coverage of operations × scales

**Row 5: Hash Algorithm**
- Parameter: "Hash Algorithm"
- Value/Range: "SHA-256"
- **Rationale**: Industry standard, cryptographically secure

**Row 6: Ledger Format**
- Parameter: "Ledger Format"
- Value/Range: "JSON"
- **Rationale**: Human-readable, widely supported

**Row 7: Metrics Collected**
- Parameter: "Metrics Collected"
- Value/Range: "Execution time (ms), throughput (ops/sec)"
- **Rationale**: Standard performance metrics

**Row 8: Timing Method**
- Parameter: "Timing Method"
- Value/Range: "Python time.time() with microsecond precision"
- **Rationale**: Sufficient precision for millisecond measurements

**Row 9: Repetitions**
- Parameter: "Repetitions"
- Value/Range: "1 per scenario (deterministic operations)"
- **Rationale**: Hashing is deterministic; no variance

**Row 10: Expected Throughput**
- Parameter: "Expected Throughput"
- Value/Range: ">1000 ops/sec for verification"
- **Rationale**: Enterprise-ready performance target

**Row 11: Hypothesis**
- Parameter: "Hypothesis"
- Value/Range: "Linear O(n) scalability with credential count"
- **Rationale**: Each credential processed independently

### Key Insights
- 8 scenarios test 2 operations at 4 scales
- SHA-256 provides cryptographic security
- Expected >1000 ops/sec demonstrates enterprise readiness

### Experimental Design Rationale
- **Why these counts**: 10 (small org), 50 (department), 100 (division), 500 (enterprise)
- **Why SHA-256**: Balance of security and performance
- **Why JSON**: Interoperability and auditability

---

## Table 3.4: Experiment 4 - Embedding Model Comparison

**Location**: Section 3.4 - Experiment 4
**Dimensions**: 10 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Specifies parameters for comparing three sentence-transformer models to validate model selection.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Experiment parameter name |
| 2 | Value/Range | Text | Parameter value or specification |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value/Range: "Value/Range"

**Row 2: Models Tested**
- Parameter: "Models Tested"
- Value/Range: "all-MiniLM-L6-v2, all-MiniLM-L12-v2, paraphrase-MiniLM-L6-v2"
- **Rationale**: Compare size (L6 vs L12) and training (all vs paraphrase)

**Row 3: Number of Models**
- Parameter: "Number of Models"
- Value/Range: "3"
- **Rationale**: Sufficient for comparison without excessive testing

**Row 4: Test Dataset**
- Parameter: "Test Dataset"
- Value/Range: "Same 10 employees × 15 roles"
- **Rationale**: Consistent comparison across models

**Row 5: Metrics Collected**
- Parameter: "Metrics Collected"
- Value/Range: "Avg similarity, std dev, inference time, model size"
- **Rationale**: Balances accuracy, speed, and resource usage

**Row 6: Inference Timing**
- Parameter: "Inference Timing"
- Value/Range: "Average over all 150 comparisons"
- **Rationale**: Amortizes model loading overhead

**Row 7: Model Sizes**
- Parameter: "Model Sizes"
- Value/Range: "L6: 22.7 MB, L12: 33.4 MB, Paraphrase: 22.7 MB"
- **Rationale**: L12 is 47% larger than L6

**Row 8: Expected Winner**
- Parameter: "Expected Winner"
- Value/Range: "all-MiniLM-L6-v2 (speed/accuracy balance)"
- **Rationale**: Hypothesis based on literature

**Row 9: Accuracy Tolerance**
- Parameter: "Accuracy Tolerance"
- Value/Range: "±2% similarity score acceptable"
- **Rationale**: Small differences not meaningful for recommendations

**Row 10: Hypothesis**
- Parameter: "Hypothesis"
- Value/Range: "Smaller models sufficient for skill matching task"
- **Rationale**: Skill matching less complex than general NLU

### Key Insights
- 3 models compared on identical dataset
- L6 vs L12 tests size/accuracy tradeoff
- ±2% tolerance recognizes practical equivalence

### Experimental Design Rationale
- **Why these models**: Same family (MiniLM) for fair comparison
- **Why not larger models**: Focus on deployment efficiency
- **Why ±2% tolerance**: Below human perception threshold

---

## Table 3.5: Experiment 5 - Scalability Analysis

**Location**: Section 3.5 - Experiment 5
**Dimensions**: 10 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Defines parameters for evaluating system scalability across different organization sizes.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Experiment parameter name |
| 2 | Value/Range | Text | Parameter value or range |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value/Range: "Value/Range"

**Row 2: Employee Counts**
- Parameter: "Employee Counts"
- Value/Range: "10, 50, 100"
- **Rationale**: Small, medium, large organization sizes

**Row 3: Role Counts**
- Parameter: "Role Counts"
- Value/Range: "15, 50, 100"
- **Rationale**: Limited, moderate, extensive role catalogs

**Row 4: Scenarios Tested**
- Parameter: "Scenarios Tested"
- Value/Range: "6 (combinations of employee/role counts)"
- **Rationale**: Not all combinations (would be 9); selected representative scenarios

**Row 5: Total Comparisons Range**
- Parameter: "Total Comparisons Range"
- Value/Range: "150 to 10,000"
- **Rationale**: 67× scale increase tests linearity

**Row 6: Metrics Collected**
- Parameter: "Metrics Collected"
- Value/Range: "Total time, time per comparison, memory usage"
- **Rationale**: Comprehensive performance profile

**Row 7: Complexity Analysis**
- Parameter: "Complexity Analysis"
- Value/Range: "Linear regression (R² correlation)"
- **Rationale**: Quantifies linearity of scaling

**Row 8: Expected Complexity**
- Parameter: "Expected Complexity"
- Value/Range: "O(n×m) where n=employees, m=roles"
- **Rationale**: Each employee compared to each role

**Row 9: Expected R²**
- Parameter: "Expected R²"
- Value/Range: ">0.95 (strong linear correlation)"
- **Rationale**: R²>0.95 indicates excellent linear fit

**Row 10: Hypothesis**
- Parameter: "Hypothesis"
- Value/Range: "Linear scalability suitable for enterprise deployment"
- **Rationale**: Linear scaling predictable and manageable

### Key Insights
- 6 scenarios span 150 to 10,000 comparisons
- R² correlation quantifies linearity
- O(n×m) complexity expected and validated

### Experimental Design Rationale
- **Why these sizes**: Represent small (10), medium (50), large (100) organizations
- **Why 6 scenarios**: Balance coverage and computation time
- **Why R²>0.95**: Industry standard for "excellent" linear fit

---

## Table 3.6: Experiment 6 - Score Distribution Analysis

**Location**: Section 3.6 - Experiment 6
**Dimensions**: 11 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Specifies parameters for statistical analysis of similarity score distribution.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Experiment parameter name |
| 2 | Value/Range | Text | Parameter value or specification |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value/Range: "Value/Range"

**Row 2: Sample Size**
- Parameter: "Sample Size"
- Value/Range: "150 (10 employees × 15 roles)"
- **Rationale**: Complete dataset; sufficient for statistical analysis

**Row 3: Score Range**
- Parameter: "Score Range"
- Value/Range: "0-100%"
- **Rationale**: Normalized percentage scale

**Row 4: Statistics Computed**
- Parameter: "Statistics Computed"
- Value/Range: "Mean, median, std dev, min, max, quartiles"
- **Rationale**: Comprehensive descriptive statistics

**Row 5: Distribution Tests**
- Parameter: "Distribution Tests"
- Value/Range: "Histogram, box plot, Q-Q plot"
- **Rationale**: Visual and quantitative normality assessment

**Row 6: Normality Assessment**
- Parameter: "Normality Assessment"
- Value/Range: "Visual Q-Q plot analysis"
- **Rationale**: Q-Q plot reveals distribution shape

**Row 7: Per-Employee Analysis**
- Parameter: "Per-Employee Analysis"
- Value/Range: "Mean, max, min scores for each employee"
- **Rationale**: Individual opportunity assessment

**Row 8: Threshold Validation**
- Parameter: "Threshold Validation"
- Value/Range: "Percentage of scores exceeding 70%"
- **Rationale**: Validates threshold from Experiment 1

**Row 9: Expected Mean**
- Parameter: "Expected Mean"
- Value/Range: "60-70%"
- **Rationale**: Moderate similarity indicates meaningful differentiation

**Row 10: Expected Std Dev**
- Parameter: "Expected Std Dev"
- Value/Range: "10-20%"
- **Rationale**: Sufficient spread to distinguish good/poor matches

**Row 11: Hypothesis**
- Parameter: "Hypothesis"
- Value/Range: "Right-skewed distribution with meaningful differentiation"
- **Rationale**: Most pairs moderate; some excellent matches

### Key Insights
- 150 samples sufficient for robust statistics
- Multiple visualization methods (histogram, box, Q-Q)
- Expected right-skewed distribution (validated)

### Experimental Design Rationale
- **Why 150 samples**: n>30 for CLT; n=150 provides robust estimates
- **Why Q-Q plot**: Best visual test for normality
- **Why per-employee analysis**: Ensures every employee has opportunities

---

# Section 4: Algorithm Configuration Tables

## Table 4.1: Skill Matching Algorithm Configuration

**Location**: Section 4.1 - Skill Matching Algorithm
**Dimensions**: 11 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Documents all parameters and settings for the core skill matching algorithm that computes employee-role similarity.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Algorithm parameter name |
| 2 | Configuration | Text | Parameter setting or value |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Configuration: "Configuration"

**Row 2: Similarity Metric**
- Parameter: "Similarity Metric"
- Configuration: "Cosine similarity"
- **Rationale**: Standard for high-dimensional vector comparison; range [0,1]
- **Formula**: cos(θ) = (A·B) / (||A|| ||B||)

**Row 3: Embedding Method**
- Parameter: "Embedding Method"
- Configuration: "Sentence-BERT (all-MiniLM-L6-v2)"
- **Rationale**: State-of-art sentence embeddings; pre-trained on semantic similarity

**Row 4: Text Preprocessing**
- Parameter: "Text Preprocessing"
- Configuration: "Lowercase, whitespace normalization"
- **Rationale**: Minimal preprocessing; model handles most normalization

**Row 5: Skill Aggregation**
- Parameter: "Skill Aggregation"
- Configuration: "Concatenate all skills with space separator"
- **Rationale**: Treats skill set as single semantic unit
- **Example**: "Python, SQL, Machine Learning" → "python sql machine learning"

**Row 6: Normalization**
- Parameter: "Normalization"
- Configuration: "L2 normalization (automatic in model)"
- **Rationale**: Ensures unit vectors for cosine similarity

**Row 7: Batch Processing**
- Parameter: "Batch Processing"
- Configuration: "Enabled (batch size: 32)"
- **Rationale**: Efficient GPU/CPU utilization; 32 is model default

**Row 8: Score Range**
- Parameter: "Score Range"
- Configuration: "0.0 to 1.0 (converted to 0-100%)"
- **Rationale**: Percentage more intuitive for stakeholders

**Row 9: Threshold Application**
- Parameter: "Threshold Application"
- Configuration: "Post-computation filtering"
- **Rationale**: Compute all scores, then filter; enables threshold experimentation

**Row 10: Ranking Method**
- Parameter: "Ranking Method"
- Configuration: "Descending by similarity score"
- **Rationale**: Highest similarity = best match

**Row 11: Top-K Recommendations**
- Parameter: "Top-K Recommendations"
- Configuration: "K=5 (configurable)"
- **Rationale**: Manageable number for review; configurable per use case

### Key Insights
- Cosine similarity on 384-dimensional embeddings
- Batch size 32 optimizes throughput
- Post-computation filtering enables experimentation

### Algorithm Flow
1. Concatenate skills → text string
2. Embed text → 384-dim vector
3. Compute cosine similarity → score [0,1]
4. Convert to percentage → score [0,100]
5. Filter by threshold → qualified recommendations
6. Rank descending → top-K results

---

## Table 4.2: Skill Gap Analysis Algorithm Configuration

**Location**: Section 4.2 - Skill Gap Analysis Algorithm
**Dimensions**: 8 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Specifies the algorithm for identifying skill gaps and recommending remediation courses.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Algorithm parameter name |
| 2 | Configuration | Text | Parameter setting or method |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Configuration: "Configuration"

**Row 2: Gap Detection Method**
- Parameter: "Gap Detection Method"
- Configuration: "Set difference (required - possessed)"
- **Rationale**: Mathematical set operation; clear gap definition
- **Formula**: Gaps = RequiredSkills \ PossessedSkills

**Row 3: Skill Extraction**
- Parameter: "Skill Extraction"
- Configuration: "Parse comma-separated skill lists"
- **Rationale**: Simple, reliable parsing; handles variable skill counts

**Row 4: Matching Strategy**
- Parameter: "Matching Strategy"
- Configuration: "Exact string match (case-insensitive)"
- **Rationale**: Avoids false positives from fuzzy matching
- **Example**: "Python" matches "python" but not "Python Programming"

**Row 5: Gap Prioritization**
- Parameter: "Gap Prioritization"
- Configuration: "By frequency in high-similarity roles"
- **Rationale**: Focus on skills valuable across multiple opportunities

**Row 6: Course Recommendation**
- Parameter: "Course Recommendation"
- Configuration: "Match gap skills to course skills_taught"
- **Rationale**: Direct skill-to-course mapping

**Row 7: Recommendation Limit**
- Parameter: "Recommendation Limit"
- Configuration: "Top 3 courses per gap skill"
- **Rationale**: Prevents overwhelming users; focuses on best options

**Row 8: Course Ranking**
- Parameter: "Course Ranking"
- Configuration: "By skill coverage and difficulty match"
- **Rationale**: Prioritizes comprehensive, appropriate courses

### Key Insights
- Set difference provides precise gap identification
- Case-insensitive matching handles formatting variations
- Top 3 courses per gap balances choice and focus

### Algorithm Flow
1. Extract required skills from target role
2. Extract possessed skills from employee profile
3. Compute set difference → skill gaps
4. For each gap skill:
   - Find courses teaching that skill
   - Rank by coverage and difficulty
   - Return top 3 courses
5. Aggregate recommendations

---

## Table 4.3: Blockchain Credential Algorithm Configuration

**Location**: Section 4.3 - Blockchain Credential Algorithm
**Dimensions**: 10 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Documents the blockchain-inspired credential verification algorithm parameters.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Algorithm parameter name |
| 2 | Configuration | Text | Parameter setting or specification |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Configuration: "Configuration"

**Row 2: Hash Function**
- Parameter: "Hash Function"
- Configuration: "SHA-256"
- **Rationale**: Cryptographically secure; industry standard
- **Properties**: Deterministic, collision-resistant, one-way

**Row 3: Hash Input**
- Parameter: "Hash Input"
- Configuration: "JSON string of credential data"
- **Rationale**: Structured, human-readable, includes all credential fields
- **Fields**: credential_id, employee_id, course_id, timestamp, previous_hash

**Row 4: Credential ID Format**
- Parameter: "Credential ID Format"
- Configuration: "CRED_XXXX (sequential)"
- **Rationale**: Human-readable, sortable, unique
- **Example**: CRED_0001, CRED_0002, ...

**Row 5: Timestamp Format**
- Parameter: "Timestamp Format"
- Configuration: "ISO 8601 (YYYY-MM-DD HH:MM:SS)"
- **Rationale**: International standard, sortable, unambiguous
- **Example**: 2026-01-12 14:30:45

**Row 6: Previous Hash**
- Parameter: "Previous Hash"
- Configuration: "SHA-256 hash of previous credential"
- **Rationale**: Creates immutable chain; tampering detection

**Row 7: Genesis Block**
- Parameter: "Genesis Block"
- Configuration: "Hash: 0000000000000000..."
- **Rationale**: First block has no predecessor; uses zero hash

**Row 8: Ledger Storage**
- Parameter: "Ledger Storage"
- Configuration: "In-memory list (production: database)"
- **Rationale**: Prototype uses memory; production requires persistence

**Row 9: Verification Method**
- Parameter: "Verification Method"
- Configuration: "Recompute hash and compare"
- **Rationale**: Deterministic verification; detects any tampering
- **Process**: Hash(credential_data) == stored_hash?

**Row 10: Immutability**
- Parameter: "Immutability"
- Configuration: "Append-only ledger structure"
- **Rationale**: No updates or deletes; only additions

### Key Insights
- SHA-256 provides cryptographic security
- Chain structure enables tamper detection
- Append-only ensures immutability

### Algorithm Flow - Issue Credential
1. Generate credential_id (sequential)
2. Capture timestamp (ISO 8601)
3. Get previous_hash from last credential
4. Create JSON with all fields
5. Compute SHA-256 hash
6. Append to ledger

### Algorithm Flow - Verify Credential
1. Retrieve credential from ledger
2. Extract credential data
3. Recompute SHA-256 hash
4. Compare with stored hash
5. Return match status

---

# Section 5: Evaluation Metrics Tables

## Table 5.1: Recommendation Quality Metrics

**Location**: Section 5.1 - Recommendation Quality Metrics
**Dimensions**: 7 rows × 3 columns
**Style**: Light Grid Accent 1

### Purpose
Defines metrics for evaluating the quality and relevance of role recommendations.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Metric | Text | Metric name |
| 2 | Formula/Method | Text | Calculation method |
| 3 | Target Value | Text | Expected or desired value |

### Row-by-Row Content

**Row 1 (Header)**
- Metric: "Metric"
- Formula/Method: "Formula/Method"
- Target Value: "Target Value"

**Row 2: Average Similarity Score**
- Metric: "Average Similarity Score"
- Formula/Method: "Mean of all employee-role scores"
- Target Value: "60-70%"
- **Rationale**: Too low = poor matches; too high = insufficient differentiation
- **Formula**: Σ(scores) / n where n=150

**Row 3: Top Match Score**
- Metric: "Top Match Score"
- Formula/Method: "Highest score per employee"
- Target Value: ">80%"
- **Rationale**: Every employee should have at least one excellent opportunity
- **Formula**: max(scores) for each employee

**Row 4: Recommendations per Employee**
- Metric: "Recommendations per Employee"
- Formula/Method: "Count of scores above threshold"
- Target Value: "3-5"
- **Rationale**: Enough choice without overwhelming; manageable for review
- **Formula**: count(score > threshold) per employee

**Row 5: Score Standard Deviation**
- Metric: "Score Standard Deviation"
- Formula/Method: "Std dev of all scores"
- Target Value: "10-20%"
- **Rationale**: Sufficient spread to distinguish good/poor matches
- **Formula**: √(Σ(score - mean)² / n)

**Row 6: Coverage**
- Metric: "Coverage"
- Formula/Method: "% of employees with ≥1 recommendation"
- Target Value: "100%"
- **Rationale**: System must serve all employees
- **Formula**: (employees with recommendations / total employees) × 100%

**Row 7: Precision@K**
- Metric: "Precision@K"
- Formula/Method: "Relevant recommendations in top K"
- Target Value: ">70%"
- **Rationale**: Most top recommendations should be truly relevant
- **Formula**: (relevant in top K / K) × 100%

### Key Insights
- 6 metrics provide comprehensive quality assessment
- Targets balance quantity (3-5 recs) and quality (>80% top score)
- 100% coverage ensures equity

### Metric Interdependencies
- Lower threshold → more recommendations → lower avg score
- Higher threshold → fewer recommendations → higher avg score
- Optimal balance at 70% threshold (from Experiment 1)

---

## Table 5.2: Performance Metrics

**Location**: Section 5.2 - Performance Metrics
**Dimensions**: 7 rows × 3 columns
**Style**: Light Grid Accent 1

### Purpose
Specifies metrics for evaluating system computational performance and efficiency.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Metric | Text | Metric name |
| 2 | Measurement Method | Text | How metric is measured |
| 3 | Target Value | Text | Performance target |

### Row-by-Row Content

**Row 1 (Header)**
- Metric: "Metric"
- Measurement Method: "Measurement Method"
- Target Value: "Target Value"

**Row 2: Inference Time**
- Metric: "Inference Time"
- Measurement Method: "time.time() before/after embedding"
- Target Value: "<100ms per batch"
- **Rationale**: Real-time feel for users; batch of 32 sequences
- **Measurement**: t_end - t_start for model.encode()

**Row 3: Comparison Time**
- Metric: "Comparison Time"
- Measurement Method: "Time for cosine similarity computation"
- Target Value: "<1ms per pair"
- **Rationale**: Negligible compared to embedding time
- **Measurement**: t_end - t_start for cosine_similarity()

**Row 4: Total Processing Time**
- Metric: "Total Processing Time"
- Measurement Method: "End-to-end for all comparisons"
- Target Value: "<5s for 150 pairs"
- **Rationale**: Acceptable wait time for batch processing
- **Measurement**: Full pipeline from data load to results

**Row 5: Throughput**
- Metric: "Throughput"
- Measurement Method: "Operations per second"
- Target Value: ">1000 ops/sec"
- **Rationale**: Enterprise-scale performance
- **Formula**: operations / total_time

**Row 6: Memory Usage**
- Metric: "Memory Usage"
- Measurement Method: "Peak RAM during processing"
- Target Value: "<500 MB"
- **Rationale**: Modest hardware requirements
- **Measurement**: Peak memory from system monitor

**Row 7: Model Load Time**
- Metric: "Model Load Time"
- Measurement Method: "Time to load embedding model"
- Target Value: "<5 seconds"
- **Rationale**: One-time cost; amortized over many operations
- **Measurement**: t_end - t_start for SentenceTransformer()

### Key Insights
- Inference time dominates (>90% of total time)
- Throughput >1000 ops/sec enables real-time applications
- Memory <500 MB allows deployment on modest hardware

### Performance Bottlenecks
1. **Model loading** (5s) - one-time cost
2. **Embedding generation** (50-100ms/batch) - main bottleneck
3. **Similarity computation** (<1ms) - negligible

---

## Table 5.3: Scalability Metrics

**Location**: Section 5.3 - Scalability Metrics
**Dimensions**: 6 rows × 3 columns
**Style**: Light Grid Accent 1

### Purpose
Defines metrics for assessing system scalability to larger datasets and organizations.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Metric | Text | Metric name |
| 2 | Measurement Method | Text | How metric is measured |
| 3 | Target Value | Text | Scalability target |

### Row-by-Row Content

**Row 1 (Header)**
- Metric: "Metric"
- Measurement Method: "Measurement Method"
- Target Value: "Target Value"

**Row 2: Complexity Class**
- Metric: "Complexity Class"
- Measurement Method: "Big-O analysis of runtime"
- Target Value: "O(n×m)"
- **Rationale**: Linear in both dimensions; predictable scaling
- **Analysis**: n employees × m roles = n×m comparisons

**Row 3: Linear Correlation (R²)**
- Metric: "Linear Correlation (R²)"
- Measurement Method: "Regression of time vs comparisons"
- Target Value: ">0.95"
- **Rationale**: R²>0.95 indicates excellent linear fit
- **Formula**: 1 - (SS_res / SS_tot)

**Row 4: Per-Comparison Time**
- Metric: "Per-Comparison Time"
- Measurement Method: "Total time / number of comparisons"
- Target Value: "50-100 μs"
- **Rationale**: Stable per-comparison time indicates good scaling
- **Formula**: total_time / (n × m)

**Row 5: Scalability Factor**
- Metric: "Scalability Factor"
- Measurement Method: "Time ratio for 10× data increase"
- Target Value: "<10×"
- **Rationale**: Linear scaling means 10× data → ~10× time
- **Formula**: time(10×data) / time(1×data)

**Row 6: Extrapolated Performance**
- Metric: "Extrapolated Performance"
- Measurement Method: "Projected time for 1000×100"
- Target Value: "<10 seconds"
- **Rationale**: Enterprise scale (1000 employees, 100 roles) must be practical
- **Formula**: (1000 × 100) × per_comparison_time

### Key Insights
- O(n×m) complexity is optimal for exhaustive comparison
- R²>0.95 validates linear scaling assumption
- Extrapolation shows enterprise readiness

### Scalability Validation
- **Small** (10×15=150): ~1.5s
- **Medium** (50×50=2500): ~25s
- **Large** (100×100=10000): ~100s
- **Enterprise** (1000×100=100000): ~1000s ≈ 17 minutes

---

# Section 6: Visualization Configuration Tables

## Table 6.1: General Plotting Parameters

**Location**: Section 6.1 - General Plotting Parameters
**Dimensions**: 10 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Standardizes visualization parameters across all plots for consistency and publication quality.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Plotting parameter name |
| 2 | Value | Text | Parameter setting |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value: "Value"

**Row 2: Figure Size**
- Parameter: "Figure Size"
- Value: "6 inches width (varies by plot type)"
- **Rationale**: Standard column width for journals; height varies by content

**Row 3: DPI**
- Parameter: "DPI"
- Value: "300 (publication quality)"
- **Rationale**: 300 DPI is standard for print publications

**Row 4: Font Family**
- Parameter: "Font Family"
- Value: "DejaVu Sans"
- **Rationale**: Clean, professional, widely available

**Row 5: Font Size**
- Parameter: "Font Size"
- Value: "10pt (labels), 12pt (titles)"
- **Rationale**: Readable at document scale; hierarchical sizing

**Row 6: Color Palette**
- Parameter: "Color Palette"
- Value: "Seaborn default (colorblind-friendly)"
- **Rationale**: Accessible to colorblind readers (~8% of males)

**Row 7: Grid Style**
- Parameter: "Grid Style"
- Value: "Light gray, alpha=0.3"
- **Rationale**: Aids reading without visual clutter

**Row 8: Legend Position**
- Parameter: "Legend Position"
- Value: "Best (automatic) or upper right"
- **Rationale**: Matplotlib auto-positions to avoid data overlap

**Row 9: File Format**
- Parameter: "File Format"
- Value: "PNG with tight layout"
- **Rationale**: PNG for raster graphics; tight_layout removes whitespace

**Row 10: Background**
- Parameter: "Background"
- Value: "White"
- **Rationale**: Standard for publications; high contrast

### Key Insights
- 300 DPI ensures print quality
- Colorblind-friendly palette ensures accessibility
- Consistent styling across all 8 figures

---

## Table 6.2a: Heatmap Configuration

**Location**: Section 6.2 - Plot-Specific Configurations (Heatmap)
**Dimensions**: 6 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Specifies parameters unique to heatmap visualizations (similarity matrix, scalability heatmap).

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Heatmap parameter name |
| 2 | Value | Text | Parameter setting |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value: "Value"

**Row 2: Colormap**
- Parameter: "Colormap"
- Value: "YlOrRd (yellow-orange-red)"
- **Rationale**: Sequential colormap; intuitive (yellow=low, red=high)
- **Accessibility**: Distinguishable in grayscale

**Row 3: Value Range**
- Parameter: "Value Range"
- Value: "0-100%"
- **Rationale**: Normalized percentage scale; consistent across plots

**Row 4: Annotations**
- Parameter: "Annotations"
- Value: "Enabled (score values in cells)"
- **Rationale**: Precise values supplement color encoding

**Row 5: Cell Size**
- Parameter: "Cell Size"
- Value: "Auto-scaled to fit"
- **Rationale**: Adapts to matrix dimensions (10×15, 6×6, etc.)

**Row 6: Color Bar**
- Parameter: "Color Bar"
- Value: "Enabled with % labels"
- **Rationale**: Legend for color-to-value mapping

### Key Insights
- YlOrRd colormap intuitive and accessible
- Annotations provide exact values
- Auto-scaling handles different matrix sizes

---

## Table 6.2b: Bar Chart Configuration

**Location**: Section 6.2 - Plot-Specific Configurations (Bar Chart)
**Dimensions**: 5 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Defines parameters for bar chart visualizations (top recommendations, threshold analysis).

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Parameter | Text | Bar chart parameter name |
| 2 | Value | Text | Parameter setting |

### Row-by-Row Content

**Row 1 (Header)**
- Parameter: "Parameter"
- Value: "Value"

**Row 2: Orientation**
- Parameter: "Orientation"
- Value: "Horizontal"
- **Rationale**: Better for long labels (employee names, role names)

**Row 3: Bar Color**
- Parameter: "Bar Color"
- Value: "Steelblue (#4682B4)"
- **Rationale**: Professional, neutral, high contrast

**Row 4: Value Labels**
- Parameter: "Value Labels"
- Value: "Enabled (end of bars)"
- **Rationale**: Precise values without reading axis

**Row 5: Sorting**
- Parameter: "Sorting"
- Value: "By employee ID or score (descending)"
- **Rationale**: Logical ordering for interpretation

### Key Insights
- Horizontal orientation improves label readability
- Value labels eliminate axis reading
- Sorting by score highlights top performers

---

# Section 7: Reproducibility Tables

## Table 7.1: Random Seed Configuration

**Location**: Section 7.4 - Random Seed Configuration
**Dimensions**: 5 rows × 2 columns
**Style**: Light Grid Accent 1

### Purpose
Documents random seed settings to ensure deterministic, reproducible results.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Component | Text | System component name |
| 2 | Seed Value | Text | Random seed setting |

### Row-by-Row Content

**Row 1 (Header)**
- Component: "Component"
- Seed Value: "Seed Value"

**Row 2: NumPy Random**
- Component: "NumPy Random"
- Seed Value: "42"
- **Rationale**: Standard seed value; ensures reproducible array operations
- **Usage**: np.random.seed(42)

**Row 3: Python Random**
- Component: "Python Random"
- Seed Value: "42"
- **Rationale**: Ensures reproducible random.choice(), random.shuffle()
- **Usage**: random.seed(42)

**Row 4: Model Initialization**
- Component: "Model Initialization"
- Seed Value: "Deterministic (no randomness)"
- **Rationale**: Pre-trained model; no random initialization

**Row 5: Data Shuffling**
- Component: "Data Shuffling"
- Seed Value: "Disabled (preserve order)"
- **Rationale**: Maintains original data order for consistency

### Key Insights
- Seed 42 is convention (Hitchhiker's Guide reference)
- Model is deterministic (no training randomness)
- Data order preserved for reproducibility

### Reproducibility Guarantee
With these settings:
- Same input → same embeddings
- Same embeddings → same similarity scores
- Same scores → same recommendations
- **Result**: Bit-for-bit reproducibility

---

# Section 8: Validation Criteria Tables

## Table 8.1: Data Validation Criteria

**Location**: Section 8.1 - Data Validation
**Dimensions**: 7 rows × 3 columns
**Style**: Light Grid Accent 1

### Purpose
Provides checklist for validating input data quality and format.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Check | Text | Validation check name |
| 2 | Criterion | Text | What to validate |
| 3 | Pass/Fail | Text | Success criterion |

### Row-by-Row Content

**Row 1 (Header)**
- Check: "Check"
- Criterion: "Criterion"
- Pass/Fail: "Pass/Fail"

**Row 2: Record Counts**
- Check: "Record Counts"
- Criterion: "Roles=15, Courses=25, Employees=10"
- Pass/Fail: "Must match"
- **Validation**: len(df) == expected_count

**Row 3: Missing Values**
- Check: "Missing Values"
- Criterion: "No null/empty required fields"
- Pass/Fail: "Zero nulls"
- **Validation**: df.isnull().sum() == 0

**Row 4: Skill Format**
- Check: "Skill Format"
- Criterion: "Comma-separated strings"
- Pass/Fail: "Valid format"
- **Validation**: All skill fields contain commas or single skill

**Row 5: ID Uniqueness**
- Check: "ID Uniqueness"
- Criterion: "All IDs unique within dataset"
- Pass/Fail: "100% unique"
- **Validation**: df['id'].nunique() == len(df)

**Row 6: Data Types**
- Check: "Data Types"
- Criterion: "Correct types for all fields"
- Pass/Fail: "All valid"
- **Validation**: df.dtypes match schema

**Row 7: Encoding**
- Check: "Encoding"
- Criterion: "UTF-8 encoding"
- Pass/Fail: "UTF-8"
- **Validation**: File opens without encoding errors

### Key Insights
- 6 validation checks ensure data quality
- All checks must pass before experiments
- Automated validation prevents errors

---

## Table 8.2: Model Validation Criteria

**Location**: Section 8.2 - Model Validation
**Dimensions**: 6 rows × 3 columns
**Style**: Light Grid Accent 1

### Purpose
Checklist for validating embedding model functionality and performance.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Check | Text | Validation check name |
| 2 | Criterion | Text | What to validate |
| 3 | Pass/Fail | Text | Success criterion |

### Row-by-Row Content

**Row 1 (Header)**
- Check: "Check"
- Criterion: "Criterion"
- Pass/Fail: "Pass/Fail"

**Row 2: Model Loading**
- Check: "Model Loading"
- Criterion: "Successfully loads without errors"
- Pass/Fail: "No errors"
- **Validation**: SentenceTransformer() completes successfully

**Row 3: Embedding Dimension**
- Check: "Embedding Dimension"
- Criterion: "Output dimension = 384"
- Pass/Fail: "384"
- **Validation**: model.encode("test").shape[0] == 384

**Row 4: Score Range**
- Check: "Score Range"
- Criterion: "All scores in [0, 1]"
- Pass/Fail: "0 ≤ score ≤ 1"
- **Validation**: (scores >= 0).all() and (scores <= 1).all()

**Row 5: Determinism**
- Check: "Determinism"
- Criterion: "Same input → same output"
- Pass/Fail: "100% match"
- **Validation**: encode(text) == encode(text) for all texts

**Row 6: Performance**
- Check: "Performance"
- Criterion: "Inference time < 100ms/batch"
- Pass/Fail: "<100ms"
- **Validation**: time(encode(batch)) < 0.1 seconds

### Key Insights
- 5 validation checks ensure model correctness
- Determinism critical for reproducibility
- Performance check ensures efficiency

---

## Table 8.3: Results Validation Criteria

**Location**: Section 8.3 - Results Validation
**Dimensions**: 8 rows × 3 columns
**Style**: Light Grid Accent 1

### Purpose
Defines expected ranges for experimental results to validate correctness.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Check | Text | Result to validate |
| 2 | Criterion | Text | What to measure |
| 3 | Expected Range | Text | Acceptable value range |

### Row-by-Row Content

**Row 1 (Header)**
- Check: "Check"
- Criterion: "Criterion"
- Expected Range: "Expected Range"

**Row 2: Mean Similarity**
- Check: "Mean Similarity"
- Criterion: "Average score across all pairs"
- Expected Range: "60-70%"
- **Validation**: 0.60 <= mean(scores) <= 0.70

**Row 3: Std Deviation**
- Check: "Std Deviation"
- Criterion: "Score variability"
- Expected Range: "10-20%"
- **Validation**: 0.10 <= std(scores) <= 0.20

**Row 4: Top Scores**
- Check: "Top Scores"
- Criterion: "Best match per employee"
- Expected Range: ">75%"
- **Validation**: min(max_scores) > 0.75

**Row 5: Coverage**
- Check: "Coverage"
- Criterion: "Employees with recommendations"
- Expected Range: "100%"
- **Validation**: (employees_with_recs / total_employees) == 1.0

**Row 6: Blockchain Throughput**
- Check: "Blockchain Throughput"
- Criterion: "Operations per second"
- Expected Range: ">1000 ops/sec"
- **Validation**: throughput > 1000

**Row 7: Scalability R²**
- Check: "Scalability R²"
- Criterion: "Linear correlation"
- Expected Range: ">0.95"
- **Validation**: r_squared > 0.95

**Row 8: File Generation**
- Check: "File Generation"
- Criterion: "All output files created"
- Expected Range: "12 files"
- **Validation**: len(glob("results/*")) >= 12

### Key Insights
- 7 validation checks cover all key results
- Ranges based on experimental design
- All checks must pass for valid results

---

# Section 9: Appendix Tables

## Table 9.1: Version History

**Location**: Section 9.5 - Version History
**Dimensions**: 4 rows × 3 columns
**Style**: Light Grid Accent 1

### Purpose
Tracks document versions and changes over time.

### Structure
| Column | Header | Content Type | Description |
|--------|--------|--------------|-------------|
| 1 | Version | Text | Version number |
| 2 | Date | Text | Release date |
| 3 | Changes | Text | Summary of changes |

### Row-by-Row Content

**Row 1 (Header)**
- Version: "Version"
- Date: "Date"
- Changes: "Changes"

**Row 2: Version 1.0**
- Version: "1.0"
- Date: "2026-01-12"
- Changes: "Initial release with all 6 experiments"
- **Significance**: First complete version; production-ready

**Row 3: Version 1.1 (Planned)**
- Version: "1.1"
- Date: "TBD"
- Changes: "Planned: Additional scalability tests"
- **Scope**: Extended scalability to 5000+ employees

**Row 4: Version 2.0 (Planned)**
- Version: "2.0"
- Date: "TBD"
- Changes: "Planned: Real-world deployment configuration"
- **Scope**: Production deployment parameters and optimizations

### Key Insights
- Version 1.0 is current production release
- Future versions planned for extensions
- Semantic versioning (major.minor)

---

# Summary Statistics

## Total Tables in Document: 28 Tables

### By Section:
- **Section 1 (System)**: 3 tables
- **Section 2 (Datasets)**: 3 tables
- **Section 3 (Experiments)**: 6 tables
- **Section 4 (Algorithms)**: 3 tables
- **Section 5 (Metrics)**: 3 tables
- **Section 6 (Visualization)**: 3 tables
- **Section 7 (Reproducibility)**: 1 table
- **Section 8 (Validation)**: 3 tables
- **Section 9 (Appendix)**: 1 table

### By Dimensions:
- **2 columns**: 22 tables (parameter-value pairs)
- **3 columns**: 6 tables (metric-method-target)

### By Purpose:
- **Configuration**: 15 tables (system, algorithm, visualization settings)
- **Specification**: 9 tables (experiments, datasets, metrics)
- **Validation**: 4 tables (data, model, results validation)

### Total Data Points:
- **Rows**: ~250 rows across all tables
- **Cells**: ~600 cells of information
- **Parameters**: 200+ unique parameters documented

---

# Table Usage Guide

## For Reproducibility
**Use these tables**:
- Table 1.2 (Software versions)
- Table 7.1 (Random seeds)
- All Section 3 tables (Experiment configurations)

## For Validation
**Use these tables**:
- Table 8.1 (Data validation)
- Table 8.2 (Model validation)
- Table 8.3 (Results validation)

## For Extension
**Use these tables**:
- All Section 4 tables (Algorithm configurations)
- All Section 5 tables (Evaluation metrics)
- Table 3.5 (Scalability parameters)

## For Deployment
**Use these tables**:
- Table 1.1 (Hardware requirements)
- Table 1.3 (Model configuration)
- Table 5.2 (Performance targets)

---

# Conclusion

This detailed table description document provides comprehensive documentation of all 28 tables in the SkillChain DX Experiment Configuration document. Each table is described with:

✅ **Purpose** - Why the table exists
✅ **Structure** - Column definitions
✅ **Content** - Row-by-row details
✅ **Rationale** - Design decisions
✅ **Insights** - Key takeaways

These tables collectively provide complete specifications for reproducible, validated, and extensible research in AI-powered workforce development.

---

**Document**: DETAILED_TABLE_DESCRIPTIONS.md
**Tables Documented**: 28
**Total Rows**: ~250
**Total Parameters**: 200+
**Purpose**: Complete reference for all configuration tables
**Status**: Production-ready ✅


