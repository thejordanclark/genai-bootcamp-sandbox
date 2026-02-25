# CSV Validator API Documentation

## Overview

The CSV Validator module provides functionality to validate clinical trial CSV files against predefined data quality rules. It ensures that critical columns exist and contain valid data within expected ranges.

## Module: `src.validators.csv_validator`

### Function: `validate_csv`

Validates a clinical trial CSV file according to specified data quality rules.

#### Signature

```python
validate_csv(file_path: str) -> tuple[bool, list[str]]
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file_path` | str | Yes | Path to the CSV file to validate (relative or absolute) |

#### Returns

Returns a tuple containing two elements:

| Position | Type | Description |
|----------|------|-------------|
| 0 | bool | `True` if the file passes all validation checks, `False` otherwise |
| 1 | list[str] | List of validation error messages (empty if valid) |

#### Validation Rules

The function performs the following validation checks:

1. **File Readability**
   - Confirms the file can be read as a valid CSV
   - Returns error if file is missing, corrupted, or not a valid CSV

2. **SubjectID Column**
   - Must exist in the CSV file
   - Must not contain any null/missing values

3. **Age Column**
   - Must exist in the CSV file
   - Must not contain any null/missing values
   - All values must be between 18 and 65 (inclusive)

#### Usage Examples

**Example 1: Valid CSV File**

```python
from src.validators.csv_validator import validate_csv

is_valid, errors = validate_csv('data/sample_valid.csv')

if is_valid:
    print("CSV file is valid!")
else:
    print("Validation errors found:")
    for error in errors:
        print(f"  - {error}")
```

**Example 2: Invalid CSV File**

```python
from src.validators.csv_validator import validate_csv

is_valid, errors = validate_csv('data/sample_invalid.csv')
# Returns: (False, ["'Age' column contains values outside the range of 18-65."])
```

**Example 3: Error Handling**

```python
from src.validators.csv_validator import validate_csv

try:
    is_valid, errors = validate_csv('data/patient_data.csv')
    
    if not is_valid:
        # Log errors for review
        with open('logs/validation_errors.log', 'a') as log:
            log.write(f"Validation failed: {', '.join(errors)}\n")
except Exception as e:
    print(f"Unexpected error: {e}")
```

#### Error Messages

| Error Message | Cause | Resolution |
|--------------|-------|------------|
| `Error reading CSV file: {details}` | File doesn't exist, isn't readable, or isn't valid CSV | Check file path and format |
| `Missing 'SubjectID' column.` | SubjectID column not found in CSV | Add SubjectID column to CSV |
| `'SubjectID' column contains null values.` | One or more SubjectID values are missing | Fill in all SubjectID values |
| `Missing 'Age' column.` | Age column not found in CSV | Add Age column to CSV |
| `'Age' column contains null values.` | One or more Age values are missing | Fill in all Age values |
| `'Age' column contains values outside the range of 18-65.` | Age values outside acceptable range | Ensure all ages are between 18-65 |

#### Dependencies

- **pandas**: Used for CSV file reading and data manipulation

#### Notes

- The function performs all validation checks even if early checks fail, returning all applicable error messages
- Age range validation (18-65) is inclusive on both ends
- The function is designed for clinical trial data validation where age restrictions are common
