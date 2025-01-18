import streamlit as st
import pandas as pd

def analyzed_upload():    
    if "analyzed_csv_files" not in st.session_state:
        st.session_state.analyzed_csv_files = {}

    st.title('Csv Files Handler')

    #Upload
    analyzed_files = st.file_uploader('Dump analyzed csv files here', type='csv', accept_multiple_files =True)
    if analyzed_files:
        for file in analyzed_files:
            st.session_state.analyzed_csv_files[file.name] = pd.read_csv(file)
    
    #List and handle changes for uploaded archieves
    if st.session_state.analyzed_csv_files:
        file_name = st.selectbox('Uploaded archieves', st.session_state.analyzed_csv_files.keys())
        st.dataframe(st.session_state.analyzed_csv_files[file_name])

        if(st.button('Remove file')):
            del st.session_state[file_name]
            st.experimental_rerun()
    
    else:
        st.info('No csv archieve')