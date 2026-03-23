import pandas as pd
import pytest
import sys
sys.path.insert(0, 'src')
from pipeline import clean_data

def get_sample_data():
    data = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Alice', None, 'Charlie', 'Charlie', 'Eve'],
        'age': [28, 33, 35, 35, None],
        'salary': [55000, 62000, 58000, 58000, None],
        'department': ['Engineering', 'Marketing', 'Engineering', 'Engineering', 'HR']
    }
    return pd.DataFrame(data)

def test_missing_names_dropped():
    df = clean_data(get_sample_data())
    assert df['name'].isnull().sum() == 0

def test_duplicates_removed():
    df = clean_data(get_sample_data())
    dupes = df.duplicated(subset=['name', 'age', 'salary', 'department'])
    assert dupes.sum() == 0

def test_missing_age_filled():
    df = clean_data(get_sample_data())
    assert df['age'].isnull().sum() == 0

def test_missing_salary_filled():
    df = clean_data(get_sample_data())
    assert df['salary'].isnull().sum() == 0