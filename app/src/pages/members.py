import streamlit as st
import pandas as pd
import datetime as dt
from cctc import clean_members, format, clean_infra

import awesome_streamlit as ast

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        st.sidebar.title("Input Data")

        st.sidebar.markdown("Import Members CSV")
        uploaded_file = st.sidebar.file_uploader("Choose a file")

        expire_date = pd.to_datetime(st.sidebar.date_input('Pick a Expiration Date')).strftime(format)
        result =""

        if uploaded_file is not None:
            members = pd.read_csv(uploaded_file)
            members = clean_members(members)
            members_filtered = members[members['Membership Expiration Date'] <= expire_date]

            st.table(members_filtered)