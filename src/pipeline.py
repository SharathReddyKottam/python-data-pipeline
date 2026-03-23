import pandas as pd
import json
import os

def load_data(filepath):
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} rows")
    return df

def clean_data(df):
    # Drop rows where name is missing
    df = df.dropna(subset=['name'])

    # Fill missing age and salary with column average
    df['age'] = df['age'].fillna(df['age'].mean())
    df['salary'] = df['salary'].fillna(df['salary'].mean())

    # Remove duplicate rows
    # Remove duplicate rows ignoring id column
    df = df.drop_duplicates(subset=['name', 'age', 'salary', 'department'])
    print(f"Cleaned data has {len(df)} rows")
    return df

def generate_report(df):
    report = {
        "total_rows": len(df),
        "average_age": round(df['age'].mean(), 2),
        "average_salary": round(df['salary'].mean(), 2),
        "departments": df['department'].value_counts().to_dict()
    }
    return report

def save_report(report, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"Report saved to {output_path}")

if __name__ == "__main__":
    df = load_data("data/sample.csv")
    df = clean_data(df)
    report = generate_report(df)
    save_report(report, "output/report.json")