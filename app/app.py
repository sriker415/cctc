import streamlit as st
import pandas as pd
import datetime as dt
from cctc import clean_members, format, clean_infra, password

st.set_page_config(layout="wide")

st.title("Cape Cod Tech Council")

text_input_container = st.empty()
pwd = text_input_container.text_input("Enter a password", type="password")

if pwd == password:
    text_input_container.empty()

    # Create a page dropdown 
    # page = st.sidebar.selectbox("Menu", ["Home", "Membership"]) 
    # if page == "Home":
    #     st.markdown("Welcome")

    # elif page == "Membership":
        
    def main():
        st.sidebar.title("Input Parameteres")
        expire_date = pd.to_datetime(st.sidebar.date_input('Pick a Expiration Date')).strftime(format)
        result =""
        
        st.markdown("Import Members CSV")
        uploaded_file = st.file_uploader("Choose a file")

        if uploaded_file is not None:
            members = pd.read_csv(uploaded_file)
            members = clean_members(members)
            members_filtered = members[members['Membership Expiration Date'] <= expire_date]

            st.table(members_filtered)
    
    if __name__=='__main__': 
        main()
    

elif len(pwd) > 0:
    st.markdown("Wrong Password, try again")