"""Home page shown when the user enters the application"""
import streamlit as st
import awesome_streamlit as ast

def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        st.write(
            """
            Welcome to Cape Cod Tech Council App  
            __Purpose:__ To easily view, merge, and manipulate Cape Cod Tech Council's membership data

            ## Contents

            ### Membership Expiration 
              * Easily find members about to expire
              * Membership file should be saved as `members_update_date.csv` with date as `day_month_year`  
                * i.e.: `members_9_16_21.csv`  
              * Upload File
              * Select maximum expiration date
            """
        )