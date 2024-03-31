import pandas as pd
from llm_api_client import llm_to_dtype

def infer_and_convert_data_types(df):
    """
    Covert df to appropriate data types

    Parameters:
        - df
    
    Returns: 
        - df
    """

    # Check for header
    if isinstance(df.columns[0], str):
        print(df.head(3))
        # if header give it to gemini and convert columns to appropriate datatypes
        dtypes = llm_to_dtype(df.head(3))

        print(f'dtypes are: {dtypes}')

        # Test
        df = str_col_to_dtype(dtypes, df)

        return df

    for col in df.columns:
        print(df[col])

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

def str_col_to_dtype(dtypes, df):
    """
    
    Return:
        - Column with correct dtype
    """
    for i, col in enumerate(df.columns):
        if dtypes[i][:3] == 'int':
            df[col] = pd.to_numeric(df[col], downcast='signed', errors='coerce')
            df[col]= df[col].convert_dtypes(convert_integer = True)
            #df[col] = df[col].astype('int32', errors='raise')
        elif dtypes[i] == 'datetime64':
            try:
                df[col] = pd.to_datetime(df[col])
                continue
            except (ValueError, TypeError):
                pass
        elif dtypes[i] == 'category':
            df[col] = pd.Categorical(df[col])
        elif dtypes[i] == 'bool':
            df[col] = df[col].astype('bool')
        elif dtypes[i] == 'complex':
            df[col] = df[col].astype('complex')
        elif dtypes[i] == 'timedelta':
            df[col] = pd.to_timedelta(df[col])
    
    return df


if __name__ == "__main__":
    # Test the function with your DataFrame
    #df = pd.read_csv('../uploads/sample_data.csv')
    df = pd.read_csv('../uploads/example2.csv')
    #print("Data types before inference:")
    #print(df.dtypes)

    df = infer_and_convert_data_types(df)

   # print("\nData types after inference:")
   # print(df.dtypes)
