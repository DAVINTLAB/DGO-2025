import streamlit as st
import pandas as pd

def users_dashboard_page():
    st.title('Users Dashboard')
    option = st.selectbox('Options', ['Top authors', 'Top authors by video', 'Top authors in different videos'])
    
    if(option == 'Top authors'):
        amount = st.slider('Amount of authors', 1, 100, 10)

        if "default_csv_files" not in st.session_state or not st.session_state.default_csv_files:
            st.warning('No data uploaded, please upload some data before checking this page')
            return
        
        csv_files = st.session_state['default_csv_files']

        full_data = pd.DataFrame()
        
        for file_name, data in csv_files.items():
            data['source'] = file_name
            full_data = pd.concat([full_data, data])

        if 'author' in full_data.columns:
            authors = full_data['author'].value_counts()
            top_authors = authors.head(amount)

            for author in top_authors.index:
                with st.expander(f'{author} - {len(full_data[full_data["author"] == author])} comments'):
                    author_data = full_data[full_data['author'] == author].drop(columns=['author']).reset_index(drop=True)
                    st.write(f'Comments from {author}')
                    st.write(author_data.to_html(index=False), unsafe_allow_html=True)
    
    elif(option == 'Top authors by video'):
        amount = st.slider('Amount of authors', 1, 100, 10)

        selected_video = st.selectbox('Select video', list(st.session_state['default_csv_files'].keys()))
        csv_files = st.session_state['default_csv_files']
        data = csv_files[selected_video]

        if 'author' in data.columns:
            authors = data['author'].value_counts()
            top_authors = authors.head(10)

            for author in top_authors.index:
                with st.expander(f'{author} - {len(data[data["author"] == author])} comments'):
                    author_data = data[data['author'] == author].drop(columns=['author']).reset_index(drop=True)
                    st.write(f'Comments from {author}')
                    st.write(author_data.to_html(index=False), unsafe_allow_html=True)

    elif(option == 'Top authors in different videos'):
        amount = st.slider('Amount of authors', 1, 100, 10)

        if "default_csv_files" not in st.session_state or not st.session_state.default_csv_files:
            st.warning('No data uploaded, please upload some data before checking this page')
            return
        
        csv_files = st.session_state['default_csv_files']

        author_counts = {}

        for file_name, data in csv_files.items():
            if 'author' in data.columns:
                for author in data['author'].dropna().unique():
                    if author not in author_counts:
                        author_counts[author] = 0
                    author_counts[author] += 1

        top_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:amount]

        for author, count in top_authors:
            with st.expander(f'{author} - {count} videos'):
                for file_name, data in csv_files.items():
                    if 'author' in data.columns:
                        author_data = data[data['author'] == author].drop(columns=['author']).reset_index(drop=True)
                        if len(author_data) > 0:
                            st.write(f'Comments from {author} in {file_name}')
                            st.write(author_data.to_html(index=False), unsafe_allow_html=True)
