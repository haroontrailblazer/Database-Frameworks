import pandas as pd

def transform_data(input_data):
    """
    Perform data transformation (example: multiply all values by 2)
    """
    transformed_data = input_data.apply(lambda x: x * 2)
    return transformed_data


def load_data(transformed_data):
    """
    Load transformed data into a CSV file
    """
    transformed_data.to_csv('transformed_data.csv', index=False)