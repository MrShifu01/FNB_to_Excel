import pandas as pd

def preprocess_dataframe(excel_file_path):
    df = pd.read_excel(excel_file_path)
    # Delete the rows of index 0-5
    df.drop(index=range(0, 5), inplace=True)

    # Set the first row as the header
    df.columns = df.iloc[0]
    # Drop the first row since it's now the header
    df = df.drop(df.index[0])
    # Optionally, reset the index if you want
    df.reset_index(drop=True, inplace=True)

    df.columns = df.columns.str.replace(' ', '')


    # Create columns and rearrange them as per instructions
    df.drop(columns=df.columns[2], inplace=True)
    df['temp'] = df['Amount']
    df.drop(columns='Amount', inplace=True)
    df['Amount'] = df['temp']
    df.drop(columns='temp', inplace=True)


    df.insert(0, 'Account', 'FNB')
    df.insert(2, 'Year', '')
    df.insert(3, 'Adj Month', '')
    df.insert(5, 'Category', '')
    df.insert(6, 'Selection', '')
    df.insert(7, 'Details', '')

    df = df.applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x)

    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

    # Convert the 'Date' column to datetime format if it isn't already
    df['Date'] = pd.to_datetime(df['Date'])


    # Extract the year and create the 'Year' column
    df['Year'] = df['Date'].dt.year
    # Create the 'Adj Month' column
    df['Adj Month'] = df['Date'].dt.month.astype(
        str) + "-" + df['Date'].dt.year.astype(str)

    return df
