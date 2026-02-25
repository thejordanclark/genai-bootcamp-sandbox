import pytest
from src.validators.csv_validator import validate_csv

# Test valid CSV file : 'data/sample_valid.csv'
def test_validate_csv_valid():
    is_valid, errors = validate_csv('data/sample_valid.csv')
    assert is_valid == True
    assert errors == []

# Test invalid CSV file : 'data/sample_invalid.csv'
def test_validate_csv_invalid():
    is_valid, errors = validate_csv('data/sample_invalid.csv')
    assert is_valid == False
    assert len(errors) > 0
