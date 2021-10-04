import pandas as pd
import base64
from pathlib import Path

format = "%Y-%m-%d"

def clean_dates(df, column):
    df[column] = pd.to_datetime(df[column]).dt.strftime(format)
    return(df[column])

def get_update(file_name):
    file_name = str(file_name)
    mth, day, year = [int(s) for s in file_name.replace("_", " ").replace(".", " ").split() if s.isdigit()]
    file_date = str(2000 + year) + '-' + str(mth) + '-' + str(day)
    return file_date

def clean_members(df, file_date):
    df['update_date'] = file_date
    df['Membership Start Date'] = clean_dates(df, 'Membership Start Date')
    df['Membership Enrollment Date'] = clean_dates(df, 'Membership Enrollment Date')
    df['Membership Expiration Date'] = clean_dates(df, 'Membership Expiration Date')
    df = df.rename({'Email': 'Member Email'}, axis = 1)
    df['Member Email'] = df['Member Email'].str.lower()

    return df

def clean_infra(df):
    #get first/last name from full name
    df[['First Name', 'Last Name']] = df['Full Name (F)'].str.split(" ", 1, expand=True)
    #get attendee number
    df['Attendee Number'] = df['Attendee Detail'].str.split().str[-1].str.replace("#", "").str.replace(")", "", regex=True)
    df['Member Email'] = df['Email 1'].str.lower()

def create_download(df, filename):
    """
    Download dataframe as a CSV file and name file based on plan quarter, year, and department 
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f"""<a style='display: block; text-align: right;' href="data:file/csv;base64,{b64}" download="{filename}.csv">Download Members</a>"""
    return href 

