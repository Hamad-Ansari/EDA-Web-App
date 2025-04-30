#libraris
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns
import pydeck as pdk
import plotly.express as px

import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Load the dataset
st.markdown('''
    # ** Exploratory Data Analysis **
    This App Developed by ** [Hammad_Zahid](https://github.com/Hamad-Ansari/Hammad.git) **,
    This is for** EDA App **
''')

# How to upload the file from pc
with st.sidebar.header("Upload your file"):
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
    st.sidebar.markdown('[Example CSV file🎈](https://www.kaggle.com/datasets/benroshan/titanic-dataset-from-kaggle)')
    st.sidebar.markdown('[Example Excel file🎈](https://www.kaggle.com/datasets/benroshan/titanic-dataset-from-kaggle)')
    st.sidebar.markdown('[Example Dataset🎈](https://www.kaggle.com/datasets/benroshan/titanic-dataset-from-kaggle)')

# Main content
if uploaded_file is not None:
    try:
        # Read file based on extension
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        
        st.header("** Input DataFrame **")
        st.write(df)
        
        st.write("** Shape of DataFrame **")
        st.write(df.shape)
        
        st.write("** Data Types of DataFrame **")
        st.write(df.dtypes)
        
        st.write("** Missing Values of DataFrame **")
        st.write(df.isnull().sum())
        
        st.write("** DataFrame Description **")
        st.write(df.describe())
        
        # Only show correlation if there are numeric columns
        numeric_df = df.select_dtypes(include=[np.number])
        if not numeric_df.empty:
            st.write("** DataFrame Correlation **")
            st.write(numeric_df.corr())
        
        st.write("** DataFrame Head **")
        st.write(df.head())
        
        # Simple visualizations (only for numeric data)
        numeric_cols = numeric_df.columns.tolist()
        if numeric_cols:
            st.line_chart(df[numeric_cols])
            st.bar_chart(df[numeric_cols])
            st.area_chart(df[numeric_cols])
        
        # Profiling report
        pr = ProfileReport(df, explorative=True)
        st.write("** Profiling Report with pandas **")
        st_profile_report(pr)
        
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

else:
    st.info("Please upload a CSV or Excel file to see the EDA report.")
    st.markdown("Or use the example datasets provided in the sidebar.")
    
    if st.button("Use Titanic Example Dataset"):
        df = sns.load_dataset("titanic")
        st.write(df)
        
        st.write("** Shape of DataFrame **")
        st.write(df.shape)
        
        st.write("** Data Types of DataFrame **")
        st.write(df.dtypes)
        
        st.write("** Missing Values of DataFrame **")
        st.write(df.isnull().sum())
        
        st.write("** DataFrame Description **")
        st.write(df.describe())
        
        # Example visualizations
        fig, ax = plt.subplots()
        ax.scatter(df['age'], df['fare'])
        ax.set_title("Age vs Fare Scatter Plot")
        st.pyplot(fig)
        
        # Plotly scatter plot
        if 'age' in df.columns and 'fare' in df.columns:
            fig = px.scatter(df, x='age', y='fare', color='survived')
            st.plotly_chart(fig)
        
        # Profiling report for example data
        pr = ProfileReport(df, explorative=True)
        st_profile_report(pr)
