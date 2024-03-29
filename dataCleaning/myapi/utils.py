import pandas as pd


def datafile_to_df(file_path):
    """
    Converts the given file to a CSV file.

    Inputs:
        file_path: str
    
    Returns: 
        pd.DataFrame
    """

    if file_path.endswith('.csv'):
        df = pd.read_csv('./' + file_path)
    elif file_path.endswith('.xlsx'):
        print('./' + file_path)
        df = pd.read_excel('./' + file_path)
    else:
        raise ValueError('Unsupported file type')
    return df
    