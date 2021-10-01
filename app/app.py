import streamlit as st
import pandas as pd
import datetime as dt
from cctc import clean_members, format, clean_infra

st.set_page_config(
        page_title="Cape Cod Tech Council",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )

st.title("Cape Cod Tech Council")

text_input_container = st.empty()
pwd = text_input_container.text_input("Enter a password", type="password")

if pwd == st.secrets["password"]:
    text_input_container.empty()

    # Create a page dropdown 
    # page = st.sidebar.selectbox("Menu", ["Home", "Membership"]) 
    # if page == "Home":
    #     st.markdown("Welcome")

    # elif page == "Membership":
        
    def main():
        st.sidebar.title("Input Data")

        st.sidebar.markdown("Import Members CSV")
        uploaded_file = st.sidebar.file_uploader("Choose a file")

        # st.sidebar.markdown("Import Group CSV")
        # uploaded_file2 = st.sidebar.file_uploader("Choose aother file")

        # st.sidebar.markdown("Import Infrastructure CSV")
        # uploaded_file3 = st.sidebar.file_uploader("Choose a third file")

        expire_date = pd.to_datetime(st.sidebar.date_input('Pick a Expiration Date')).strftime(format)
        result =""

        if uploaded_file is not None:
            members = pd.read_csv(uploaded_file)
            members = clean_members(members)
            members_filtered = members[members['Membership Expiration Date'] <= expire_date]

            st.table(members_filtered)
    
    if __name__=='__main__': 
        main()
    

elif len(pwd) > 0:
    st.markdown("Wrong Password, try again")