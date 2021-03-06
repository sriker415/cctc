import streamlit as st
import awesome_streamlit as ast

import pages.home
import pages.members

st.set_page_config(
        page_title="Cape Cod Tech Council",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )

st.title("Cape Cod Tech Council")

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": pages.home,
    "Membership Expiration": pages.members
}

text_input_container = st.empty()
pwd = text_input_container.text_input("Enter the password:", type="password")

if len(pwd) == 0:
    pass
else:
    if pwd == st.secrets["password"]:
        text_input_container.empty()
        def main():
            """
            Main function of the App
            """
            st.sidebar.title("Navigation")
            selection = st.sidebar.radio("Go to", list(PAGES.keys()))

            page = PAGES[selection]

            with st.spinner(f"Loading {selection} ..."):
                ast.shared.components.write_page(page)
        if __name__ == "__main__":
            main()

    elif pwd != st.secrets["password"]:
        st.markdown("Wrong Password, try again") 