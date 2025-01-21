import streamlit as st
import plotly.graph_objects as go

def show_general_stats_graph(file_name, classification_col):
    data = st.session_state.analyzed_csv_files[file_name]

    counts = data[classification_col].value_counts()
    classifications = counts.index
    values = counts.values

    fig = go.Figure(
        data=[go.Pie(
            labels=classifications,
            values=values,
            hole=0
        )]
    )

    fig.update_layout(
        title=f"Distribution of Classifications in {file_name}",
    )

    st.plotly_chart(fig)

def show_support_graph(file_name):
    data = st.session_state.analyzed_csv_files[file_name]

    support_data = data[data["Viés político suporte"].notnull()]

    if support_data.empty:
        st.warning("No 'Support' data found.")
        return
        
    support_col = "Viés político suporte"

    support_counts = support_data[support_col].value_counts()
    support_categories = support_counts.index
    support_values = support_counts.values

    fig = go.Figure(
        data=[go.Pie(
            labels=support_categories,
            values=support_values,
            hole=0  # Ajuste para estilo donut, se preferir
        )]
    )
        
    fig.update_layout(
        title=f"Support Distribution in {file_name}",
    )

    st.plotly_chart(fig)

def show_critics_graph(file_name):
    data = st.session_state.analyzed_csv_files[file_name]

    critics_data = data[data["Viés político Crítica e Protesto"].notnull()]

    if critics_data.empty:
        st.warning("No 'Critics' data found.")
        return
        
    critics_col = "Viés político Crítica e Protesto"

    critics_counts = critics_data[critics_col].value_counts()
    critics_categories = critics_counts.index
    critics_values = critics_counts.values

    fig = go.Figure(
        data=[go.Pie(
            labels=critics_categories,
            values=critics_values,
            hole=0
        )]
    )
        
    fig.update_layout(
        title=f"Critics Distribution in {file_name}",
    )

    st.plotly_chart(fig)