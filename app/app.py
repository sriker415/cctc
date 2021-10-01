import streamlit as st

import awesome_streamlit as ast

import src.pages.home
import src.pages.members

st.set_page_config(
        page_title="Cape Cod Tech Council",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )

st.title("Cape Cod Tech Council")

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": src.pages.home,
    "Membership": src.pages.members
}

text_input_container = st.empty()
pwd = text_input_container.text_input("Enter a password", type="password")

if pwd == st.secrets["password"]:
    text_input_container.empty()
    def main():
        """Main function of the App"""
        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", list(PAGES.keys()))

        page = PAGES[selection]

        with st.spinner(f"Loading {selection} ..."):
            ast.shared.components.write_page(page)

    if __name__ == "__main__":
        main()

elif len(pwd) > 0:
    st.markdown("Wrong Password, try again")