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

## Option 1: Script to collect video data
First make sure you have a way to run Jupyter Notebook files, the easier option is to use Google Colab.  
Upload the intended Jupyter File to your Colab and then run all (there is a button for that option)  
You will be asked for a video ID (which you can find in the URL, after the **watch?v=**) and for a YouTube API Key, which you can create in [Google Cloud Console](https://console.cloud.google.com)  
Finally after giving the correct information and waiting for a couple time (about 1 second or less for each 100 comments) you can expect to see a file called **youtube_comments.csv**  

## Option 2: Dashboard
To run the dashboard open a terminal in the root folder (DGO-2025).  
Than type the following command:  
```bash
streamlit run app.py
```

## 📁 Folder structure

```bash
src/
├── app_pages/              # Folder containing all the dashboard pages
├── collectores/            # Scripts to collect video data
├── mocks/                  # Contains the data we colected and used on our article
└── app.py                  # Acts as the router and also the execution entry point
```
