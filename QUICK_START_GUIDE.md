# SkillChain-DX Quick Start Guide

## System Overview
SkillChain-DX is a blockchain-based skill inference and training recommendation system that uses AI to match employees with relevant training courses.

## Prerequisites
- Python 3.8+
- Required packages (install via `pip install -r requirements.txt`):
  - sentence-transformers
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - python-docx

## Quick Start

### 1. Run the Main Demo
```bash
python main.py
```

This will:
- Load sample data (employees, courses, job roles)
- Generate skill-based recommendations
- Issue blockchain credentials
- Display results

### 2. Run Comprehensive Experiments
```bash
python run_comprehensive_experiments.py
```

This will:
- Execute all 6 experiments
- Generate visualizations
- Create research paper document
- Save results to `results/` folder

### 3. Run Individual Components

#### Skill Inference Only
```python
from src.skill_inference import SkillInferenceEngine

engine = SkillInferenceEngine()
recommendations = engine.recommend_courses('EMP001', threshold=70)
print(recommendations)
```

#### Blockchain Operations Only
```python
from src.blockchain import CredentialLedger

ledger = CredentialLedger()
ledger.issue_credential('EMP001', 'TC001', 'Python Programming', '2024-01-01')
is_valid = ledger.verify_credential('EMP001', 'TC001', 'Python Programming', '2024-01-01')
```

## File Structure

```
SkillChain-DX/
├── src/
│   ├── skill_inference.py    # AI-based recommendation engine
│   ├── blockchain.py          # Blockchain credential management
│   └── experiments.py         # Experimental evaluation suite
├── data/
│   ├── employees.csv          # Employee profiles
│   ├── training_courses.csv   # Available courses
│   └── job_roles.csv          # Job role definitions
├── results/                   # Generated outputs
│   ├── *.png                  # Visualizations
│   ├── *.json                 # Data files
│   └── *.docx                 # Research paper
├── main.py                    # Main demonstration
├── run_comprehensive_experiments.py  # Full experimental suite
└── requirements.txt           # Python dependencies
```

## Key Features

### 1. Skill Inference
- Uses sentence transformers for semantic similarity
- Compares employee skills with course requirements
- Generates personalized recommendations

### 2. Blockchain Credentials
- SHA-256 hashing for credential integrity
- Immutable credential ledger
- Fast verification (sub-millisecond)

### 3. Experimental Evaluation
- 6 comprehensive experiments
- Performance benchmarking
- Scalability analysis

## Configuration

### Adjust Recommendation Threshold
Edit in `main.py` or pass as parameter:
```python
recommendations = engine.recommend_courses('EMP001', threshold=75)  # Default: 70
```

### Change Embedding Model
Edit in `src/skill_inference.py`:
```python
self.model = SentenceTransformer('all-MiniLM-L12-v2')  # Default: all-MiniLM-L6-v2
```

## Output Files

### After Running Experiments
- `results/SkillChain_DX_Implementation_Results.docx` - Research paper
- `results/experimental_results.json` - Raw data
- `results/exp*.png` - Visualizations
- `results/recommendations_report.json` - Detailed recommendations
- `results/verification_report.json` - Blockchain verification results

## Common Use Cases

### 1. Get Recommendations for an Employee
```python
from src.skill_inference import SkillInferenceEngine

engine = SkillInferenceEngine()
recs = engine.recommend_courses('EMP001', threshold=70)
print(recs[['course_id', 'course_name', 'similarity_score']])
```

### 2. Issue a Training Credential
```python
from src.blockchain import CredentialLedger

ledger = CredentialLedger()
ledger.issue_credential(
    employee_id='EMP001',
    course_id='TC001',
    course_name='Python Programming',
    completion_date='2024-01-01'
)
```

### 3. Verify a Credential
```python
is_valid = ledger.verify_credential(
    employee_id='EMP001',
    course_id='TC001',
    course_name='Python Programming',
    completion_date='2024-01-01'
)
print(f"Credential valid: {is_valid}")
```

### 4. Generate Similarity Heatmap
```python
from src.skill_inference import SkillInferenceEngine

engine = SkillInferenceEngine()
engine.create_similarity_heatmap('results/heatmap.png')
```

### 5. Generate Recommendations Report
```python
report = engine.generate_recommendations_report('results/report.json')
```

## Performance Tips

1. **For Large Datasets**: Use batch processing
2. **For Faster Inference**: Use smaller embedding models (L6 vs L12)
3. **For Better Accuracy**: Use larger models or ensemble methods
4. **For Production**: Cache embeddings to avoid recomputation

## Troubleshooting

### Issue: Slow first run
**Solution**: First run downloads embedding models (~90MB). Subsequent runs are faster.

### Issue: Out of memory
**Solution**: Reduce batch size or use smaller embedding model.

### Issue: No recommendations
**Solution**: Lower the similarity threshold (try 60% instead of 70%).

### Issue: Too many recommendations
**Solution**: Increase the similarity threshold (try 80% instead of 70%).

## Support

For questions or issues:
1. Check the research paper: `results/SkillChain_DX_Implementation_Results.docx`
2. Review experimental results: `results/experimental_results.json`
3. Examine the code documentation in `src/` files

## License
This project is part of academic research for Applied Sciences journal submission.

