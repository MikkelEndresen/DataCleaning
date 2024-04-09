import pandas as pd
from .llm_api_client import llm_to_dtype

def infer_and_convert_data_types(df):
    """
    Covert df to appropriate data types

    Parameters:
        - df
    
    Returns: 
        - df
    """
    print(df.columns[0])
    # Check for header
    if isinstance(df.columns[0], str):
        # if header then give it to gemini with three first rows
        # and then convert columns to suggested datatypes
        
        dtypes = llm_to_dtype(df.head(3))
        print(f'dtypes are: {dtypes}')
        df = convert_to_dtype(dtypes, df)
    
        return df

    # code runs if .csv file comes without header.

    for col in df.columns:

        # Attempt to convert to numeric first
        df_converted = pd.to_numeric(df[col], errors='coerce')
        if not df_converted.isna().all():  # If at least one value is numeric
            df[col] = df_converted
            continue

        # Attempt to convert to datetime
        try:
            df[col] = pd.to_datetime(df[col])
            continue
        except (ValueError, TypeError):
            pass

        # Check if the column should be categorical
        if len(df[col].unique()) / len(df[col]) < 0.5:  # Example threshold for categorization
            df[col] = pd.Categorical(df[col])

        

    return df

def convert_to_dtype(dtypes, df):
    """
    Input:
        - List of dtypes specified
        - Dataframe
    
    Return:
        - Dataframe with updated dtypes
    """


    conversion_functions = {
        'int': lambda col: convert_to_int(col, downcast='signed'),
        'float': lambda col: convert_to_float(col, downcast='float'),
        'datetime64': convert_to_datetime, 
        'category': convert_to_category,
        'bool': convert_to_bool,
        'complex': convert_to_complex,
        'timedelta': convert_to_timedelta,
        'object': convert_to_object
    }

    for i, col in enumerate(df.columns):
        for dtype, conversion_func in conversion_functions.items():
            if i >= len(dtypes):
                break
            if dtypes[i].startswith(dtype):
                df[col] = conversion_func(df[col])
                break
    
    return df


def convert_to_int(col, downcast=None):
    """
    Converting column to integers
    """
    try:
        col = pd.to_numeric(col, downcast=downcast, errors="coerce")
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to integer: {e}")
    return col

def convert_to_float(col, downcast=None):
    """
    Converting column to floats
    """
    try:
        col = pd.to_numeric(col, downcast=downcast)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to float: {e}")
    return col

def convert_to_category(col):
    """
    Converting column to category
    """
    try:
        col = pd.Categorical(col)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to categorical: {e}")
    return col
    
def convert_to_bool(col):
    """
    Converting column to booleans
    """
    try:
        col = col.astype('bool')
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to bool: {e}")
    return col
    
def convert_to_complex(col):
    try:
        col = col.astype('complex')
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to complex numnbers: {e}")
    return col

def convert_to_timedelta(col):
    """
    Converting column to timedelta
    """
    try:
        col = pd.to_timedelta(col)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to timedelta: {e}")
    return col

def convert_to_object(col):
    """
    Converting column to object
    """
    try:
        col = col.astype(object)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to object: {e}")
    return col

def convert_to_datetime(col):
    """
    Converting column to dateetime
    """
    try:
        col = pd.to_datetime(col)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to datetime: {e}")
    return col


if __name__ == "__main__":
    # Test the function with your DataFrame
    #df = pd.read_csv('../uploads/sample_data.csv')
    df = pd.read_csv('../uploads/example2.csv')
    #print("Data types before inference:")
    #print(df.dtypes)

    df = infer_and_convert_data_types(df)

   # print("\nData types after inference:")
   # print(df.dtypes)
