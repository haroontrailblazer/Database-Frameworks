import pandas as pd
import data_transformation


def test_transform_data():
    """
    Test transformation logic
    """
    input_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    expected_output = pd.DataFrame({'A': [2, 4, 6], 'B': [8, 10, 12]})
    
    transformed_data = data_transformation.transform_data(input_data)
    
    assert transformed_data.equals(expected_output)


def test_load_data():
    """
    Test data loading (CSV writing and reading)
    """
    input_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    data_transformation.load_data(input_data)
    
    loaded_data = pd.read_csv('transformed_data.csv')
    
    assert input_data.equals(loaded_data)