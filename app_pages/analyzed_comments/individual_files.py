from app_pages.analyzed_comments.graphs.graphs import show_general_stats_graph, show_support_graph
import streamlit as st

def individual_analysis_page():
    st.title('Individual analysis page')

    if "analyzed_csv_files" not in st.session_state or not st.session_state.analyzed_csv_files:
        st.warning('No data uploaded, please upload some data before checking this page')
        return
    
    file_name = st.selectbox('Uploaded archieves', st.session_state.analyzed_csv_files.keys())

    classification_col = ['Desempate']

    if file_name:
        show_general_stats_graph(file_name, classification_col)
        show_support_graph(file_name, classification_col)

        

    
    