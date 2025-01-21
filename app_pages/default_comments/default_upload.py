import streamlit as st
import pandas as pd

def default_upload():
    DEFAULT_PATHS = {
        "CNN": "mocks/general/CNN_Geral.csv",
        "FolhaSP": "mocks/general/FolhaSP_Geral.csv",
        "Itatiaia": "mocks/general/Itatiaia_Geral.csv",
        "Poder360": "mocks/general/Poder360_Geral.csv",
        "UOL": "mocks/general/UOL_Geral.csv"
    }

    if "default_csv_files" not in st.session_state:
        st.session_state.default_csv_files = {}

    st.title('Csv Files Handler')

    if st.button('Upload default'):
        for name, path in DEFAULT_PATHS.items():
            try:
                st.session_state.default_csv_files[name] = pd.read_csv(path, delimiter=';')
            except Exception:
                pass
    
    default_files = st.file_uploader('Dump default csv files here', type='csv', accept_multiple_files =True)
    if default_files:
        for file in default_files:
            st.session_state.default_csv_files[file.name] = pd.read_csv(file, delimiter=';')

    if st.session_state.default_csv_files:
        file_name = st.selectbox('Uploaded archieves', st.session_state.default_csv_files.keys())
        st.dataframe(st.session_state.default_csv_files[file_name])

        if(st.button('Remove file')):
            del st.session_state.default_csv_files[file_name]
    
    else:
        st.info('No csv archieve')