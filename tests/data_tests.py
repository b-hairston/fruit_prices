import pandas as pd
import pytest
import os
import capsys
from transformations import normalize_csv

def test_normalize_csv():
    # Create a sample input file
    input_file = "test_input.csv"
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    df.to_csv(input_file, index=False)
    
    # Call the function
    normalize_csv(input_file)
    
    # Assert the expected output
    expected_output = "col1    int64\ncol2    object\ndtype: object\n"
    captured_output = capsys.readouterr().out
    assert captured_output == expected_output
    
    # Clean up the sample input file
    os.remove(input_file)