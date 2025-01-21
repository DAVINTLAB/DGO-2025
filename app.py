from app_pages import landing_page
from app_pages.analyzed_comments.categories import categories_page
from app_pages.analyzed_comments.analyzed_upload import analyzed_upload
from app_pages.analyzed_comments.individual_files import individual_analysis_page
from app_pages.default_comments.default_upload import default_upload
from app_pages.default_comments.general_visualization import general_visualization_page
from app_pages.default_comments.users_dashboard import users_dashboard_page
import streamlit as st

st.set_page_config(
    page_title='Views',
    page_icon='📊',
    layout='wide',
    menu_items={'Get Help': None, 'Report a Bug': None, 'About': None}
)

main_section = st.sidebar.selectbox('Main Section', ['Analyzed Comments', 'Default Comments'])

sub_section = ''

if(main_section == 'Analyzed Comments'):
    sub_section = st.sidebar.selectbox('Sub Section', ['Upload File', 'Categories', 'Individual Analysis'])
    match sub_section:
        case 'Upload File':
            analyzed_upload()
        case 'Categories':
            categories_page()
        case 'Individual Analysis':
            individual_analysis_page()
        case _:
            landing_page()



elif(main_section == 'Default Comments'):
    sub_section = st.sidebar.selectbox('Sub Section', ['Upload File', 'General Visualization', 'Users Dashboard'])
    match sub_section:
        case 'Upload File':
            default_upload()
        case 'General Visualization':
            general_visualization_page()
        case 'Users Dashboard':
            users_dashboard_page()
        case _:
            landing_page()

else:
    landing_page()
