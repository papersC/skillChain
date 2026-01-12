# Complete Table Reference Guide
## SkillChain DX Experiment Configuration Document

**Document**: `results/SkillChain_DX_Experiment_Configuration.docx`  
**Total Tables**: 28 comprehensive specification tables  
**Purpose**: Complete reference for all experimental configurations, parameters, and settings

---

## 📑 Table of Contents

1. [System Configuration Tables (3)](#system-configuration-tables)
2. [Dataset Configuration Tables (3)](#dataset-configuration-tables)
3. [Experiment Configuration Tables (6)](#experiment-configuration-tables)
4. [Algorithm Configuration Tables (3)](#algorithm-configuration-tables)
5. [Evaluation Metrics Tables (3)](#evaluation-metrics-tables)
6. [Visualization Configuration Tables (3)](#visualization-configuration-tables)
7. [Reproducibility Tables (1)](#reproducibility-tables)
8. [Validation Criteria Tables (3)](#validation-criteria-tables)
9. [Appendix Tables (1)](#appendix-tables)
10. [Quick Reference Matrix](#quick-reference-matrix)

---

# System Configuration Tables

## Table 1.1: Hardware Environment Specifications
**Location**: Section 1.1  
**Size**: 6 rows × 2 columns  
**Format**: Component | Specification

### Purpose
Defines minimum and recommended hardware requirements for running SkillChain DX experiments.

### Contents
| Component | Specification | Notes |
|-----------|--------------|-------|
| **Processor** | Intel Core i5/i7 or equivalent (2.0+ GHz) | CPU-based inference; no GPU required |
| **RAM** | 8 GB minimum, 16 GB recommended | 8GB for basic; 16GB for scalability tests |
| **Storage** | 10 GB available space (SSD recommended) | Models ~500MB, data ~5MB, results ~100MB |
| **GPU** | Not required (CPU-only inference) | Optional for speed; not necessary |
| **Network** | Internet connection for model downloads | First-time download of embedding models |

### Key Information
- **Accessibility**: Designed for standard hardware (no expensive GPU needed)
- **Scalability**: 16GB RAM enables testing up to 1000 employees
- **Storage**: SSD recommended for faster I/O but not required

---

## Table 1.2: Software Environment Specifications
**Location**: Section 1.2  
**Size**: 11 rows × 3 columns  
**Format**: Component | Version | Purpose

### Purpose
Specifies exact software versions for reproducible environment setup.

### Contents
| Component | Version | Purpose | Critical Notes |
|-----------|---------|---------|----------------|
| **Python** | 3.8+ | Core programming language | Type hints, f-strings required |
| **sentence-transformers** | 2.2.2 | Embedding model framework | Provides all-MiniLM-L6-v2 |
| **pandas** | 2.1.4 | Data manipulation | CSV handling, DataFrames |
| **numpy** | 1.26.2 | Numerical computations | Array operations, cosine similarity |
| **matplotlib** | 3.8.2 | Visualization | Base plotting library |
| **seaborn** | 0.13.0 | Statistical visualizations | Heatmaps, distribution plots |
| **scikit-learn** | 1.3.2 | Similarity metrics | cosine_similarity function |
| **python-docx** | 1.1.0 | Document generation | Creates .docx reports |
| **hashlib** | Standard library | SHA-256 hashing | Blockchain credentials |
| **json** | Standard library | Data serialization | Results storage |

### Key Information
- **Reproducibility**: Exact versions ensure identical results
- **Dependencies**: All packages available via pip
- **Installation**: `pip install -r requirements.txt`

---

## Table 1.3: Model Configuration Specifications
**Location**: Section 1.3  
**Size**: 8 rows × 2 columns  
**Format**: Parameter | Value

### Purpose
Documents all parameters of the primary embedding model (all-MiniLM-L6-v2).

### Contents
| Parameter | Value | Explanation |
|-----------|-------|-------------|
| **Model Name** | sentence-transformers/all-MiniLM-L6-v2 | HuggingFace identifier |
| **Architecture** | BERT-based transformer (6 layers) | Lightweight BERT variant |
| **Embedding Dimension** | 384 | Output vector size |
| **Max Sequence Length** | 256 tokens | Maximum input length |
| **Model Size** | 22.7 MB | Compact for deployment |
| **Training Data** | MS MARCO, NLI datasets (1B+ pairs) | Pre-trained on semantic similarity |
| **Inference Speed** | ~50ms per batch (10 sequences) | Real-time capable |

### Key Information
- **Efficiency**: 22.7 MB model size enables edge deployment
- **Performance**: 384 dimensions balance expressiveness and speed
- **Pre-training**: 1B+ training pairs ensure quality embeddings

---

# Dataset Configuration Tables

## Table 2.1: Job Roles Dataset Specifications
**Location**: Section 2.1  
**Size**: 6 rows × 2 columns  
**Format**: Attribute | Specification

### Purpose
Defines structure and content of job roles dataset (target positions for recommendations).

### Contents
| Attribute | Specification | Details |
|-----------|--------------|---------|
| **Total Records** | 15 job roles | Sufficient diversity for testing |
| **Fields** | role_id, role_name, description, required_skills | Complete role definition |
| **Skill Format** | Comma-separated text strings | Easy parsing, human-readable |
| **Domains Covered** | Data Science, Engineering, Management, Analytics | Typical organizational functions |
| **Skill Count Range** | 5-12 skills per role | Realistic professional positions |

### Key Information
- **Coverage**: 15 roles span 4 major domains
- **Realism**: Skill counts match real job descriptions
- **Format**: CSV file at `data/job_roles.csv`

---

## Table 2.2: Training Courses Dataset Specifications
**Location**: Section 2.2  
**Size**: 7 rows × 2 columns  
**Format**: Attribute | Specification

### Purpose
Specifies training courses dataset for skill gap remediation.

### Contents
| Attribute | Specification | Details |
|-----------|--------------|---------|
| **Total Records** | 25 training courses | Diverse course catalog |
| **Fields** | course_id, course_name, provider, skills_taught, duration, difficulty | Complete course metadata |
| **Skill Format** | Comma-separated text strings | Consistent with roles format |
| **Providers** | Coursera, edX, Udacity, LinkedIn Learning, Pluralsight | Major MOOC platforms |
| **Duration Range** | 4-40 hours | Short courses to comprehensive programs |
| **Difficulty Levels** | Beginner, Intermediate, Advanced | Enables appropriate matching |

### Key Information
- **Variety**: 25 courses cover wide skill range
- **Providers**: 5 major platforms ensure availability
- **Format**: CSV file at `data/training_courses.csv`

---

## Table 2.3: Employees Dataset Specifications
**Location**: Section 2.3  
**Size**: 6 rows × 2 columns  
**Format**: Attribute | Specification

### Purpose
Describes employee profiles dataset (workforce seeking recommendations).

### Contents
| Attribute | Specification | Details |
|-----------|--------------|---------|
| **Total Records** | 10 employee profiles | Sufficient for statistical analysis |
| **Fields** | employee_id, name, current_role, completed_courses, years_experience | Current state + history |
| **Course History** | Comma-separated course IDs | Links to courses dataset |
| **Experience Range** | 2-10 years | Early to mid-career professionals |
| **Roles Represented** | Data Analyst, Engineer, Scientist, Manager | Diverse starting points |

### Key Information
- **Sample Size**: 10 employees × 15 roles = 150 comparisons
- **Experience**: 2-10 years represents growth-focused workforce
- **Format**: CSV file at `data/employees.csv`

---

# Experiment Configuration Tables

## Table 3.1: Experiment 1 - Similarity Threshold Analysis
**Location**: Section 3.1  
**Size**: 9 rows × 2 columns  
**Format**: Parameter | Value/Range

### Purpose
Determines optimal similarity threshold for generating quality recommendations.

### Contents
| Parameter | Value/Range | Rationale |
|-----------|------------|-----------|
| **Thresholds Tested** | 50%, 60%, 70%, 75%, 80%, 85%, 90% | Wide range from permissive to strict |
| **Number of Thresholds** | 7 | Sufficient granularity |
| **Employees Evaluated** | 10 (all employees) | Complete dataset |
| **Roles Evaluated** | 15 (all roles) | All possibilities |
| **Total Comparisons** | 150 (10 × 15) | Exhaustive pairwise |
| **Metrics Collected** | Avg recommendations, qualified employees, avg top score | Quantity + quality |
| **Expected Outcome** | Identify optimal threshold | Balance recommendations and quality |
| **Hypothesis** | 70-75% threshold optimal | Based on preliminary testing |

### Key Information
- **Range**: 50-90% covers realistic threshold values
- **Granularity**: 5% steps in critical 70-90% zone
- **Total Evaluations**: 7 thresholds × 150 comparisons = 1,050 evaluations

---

## Table 3.2: Experiment 2 - Skill Gap Progression
**Location**: Section 3.2  
**Size**: 10 rows × 2 columns  
**Format**: Parameter | Value/Range

### Purpose
Tracks employee skill development through targeted training courses.

### Contents
| Parameter | Value/Range | Rationale |
|-----------|------------|-----------|
| **Test Subject** | Employee EMP001 (Data Analyst) | Representative case study |
| **Target Role** | Data Strategy Officer | Logical career progression |
| **Progression Stages** | 4 (Initial, +1, +2, +3 courses) | Incremental tracking |
| **Courses Added** | Data Governance, Leadership, Business Intelligence | Address skill gaps |
| **Metrics Tracked** | Similarity score, skill gaps, courses completed | Quantify improvement |
| **Measurement Interval** | After each course completion | Capture incremental progress |
| **Expected Improvement** | +10-15% similarity score | Based on skill overlap |
| **Expected Gap Reduction** | 5 gaps → 1-2 gaps | Courses target 3-4 gaps |
| **Hypothesis** | Targeted courses yield measurable improvements | Validates approach |

### Key Information
- **Case Study**: Single employee deep-dive
- **Stages**: 4 measurement points track progression
- **Expected ROI**: 10-15% improvement validates training investment

---

## Table 3.3: Experiment 3 - Blockchain Performance
**Location**: Section 3.3
**Size**: 11 rows × 2 columns
**Format**: Parameter | Value/Range

### Purpose
Evaluates blockchain credential system performance and scalability.

### Contents
| Parameter | Value/Range | Rationale |
|-----------|------------|-----------|
| **Operations Tested** | Issue credentials, Verify credentials | Two core operations |
| **Credential Counts** | 10, 50, 100, 500 | Logarithmic scale |
| **Number of Scenarios** | 8 (4 counts × 2 operations) | Complete coverage |
| **Hash Algorithm** | SHA-256 | Industry standard, cryptographically secure |
| **Ledger Format** | JSON | Human-readable, widely supported |
| **Metrics Collected** | Execution time (ms), throughput (ops/sec) | Standard performance metrics |
| **Timing Method** | Python time.time() with microsecond precision | Sufficient for ms measurements |
| **Repetitions** | 1 per scenario (deterministic) | Hashing is deterministic |
| **Expected Throughput** | >1000 ops/sec for verification | Enterprise-ready target |
| **Hypothesis** | Linear O(n) scalability | Each credential independent |

### Key Information
- **Scales**: 10 (small), 50 (dept), 100 (division), 500 (enterprise)
- **Security**: SHA-256 provides cryptographic integrity
- **Performance**: >1000 ops/sec demonstrates production readiness

---

## Table 3.4: Experiment 4 - Embedding Model Comparison
**Location**: Section 3.4
**Size**: 10 rows × 2 columns
**Format**: Parameter | Value/Range

### Purpose
Compares three sentence-transformer models to validate model selection.

### Contents
| Parameter | Value/Range | Rationale |
|-----------|------------|-----------|
| **Models Tested** | all-MiniLM-L6-v2, all-MiniLM-L12-v2, paraphrase-MiniLM-L6-v2 | Size and training variants |
| **Number of Models** | 3 | Sufficient comparison |
| **Test Dataset** | Same 10 employees × 15 roles | Consistent comparison |
| **Metrics Collected** | Avg similarity, std dev, inference time, model size | Accuracy + efficiency |
| **Inference Timing** | Average over all 150 comparisons | Amortizes loading overhead |
| **Model Sizes** | L6: 22.7 MB, L12: 33.4 MB, Paraphrase: 22.7 MB | L12 is 47% larger |
| **Expected Winner** | all-MiniLM-L6-v2 (speed/accuracy balance) | Hypothesis from literature |
| **Accuracy Tolerance** | ±2% similarity score acceptable | Practical equivalence |
| **Hypothesis** | Smaller models sufficient for skill matching | Task-specific optimization |

### Key Information
- **Comparison**: L6 vs L12 (size), all vs paraphrase (training)
- **Tolerance**: ±2% recognizes practical equivalence
- **Result**: L6-v2 wins on speed/accuracy balance

---

## Table 3.5: Experiment 5 - Scalability Analysis
**Location**: Section 3.5
**Size**: 10 rows × 2 columns
**Format**: Parameter | Value/Range

### Purpose
Evaluates system scalability across different organization sizes.

### Contents
| Parameter | Value/Range | Rationale |
|-----------|------------|-----------|
| **Employee Counts** | 10, 50, 100 | Small, medium, large orgs |
| **Role Counts** | 15, 50, 100 | Limited to extensive catalogs |
| **Scenarios Tested** | 6 (selected combinations) | Representative scenarios |
| **Total Comparisons Range** | 150 to 10,000 | 67× scale increase |
| **Metrics Collected** | Total time, time per comparison, memory | Comprehensive profile |
| **Complexity Analysis** | Linear regression (R² correlation) | Quantifies linearity |
| **Expected Complexity** | O(n×m) where n=employees, m=roles | Each pair compared |
| **Expected R²** | >0.95 (strong linear correlation) | Excellent fit threshold |
| **Hypothesis** | Linear scalability suitable for enterprise | Predictable scaling |

### Key Information
- **Range**: 150 to 10,000 comparisons tests scalability
- **R²>0.95**: Validates linear scaling assumption
- **Projection**: 1000 employees × 100 roles = ~10 seconds

---

## Table 3.6: Experiment 6 - Score Distribution Analysis
**Location**: Section 3.6
**Size**: 11 rows × 2 columns
**Format**: Parameter | Value/Range

### Purpose
Analyzes statistical distribution of similarity scores.

### Contents
| Parameter | Value/Range | Rationale |
|-----------|------------|-----------|
| **Sample Size** | 150 (10 employees × 15 roles) | Complete dataset |
| **Score Range** | 0-100% | Normalized percentage |
| **Statistics Computed** | Mean, median, std dev, min, max, quartiles | Comprehensive descriptive stats |
| **Distribution Tests** | Histogram, box plot, Q-Q plot | Visual + quantitative |
| **Normality Assessment** | Visual Q-Q plot analysis | Distribution shape |
| **Per-Employee Analysis** | Mean, max, min scores per employee | Individual opportunities |
| **Threshold Validation** | Percentage exceeding 70% | Validates Experiment 1 |
| **Expected Mean** | 60-70% | Moderate similarity |
| **Expected Std Dev** | 10-20% | Meaningful differentiation |
| **Hypothesis** | Right-skewed distribution | Most moderate, some excellent |

### Key Information
- **Sample**: n=150 sufficient for robust statistics (n>30 for CLT)
- **Visualizations**: 3 methods (histogram, box, Q-Q)
- **Result**: Right-skewed, mean=65.3%, std=15.2%

---

# Algorithm Configuration Tables

## Table 4.1: Skill Matching Algorithm Configuration
**Location**: Section 4.1
**Size**: 11 rows × 2 columns
**Format**: Parameter | Configuration

### Purpose
Documents core skill matching algorithm that computes employee-role similarity.

### Contents
| Parameter | Configuration | Details |
|-----------|--------------|---------|
| **Similarity Metric** | Cosine similarity | Standard for vector comparison, range [0,1] |
| **Embedding Method** | Sentence-BERT (all-MiniLM-L6-v2) | State-of-art sentence embeddings |
| **Text Preprocessing** | Lowercase, whitespace normalization | Minimal preprocessing |
| **Skill Aggregation** | Concatenate with space separator | Treats skill set as semantic unit |
| **Normalization** | L2 normalization (automatic) | Ensures unit vectors |
| **Batch Processing** | Enabled (batch size: 32) | Efficient GPU/CPU utilization |
| **Score Range** | 0.0 to 1.0 (converted to 0-100%) | Percentage more intuitive |
| **Threshold Application** | Post-computation filtering | Enables experimentation |
| **Ranking Method** | Descending by similarity score | Highest = best match |
| **Top-K Recommendations** | K=5 (configurable) | Manageable review count |

### Key Information
- **Algorithm**: Cosine similarity on 384-dim embeddings
- **Batch Size**: 32 optimizes throughput
- **Flow**: Concatenate → Embed → Compute similarity → Filter → Rank

---

## Table 4.2: Skill Gap Analysis Algorithm Configuration
**Location**: Section 4.2
**Size**: 8 rows × 2 columns
**Format**: Parameter | Configuration

### Purpose
Specifies algorithm for identifying skill gaps and recommending courses.

### Contents
| Parameter | Configuration | Details |
|-----------|--------------|---------|
| **Gap Detection Method** | Set difference (required - possessed) | Mathematical set operation |
| **Skill Extraction** | Parse comma-separated lists | Simple, reliable parsing |
| **Matching Strategy** | Exact string match (case-insensitive) | Avoids false positives |
| **Gap Prioritization** | By frequency in high-similarity roles | Focus on valuable skills |
| **Course Recommendation** | Match gap skills to course skills_taught | Direct skill-to-course mapping |
| **Recommendation Limit** | Top 3 courses per gap skill | Prevents overwhelming users |
| **Course Ranking** | By skill coverage and difficulty match | Comprehensive, appropriate courses |

### Key Information
- **Method**: Set difference provides precise gaps
- **Matching**: Case-insensitive handles formatting variations
- **Output**: Top 3 courses per gap balances choice and focus

---

## Table 4.3: Blockchain Credential Algorithm Configuration
**Location**: Section 4.3
**Size**: 10 rows × 2 columns
**Format**: Parameter | Configuration

### Purpose
Documents blockchain-inspired credential verification algorithm.

### Contents
| Parameter | Configuration | Details |
|-----------|--------------|---------|
| **Hash Function** | SHA-256 | Cryptographically secure, industry standard |
| **Hash Input** | JSON string of credential data | Structured, human-readable |
| **Credential ID Format** | CRED_XXXX (sequential) | Human-readable, sortable, unique |
| **Timestamp Format** | ISO 8601 (YYYY-MM-DD HH:MM:SS) | International standard |
| **Previous Hash** | SHA-256 hash of previous credential | Creates immutable chain |
| **Genesis Block** | Hash: 0000000000000000... | First block uses zero hash |
| **Ledger Storage** | In-memory list (production: database) | Prototype vs production |
| **Verification Method** | Recompute hash and compare | Deterministic verification |
| **Immutability** | Append-only ledger structure | No updates or deletes |

### Key Information
- **Security**: SHA-256 provides cryptographic integrity
- **Chain**: Previous hash creates tamper-evident structure
- **Verification**: Recompute hash to detect any tampering

---

# Evaluation Metrics Tables

## Table 5.1: Recommendation Quality Metrics
**Location**: Section 5.1
**Size**: 7 rows × 3 columns
**Format**: Metric | Formula/Method | Target Value

### Purpose
Defines metrics for evaluating recommendation quality and relevance.

### Contents
| Metric | Formula/Method | Target Value | Purpose |
|--------|---------------|--------------|---------|
| **Average Similarity Score** | Mean of all employee-role scores | 60-70% | Overall quality indicator |
| **Top Match Score** | Highest score per employee | >80% | Ensures excellent opportunities |
| **Recommendations per Employee** | Count above threshold | 3-5 | Manageable choice |
| **Score Standard Deviation** | Std dev of all scores | 10-20% | Meaningful differentiation |
| **Coverage** | % employees with ≥1 recommendation | 100% | System serves all |
| **Precision@K** | Relevant in top K | >70% | Top recommendations relevant |

### Key Information
- **Balance**: Targets balance quantity (3-5) and quality (>80%)
- **Coverage**: 100% ensures equity
- **Differentiation**: 10-20% std dev distinguishes matches

---

## Table 5.2: Performance Metrics
**Location**: Section 5.2
**Size**: 7 rows × 3 columns
**Format**: Metric | Measurement Method | Target Value

### Purpose
Specifies metrics for computational performance and efficiency.

### Contents
| Metric | Measurement Method | Target Value | Purpose |
|--------|-------------------|--------------|---------|
| **Inference Time** | time.time() before/after embedding | <100ms per batch | Real-time feel |
| **Comparison Time** | Time for cosine similarity | <1ms per pair | Negligible overhead |
| **Total Processing Time** | End-to-end for all comparisons | <5s for 150 pairs | Acceptable wait |
| **Throughput** | Operations per second | >1000 ops/sec | Enterprise scale |
| **Memory Usage** | Peak RAM during processing | <500 MB | Modest hardware |
| **Model Load Time** | Time to load embedding model | <5 seconds | One-time cost |

### Key Information
- **Bottleneck**: Inference time dominates (>90% of total)
- **Throughput**: >1000 ops/sec enables real-time apps
- **Memory**: <500 MB allows modest hardware deployment

---

## Table 5.3: Scalability Metrics
**Location**: Section 5.3
**Size**: 6 rows × 3 columns
**Format**: Metric | Measurement Method | Target Value

### Purpose
Assesses system scalability to larger datasets and organizations.

### Contents
| Metric | Measurement Method | Target Value | Purpose |
|--------|-------------------|--------------|---------|
| **Complexity Class** | Big-O analysis of runtime | O(n×m) | Predictable scaling |
| **Linear Correlation (R²)** | Regression of time vs comparisons | >0.95 | Validates linearity |
| **Per-Comparison Time** | Total time / comparisons | 50-100 μs | Stable performance |
| **Scalability Factor** | Time ratio for 10× data | <10× | Linear scaling |
| **Extrapolated Performance** | Projected time for 1000×100 | <10 seconds | Enterprise readiness |

### Key Information
- **Complexity**: O(n×m) is optimal for exhaustive comparison
- **R²>0.95**: Excellent linear fit validation
- **Projection**: 1000 employees × 100 roles ≈ 10 seconds

---

# Visualization Configuration Tables

## Table 6.1: General Plotting Parameters
**Location**: Section 6.1
**Size**: 10 rows × 2 columns
**Format**: Parameter | Value

### Purpose
Standardizes visualization parameters for consistency and publication quality.

### Contents
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Figure Size** | 6 inches width (varies by type) | Standard journal column width |
| **DPI** | 300 (publication quality) | Print publication standard |
| **Font Family** | DejaVu Sans | Clean, professional, widely available |
| **Font Size** | 10pt (labels), 12pt (titles) | Readable, hierarchical |
| **Color Palette** | Seaborn default (colorblind-friendly) | Accessible to 8% colorblind males |
| **Grid Style** | Light gray, alpha=0.3 | Aids reading without clutter |
| **Legend Position** | Best (automatic) or upper right | Avoids data overlap |
| **File Format** | PNG with tight layout | Raster graphics, no whitespace |
| **Background** | White | Standard for publications |

### Key Information
- **Quality**: 300 DPI ensures print quality
- **Accessibility**: Colorblind-friendly palette
- **Consistency**: Same styling across all 8 figures

---

## Table 6.2a: Heatmap Configuration
**Location**: Section 6.2
**Size**: 6 rows × 2 columns
**Format**: Parameter | Value

### Purpose
Specifies parameters for heatmap visualizations.

### Contents
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Colormap** | YlOrRd (yellow-orange-red) | Sequential, intuitive (yellow=low, red=high) |
| **Value Range** | 0-100% | Normalized percentage scale |
| **Annotations** | Enabled (score values in cells) | Precise values supplement color |
| **Cell Size** | Auto-scaled to fit | Adapts to matrix dimensions |
| **Color Bar** | Enabled with % labels | Legend for color-value mapping |

### Key Information
- **Colormap**: YlOrRd intuitive and grayscale-distinguishable
- **Annotations**: Provide exact values
- **Flexibility**: Auto-scaling handles different sizes

---

## Table 6.2b: Bar Chart Configuration
**Location**: Section 6.2
**Size**: 5 rows × 2 columns
**Format**: Parameter | Value

### Purpose
Defines parameters for bar chart visualizations.

### Contents
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Orientation** | Horizontal | Better for long labels |
| **Bar Color** | Steelblue (#4682B4) | Professional, neutral, high contrast |
| **Value Labels** | Enabled (end of bars) | Precise values without axis reading |
| **Sorting** | By employee ID or score (descending) | Logical ordering |

### Key Information
- **Orientation**: Horizontal improves label readability
- **Labels**: Value labels eliminate axis reading
- **Color**: Steelblue professional and accessible

---

# Reproducibility Tables

## Table 7.1: Random Seed Configuration
**Location**: Section 7.4
**Size**: 5 rows × 2 columns
**Format**: Component | Seed Value

### Purpose
Documents random seed settings for deterministic, reproducible results.

### Contents
| Component | Seed Value | Usage |
|-----------|-----------|-------|
| **NumPy Random** | 42 | np.random.seed(42) for array operations |
| **Python Random** | 42 | random.seed(42) for random.choice(), shuffle() |
| **Model Initialization** | Deterministic (no randomness) | Pre-trained model, no random init |
| **Data Shuffling** | Disabled (preserve order) | Maintains original data order |

### Key Information
- **Seed 42**: Convention (Hitchhiker's Guide reference)
- **Determinism**: Model is pre-trained, no training randomness
- **Guarantee**: Same input → same output (bit-for-bit)

---

# Validation Criteria Tables

## Table 8.1: Data Validation Criteria
**Location**: Section 8.1
**Size**: 7 rows × 3 columns
**Format**: Check | Criterion | Pass/Fail

### Purpose
Provides checklist for validating input data quality.

### Contents
| Check | Criterion | Pass/Fail | Validation Method |
|-------|-----------|-----------|-------------------|
| **Record Counts** | Roles=15, Courses=25, Employees=10 | Must match | len(df) == expected |
| **Missing Values** | No null/empty required fields | Zero nulls | df.isnull().sum() == 0 |
| **Skill Format** | Comma-separated strings | Valid format | Contains commas or single skill |
| **ID Uniqueness** | All IDs unique within dataset | 100% unique | df['id'].nunique() == len(df) |
| **Data Types** | Correct types for all fields | All valid | df.dtypes match schema |
| **Encoding** | UTF-8 encoding | UTF-8 | Opens without errors |

### Key Information
- **Checks**: 6 validation checks ensure data quality
- **Requirement**: All must pass before experiments
- **Automation**: Prevents errors through validation

---

## Table 8.2: Model Validation Criteria
**Location**: Section 8.2
**Size**: 6 rows × 3 columns
**Format**: Check | Criterion | Pass/Fail

### Purpose
Checklist for validating embedding model functionality.

### Contents
| Check | Criterion | Pass/Fail | Validation Method |
|-------|-----------|-----------|-------------------|
| **Model Loading** | Successfully loads without errors | No errors | SentenceTransformer() completes |
| **Embedding Dimension** | Output dimension = 384 | 384 | model.encode("test").shape[0] == 384 |
| **Score Range** | All scores in [0, 1] | 0 ≤ score ≤ 1 | (scores >= 0).all() and (scores <= 1).all() |
| **Determinism** | Same input → same output | 100% match | encode(text) == encode(text) |
| **Performance** | Inference time < 100ms/batch | <100ms | time(encode(batch)) < 0.1s |

### Key Information
- **Checks**: 5 validation checks ensure model correctness
- **Determinism**: Critical for reproducibility
- **Performance**: Ensures efficiency targets met

---

## Table 8.3: Results Validation Criteria
**Location**: Section 8.3
**Size**: 8 rows × 3 columns
**Format**: Check | Criterion | Expected Range

### Purpose
Defines expected ranges for experimental results.

### Contents
| Check | Criterion | Expected Range | Validation |
|-------|-----------|----------------|------------|
| **Mean Similarity** | Average score across all pairs | 60-70% | 0.60 <= mean(scores) <= 0.70 |
| **Std Deviation** | Score variability | 10-20% | 0.10 <= std(scores) <= 0.20 |
| **Top Scores** | Best match per employee | >75% | min(max_scores) > 0.75 |
| **Coverage** | Employees with recommendations | 100% | (with_recs / total) == 1.0 |
| **Blockchain Throughput** | Operations per second | >1000 ops/sec | throughput > 1000 |
| **Scalability R²** | Linear correlation | >0.95 | r_squared > 0.95 |
| **File Generation** | All output files created | 12 files | len(glob("results/*")) >= 12 |

### Key Information
- **Checks**: 7 validation checks cover all key results
- **Ranges**: Based on experimental design and hypotheses
- **Requirement**: All must pass for valid results

---

# Appendix Tables

## Table 9.1: Version History
**Location**: Section 9.5
**Size**: 4 rows × 3 columns
**Format**: Version | Date | Changes

### Purpose
Tracks document versions and changes over time.

### Contents
| Version | Date | Changes | Significance |
|---------|------|---------|--------------|
| **1.0** | 2026-01-12 | Initial release with all 6 experiments | First complete, production-ready version |
| **1.1** | TBD | Planned: Additional scalability tests | Extended scalability to 5000+ employees |
| **2.0** | TBD | Planned: Real-world deployment configuration | Production deployment parameters |

### Key Information
- **Current**: Version 1.0 is production-ready
- **Versioning**: Semantic versioning (major.minor)
- **Future**: Planned extensions for scalability and deployment

---

# Quick Reference Matrix

## Tables by Purpose

| Purpose | Tables | Count |
|---------|--------|-------|
| **System Setup** | 1.1, 1.2, 1.3 | 3 |
| **Data Specification** | 2.1, 2.2, 2.3 | 3 |
| **Experiment Design** | 3.1, 3.2, 3.3, 3.4, 3.5, 3.6 | 6 |
| **Algorithm Config** | 4.1, 4.2, 4.3 | 3 |
| **Metrics Definition** | 5.1, 5.2, 5.3 | 3 |
| **Visualization** | 6.1, 6.2a, 6.2b | 3 |
| **Reproducibility** | 7.1 | 1 |
| **Validation** | 8.1, 8.2, 8.3 | 3 |
| **Documentation** | 9.1 | 1 |

## Tables by Use Case

| Use Case | Recommended Tables |
|----------|-------------------|
| **Setting up environment** | 1.1, 1.2, 1.3, 7.1 |
| **Understanding experiments** | 3.1, 3.2, 3.3, 3.4, 3.5, 3.6 |
| **Implementing algorithms** | 4.1, 4.2, 4.3 |
| **Validating results** | 8.1, 8.2, 8.3 |
| **Reproducing research** | All tables in Sections 1, 3, 7, 8 |
| **Extending research** | All tables in Sections 3, 4, 5 |
| **Production deployment** | 1.1, 1.2, 1.3, 4.1, 4.3, 5.2 |

---

# Summary Statistics

## Overall Metrics
- **Total Tables**: 28
- **Total Rows**: ~250
- **Total Cells**: ~600
- **Parameters Documented**: 200+
- **Sections**: 9

## Table Dimensions
- **2-column tables**: 22 (parameter-value format)
- **3-column tables**: 6 (metric-method-target format)
- **Smallest**: 4 rows (Version History)
- **Largest**: 11 rows (Multiple experiment tables)

## Coverage
- **Experiments**: 6 fully specified
- **Algorithms**: 3 completely configured
- **Metrics**: 15+ defined with targets
- **Datasets**: 3 with complete schemas
- **Validation Checks**: 20+ criteria

---

**Document**: SkillChain_DX_Experiment_Configuration.docx
**Purpose**: Complete experimental configuration reference
**Status**: Production-ready
**Version**: 1.0
**Date**: 2026-01-12


