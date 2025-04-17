# How to run
# 🚀 Streamlit + Python

This is a dashboard using [Streamlit](https://streamlit.io/) to easily build an interactive data visualization tool, along with [pip](https://pip.pypa.io/en/stable/) as package manager.

## 📦 Technologies

- [Streamlit](https://streamlit.io/) 
- [pip](https://pip.pypa.io/en/stable/)
- [Python](https://www.python.org/)

## ▶️ Setup to run locally

1. **Clone the repository**

```bash
git clone https://github.com/DAVINTLAB/DGO-2025.git
cd DGO-2025
```

Create a separate environment and install dependancies
(May vary depending on OS, but something like this will work)

```bash
python -m venv dgo-env
source dgo-env/bin/activate
pip install -r requirements.txt
```



2. **Decide which feature you want to run**

Option 1 -> Script to collect video data

Option 2 -> Dashboard

## 📁 Folder structure


```bash
src/
├── app_pages/              # Folder containing all the dashboard pages
├── collectores/            # Scripts to collect video data
├── mocks/                  # Contains the data we colected and used on our article
└── app.py                  # Acts as the router and also the execution entry point
```
