# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:43:13 2025

@author: Vitalis Mbayo @ UJ

#############################
"""
import streamlit as st
st.write("Hello, Streamlit, You are awesome!")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")
st.title("VITALIS")
st.write("Hello World")
st.write("CSS2025")
st.title("my time")


# My Plot of data

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)

import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Dr. Vitalis Mbayo"
field = "Computational Chemist"
institution = "University of Johannesburg"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")

# Streamlit Title
st.title("Feature Distribution Analysis")
# File Upload
uploaded_file = st.file_uploader("Upload a CSV dataset", type=["csv"])
if uploaded_file is not None:
    # Load DataFrame
    df = pd.read_csv(uploaded_file)
    # Display Data
    st.subheader("Dataset Overview")
    st.dataframe(df.head())
    # Select numerical columns
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if num_cols:
        st.subheader("Feature Distributions")
        for col in num_cols:
            st.subheader(f"Distribution of {col}")
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.histplot(df[col], kde=True, bins=30, ax=ax)
            st.pyplot(fig)
    else:
        st.warning("No numerical columns found in the dataset.")
else:
    st.info("Please upload a CSV file to proceed.")
st.title("#FLAG#############")