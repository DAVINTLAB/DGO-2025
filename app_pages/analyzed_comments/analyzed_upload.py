import streamlit as st
import pandas as pd

def analyzed_upload():
    DEFAULT_PATHS = {
        "CNN": "mocks/analyzed/CNN_#Desempate.csv",
        "FolhaSP": "mocks/analyzed/FolhaSP_#Desempate.csv",
        "Itatiaia": "mocks/analyzed/Itatiaia_#Desempate.csv",
        "Poder360": "mocks/analyzed/Poder360_#Desempate.csv",
        "UOL": "mocks/analyzed/UOL_#Desempate.csv"
    }

    if "analyzed_csv_files" not in st.session_state:
        st.session_state.analyzed_csv_files = {}

    st.title('Csv Files Handler')

    if st.button('Upload default'):
        for name, path in DEFAULT_PATHS.items():
            try:
                st.session_state.analyzed_csv_files[name] = pd.read_csv(path, delimiter=';')
            except Exception:
                pass

    #Upload
    analyzed_files = st.file_uploader('Dump analyzed csv files here', type='csv', accept_multiple_files =True)
    if analyzed_files:
        for file in analyzed_files:
            st.session_state.analyzed_csv_files[file.name] = pd.read_csv(file, delimiter=';')
    
    #List and handle changes for uploaded archieves
    if st.session_state.analyzed_csv_files:
        file_name = st.selectbox('Uploaded archieves', st.session_state.analyzed_csv_files.keys())
        st.dataframe(st.session_state.analyzed_csv_files[file_name])

        if(st.button('Remove file')):
            del st.session_state.analyzed_csv_files[file_name]
    
    else:
        st.info('No csv archieve')