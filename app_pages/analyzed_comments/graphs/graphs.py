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

def show_support_graph(file_name, classification_col):
    data = st.session_state.analyzed_csv_files[file_name]

    support_data = data[data[classification_col] == "Suporte"]
    print(support_data)

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