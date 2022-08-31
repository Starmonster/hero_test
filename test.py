import streamlit as st
import pandas as pd


def main():

    user_num = st.number_input("enter a number between 0 and 100", min_value=0, max_value=100)

    st.title(f"User entered {user_num}")


if __name__ == "__main__":
    main()
