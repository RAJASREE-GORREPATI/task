import streamlit as st
import pandas
st.set_page_config(layout="wide")
st.header("The Best Company")
content=""" 
A company is essentially an artificial person—also known as corporate personhood—in that it is an entity separate from the individuals who own, manage, and support its operations. 
Companies are generally organized to earn a profit from business activities, but some may be structured as nonprofit charities. 
Each country has its own hierarchy of company and corporate structures but with many similarities.
"""
st.write(content)
st.subheader("Our Team")
df = pandas.read_csv("data.csv")
col1,col2,col3=st.columns(3)
with col1:
    for index,row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/"+ row["image"])
with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
with col3:
    for index,row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])