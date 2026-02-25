# Function to validate clinical trial CSV file : validate_csv(file_path)
# Check that SubjectID column exists and is non-null
# Check that Age column exists and is between 18-65
# Return tuple: (is_valid: bool, errors: list)
import pandas as pd
def validate_csv(file_path):
    """
    Validate the clinical trial CSV file.
    Parameters:
    - file_path: str, path to the CSV file
    Returns:
    - is_valid: bool, True if the file is valid, False otherwise
    - errors: list of str, list of validation error messages
    
    Validation checks:
    - 'SubjectID' column exists and contains no null values
    - 'Age' column exists, contains no null values, and all values are between 18 and 65
    """
    errors = []
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        errors.append(f"Error reading CSV file: {e}")
        return False, errors

    # Check for SubjectID column
    if 'SubjectID' not in df.columns:
        errors.append("Missing 'SubjectID' column.")
    else:
        if df['SubjectID'].isnull().any():
            errors.append("'SubjectID' column contains null values.")

    # Check for Age column
    if 'Age' not in df.columns:
        errors.append("Missing 'Age' column.")
    else:
        if df['Age'].isnull().any():
            errors.append("'Age' column contains null values.")
        else:
            if not df['Age'].between(18, 65).all():
                errors.append("'Age' column contains values outside the range of 18-65.")

    is_valid = len(errors) == 0
    return is_valid, errors
