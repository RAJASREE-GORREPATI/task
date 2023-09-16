import streamlit as st
import pandas
st.title("The Best Company")
content=""" 
A company is essentially an artificial person—also known as corporate personhood—in that it is an entity separate from the individuals who own, manage, and support its operations. 
Companies are generally organized to earn a profit from business activities, but some may be structured as nonprofit charities. 
Each country has its own hierarchy of company and corporate structures but with many similarities.
"""
st.wrire(content)
st.header("Our Team")
df=pandas.read_csv("data.csv",sep=",")
col1,col2,col3=st.columns(3)
with col1:
    for index,row in df[:4].iterrows():
        st.write(f"{row['first name']}+{row['last name']}")
with col2:
    for index,row in df[4:8].iterrows():
        st.write(f"{row['first name']}+{row['last name']}")
with col3:
    for index,row in df[8:].iterrows():
        st.write(f"{row['first name']}+{row['last name']}")