🚀 Space Race Analysis: NASA vs. SpaceX Dashboard
=================================================

This project demonstrates an end-to-end data pipeline focused on the aerospace industry. It automates the extraction of data from space missions, processes orbit and performance indicators, and visualizes the insights in an interactive dashboard.

## 📌 Overview

The goal is to analyze the transition from government dominance (NASA) to commercial efficiency (SpaceX), using real data from launches, rocket types, and orbital destinations.

## 🛠️ Technology Stack

* **Language:** Python 3.x

* **Data Manipulation:** Pandas & NumPy

* **Data Consumption:** `space-launcher-api` (REST API)

* **Cloud & Storage:** Google Drive API & Google Sheets API

* **Business Intelligence:** Looker Studio

⚙️ Project Architecture (ETL)
-------------------------------

1. **Extraction:** Python script that consumes raw data from the `space-launcher-api`.

2. **Transformation:** Data cleaning, handling of missing values, and categorization of orbits (LEO, MEO, GEO, Lunar) using **Pandas**.

3. **Loading:** Automation via **Google Sheets API** to send structured data directly to a spreadsheet in the cloud.

4. **Visualization:** Native connection of **Looker Studio** to the spreadsheet for generating trend graphs, orbital heatmaps, and performance KPIs.

📊 Key Insights from the Dashboard
-----------------------------------

* **Launch Volume:** Monthly comparison between government and private providers.

* **Orbit Matrix:** Detailed visualization of which rocket dominates each mission profile (e.g., Falcon 9 in LEO vs. Saturn V in Lunar).

* **Infrastructure:** Utilization rate of the main global launch sites.

🚀 How to Run
----------------

1. Clone the repository:
   **Bash:**
   
   ```
   git clone https://github.com/marcoscunhaa/SpaceLaunchDataPipeline
   ```

2. Install the dependencies:
   **bash:**
   
   ```
   pip install -r requirements.txt
   ```

3. Configure your Google Cloud credentials (`config/credentials.json`) in the project root.

4. Create a Google Sheet and share editing power with the email credential provider.

5. Create a file named `.env` in the project root and configure the necessary environment variables:
   
   ```
   GOOGLE_CREDENTIALS_PATH=config/credentials.json
   SHEET_NAME=Space Launch Data
   ```

6. Run the main script to update the data:
   **Bash:**
   
   ```
   python main.py
   ```
   
   

-----

<p align="center">
  <img src="midia/template.gif" width="1200" alt="Demonstração do Pipeline" style="border-radius: 10px;">
</p>
