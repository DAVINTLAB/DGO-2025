import streamlit as st
import plotly.express as px
import pandas as pd

def general_visualization_page():
    st.title('General visualization page')

    if "default_csv_files" not in st.session_state or not st.session_state.default_csv_files:
        st.warning('No data uploaded, please upload some data before checking this page')
        return
    
    csv_files = st.session_state['default_csv_files']
    csv_data = {}

    for file_name, data in csv_files.items():
        csv_data[file_name] = len(data)

    result_df = pd.DataFrame({
        "Video": list(csv_data.keys()),
        "Comments count": list(csv_data.values())
    })

    fig = px.bar(result_df, x='Video', y='Comments count', title='Comments count per video')

    st.plotly_chart(fig)