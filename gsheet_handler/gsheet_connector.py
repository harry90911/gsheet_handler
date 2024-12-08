import gspread
import pandas as pd
from .oauth_client import authenticate_google_client

def connect_to_gsheet():
    """Connect to Google Sheets using authenticated credentials."""
    creds = authenticate_google_client()
    client = gspread.authorize(creds)
    return client

def download_data_as_dataframe(spreadsheet_id, sheet_range):
    """
    Download data from Google Sheets and return it as a Pandas DataFrame.
    
    Args:
        spreadsheet_id (str): The ID of the Google Spreadsheet.
        sheet_range (str): The range of the sheet to fetch (e.g., "Sheet1!A1:D10").
    
    Returns:
        pd.DataFrame: The fetched data as a Pandas DataFrame.
    """
    client = connect_to_gsheet()
    sheet = client.open_by_key(spreadsheet_id)
    worksheet = sheet.values_get(sheet_range)
    
    # 解析資料
    values = worksheet.get("values", [])
    if not values:
        raise ValueError("No data found in the specified range.")
    
    # 第一行作為列名，後續作為資料
    df = pd.DataFrame(values[1:], columns=values[0])
    return df
