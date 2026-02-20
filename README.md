[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR-APP-URL-HERE)

# 🇸🇬 Real-Time Singapore Weather Pipeline

A professional data engineering project that demonstrates a full **ETL (Extract, Transform, Load)** workflow using real-time government data.

##  Project Overview
This pipeline automatically fetches live temperature data from the Singapore Government (NEA) Open Data API, processes the JSON response into a clean format, and hosts a live map-based dashboard.

##  Tech Stack
* **Language:** Python 3.x
* **Data Handling:** Pandas (JSON normalization & cleaning)
* **Automation:** GitHub Actions (Hourly scheduled runs)
* **Visualization:** Streamlit (Web dashboard & Geospatial mapping)

##  Key Features
* **Automated Data Fetching:** Uses a `.yml` workflow to trigger the script every hour.
* **Geospatial Mapping:** Converts API coordinates into an interactive map of Singapore.
* **Live Deployment:** Hosted on Streamlit Cloud for instant accessibility.

##  Project Structure
* `weather_fetch.py`: The main Python engine for API calls and UI.
* `.github/workflows/main.yml`: The automation script for hourly updates.
* `requirements.txt`: List of dependencies for cloud deployment.
