# Python Data Pipeline with Jenkins CI/CD

A Python-based data cleaning pipeline automated with Jenkins CI/CD.

## Project Overview
Ingests raw CSV data, cleans it using Pandas, and generates a JSON summary report. The entire process is automated using Jenkins pipeline triggered by GitHub webhooks.

## Tech Stack
- Python 3.11
- Pandas
- Pytest
- Docker
- Jenkins
- GitHub Webhooks
- ngrok

## Project Structure
```
data-pipeline/
├── src/
│   └── pipeline.py        # data cleaning logic
├── tests/
│   └── test_pipeline.py   # automated unit tests
├── data/
│   └── sample.csv         # input data
├── output/
│   └── report.json        # generated report
├── Dockerfile
├── Jenkinsfile
└── requirements.txt
```

## Pipeline Stages
1. **Build** - Install dependencies
2. **Test** - Run pytest unit tests
3. **Dockerize** - Build Docker image
4. **Run** - Execute pipeline inside container

## How It Works
1. Push code to GitHub
2. GitHub notifies Jenkins via webhook
3. Jenkins automatically runs all 4 stages
4. Cleaned data report saved to output/report.json

## What Gets Cleaned
- Missing names → rows dropped
- Missing age/salary → filled with column average
- Duplicate rows → removed