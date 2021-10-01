import pandas as pd

format = "%Y-%m-%d"

file_date = '2021-09-16'

def clean_dates(df, column):
    df[column] = pd.to_datetime(df[column]).dt.strftime(format)
    return(df[column])

def clean_members(df):
    df['update_date'] = file_date
    df['Membership Start Date'] = clean_dates(df, 'Membership Start Date')
    df['Membership Enrollment Date'] = clean_dates(df, 'Membership Enrollment Date')
    df['Membership Expiration Date'] = clean_dates(df, 'Membership Expiration Date')
    df = df.rename({'Email': 'Member Email'}, axis = 1)

    return df

def clean_infra(df):
    #get first/last name from full name
    df[['First Name', 'Last Name']] = df['Full Name (F)'].str.split(" ", 1, expand=True)
    #get attendee number
    df['Attendee Number'] = df['Attendee Detail'].str.split().str[-1].str.replace("#", "").str.replace(")", "", regex=True)
    df['Member Email'] = df['Email 1'].str.lower()
