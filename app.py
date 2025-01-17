from pages import landing_page
import streamlit as st

st.set_page_config(
    page_title='Views',
    page_icon='📊',
    layout='wide'
)

main_section = st.sidebar.selectbox('Main Section', ['Analyzed Comments', 'Default Comments'])

sub_section = ''

if(main_section == 'Analyzed Comments'):
    sub_section = st.sidebar.selectbox('Sub Section', ['Upload File'])
    match sub_section:
        case 'Upload File':
            pass



elif(main_section == 'Default Comments'):
    sub_section = st.sidebar.selectbox('Sub Section', ['Upload File'])
    match sub_section:
        case 'Upload File':
            pass

else:
    landing_page()
