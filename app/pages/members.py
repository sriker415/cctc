import pandas as pd
import datetime as dt
import streamlit as st
import awesome_streamlit as ast

from cctc import create_download

from cctc import clean_members, format, get_update

def write():
    """
    Used to write the page in the app.py file
    """
    with st.spinner("Loading Home ..."):
        st.sidebar.title("Input Data")

        st.sidebar.markdown("Import Members CSV")
        uploaded_file = st.sidebar.file_uploader("Choose a file")

        expire_date = pd.to_datetime(st.sidebar.date_input('Pick a Expiration Date')).strftime(format)
        result =""
        
        if uploaded_file is not None:
            members = pd.read_csv(uploaded_file)
            file_date = get_update(uploaded_file)
            members = clean_members(members, file_date)
            members_filtered = members[members['Membership Expiration Date'] <= expire_date]

            href = create_download(members_filtered, 'members_filtered')
            st.markdown(href, unsafe_allow_html=True)

            st.table(members_filtered)