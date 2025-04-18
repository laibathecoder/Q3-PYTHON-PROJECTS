# Python website in 15 mints

import streamlit as st
import pandas as pd 

st.title("Simple Data Dashboard")

upload_file = st.file_uploader("Choose a CSV file for upload" , type = "csv")

if upload_file is not None:
    data_fram = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(data_fram.head())

    st.subheader("Data Summary")
    st.write(data_fram.describe())

    st.subheader("Filter Data")
    columns = data_fram.columns.tolist()
    selected_columns = st.selectbox("Select columns to filter by" , columns)
    unique_values = data_fram[selected_columns].unique()
    select_values = st.selectbox("Select values" , unique_values)


    filter_data_fram = data_fram[data_fram[selected_columns] == select_values]
    st.write(filter_data_fram)

    st.subheader("Plot Data")
    x_columns = st.selectbox("Select x-axis columns", columns)
    y_columns = st.selectbox("Select y-axis columns", columns)

    if st.button("Generate Plot"):
        st.line_chart(filter_data_fram.set_index(x_columns)[y_columns])
else:
    st.write("Waiting on file upload...")

    



