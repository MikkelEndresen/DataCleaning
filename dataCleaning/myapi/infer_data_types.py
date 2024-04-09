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
        # if header give it to gemini with three first rows
        # and then onvert columns to suggested datatypes
        
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

    for i, col in enumerate(df.columns):

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
                if dtypes[i].startswith(dtype):
                    conversion_func(df[col])
                    break



        # if i > len(dtypes) -1: # for when LLM does not return enough dtypes. 
        #     break
        # if dtypes[i][:3] == 'int':
        #     #df[col] = df[col].astype('int64')

        #     df[col] = pd.to_numeric(df[col], downcast='signed', errors='coerce')
        #     df[col]= df[col].convert_dtypes(convert_integer = True)

        # elif dtypes[i][:5] == 'float':
        #     df[col] = df[col].astype(float)

        # elif dtypes[i] == 'datetime64':
        #     try:
        #         df[col] = pd.to_datetime(df[col])
        #         continue
        #     except (ValueError, TypeError):
        #         print(f"Warning: Failed to convert values in column '{col}' to datetime.")

        # elif dtypes[i] == 'category':
        #     df[col] = pd.Categorical(df[col])

        # elif dtypes[i] == 'bool':
        #     df[col] = df[col].astype('bool')

        # elif dtypes[i] == 'complex':
        #     try:
        #         df[col] = df[col].astype('complex')
        #         continue
        #     except (ValueError, TypeError):
        #         print(f"Warning: Failed to convert values in column '{col}' to complex.")

        # elif dtypes[i] == 'timedelta':
        #     df[col] = pd.to_timedelta(df[col])

        # elif dtypes[i] == 'object':
        #     print("works")
        #     df[col] = df[col].astype(object)
    
    return df


def convert_to_int(col, downcast=None):
    """
    Converting column to integers
    """
    try:
        col = pd.to_numeric(col, downcast=downcast, errors="coerce")
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to integer: {e}")

def convert_to_float(col, downcast=None):
    """
    Converting column to floats
    """
    try:
        col = pd.to_numeric(col, downcast=downcast)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to float: {e}")

def convert_to_category(col):
    """
    Converting column to category
    """
    try:
        col = pd.Categorical(col)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to categorical: {e}")
    
def convert_to_bool(col):
    """
    Converting column to booleans
    """
    try:
        col = col.astype('bool')
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to bool: {e}")
    
def convert_to_complex(col):
    try:
        col = col.astype('complex')
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to complex numnbers: {e}")

def convert_to_timedelta(col):
    """
    Converting column to timedelta
    """
    try:
        col = pd.to_timedelta(col)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to timedelta: {e}")

def convert_to_object(col):
    """
    Converting column to object
    """
    try:
        col = col.astype(object)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to object: {e}")

def convert_to_datetime(col):
    """
    Converting column to dateetime
    """
    try:
        col = pd.to_datetime(col)
    except (ValueError, TypeError) as e:
        print(f"Error converting column {col[0]} to datetime: {e}")


if __name__ == "__main__":
    # Test the function with your DataFrame
    #df = pd.read_csv('../uploads/sample_data.csv')
    df = pd.read_csv('../uploads/example2.csv')
    #print("Data types before inference:")
    #print(df.dtypes)

    df = infer_and_convert_data_types(df)

   # print("\nData types after inference:")
   # print(df.dtypes)
