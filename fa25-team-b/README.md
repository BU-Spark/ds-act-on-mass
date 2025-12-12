
<h1 align="center">
  <br>
  <a href="https://www.bu.edu/spark/" target="_blank"><img src="https://www.bu.edu/spark/files/2023/08/logo.png" alt="BUSpark" width="200"></a>
  <br>
  ACTonMass Legislative Vote Tracker
  <br>
</h1>

<h4 align="center">A tool to collect, process, and visualize legislative voting data in Massachusetts.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#project-description">Project Description</a> •
  <a href="#data-locations">Data Locations</a>
</p>

## Overview

The ACTonMass Legislative Vote Tracker is designed to collect, clean, and analyze legislative roll call voting data for the Massachusetts House and Senate. The goal is to produce a unified dataset that powers interactive Looker Studio dashboards, enabling deeper transparency into how legislators vote, how often they miss votes, and how voting patterns evolve across legislative sessions.

This project transforms raw legislative records, including PDFs, roll call tables, and legislator information, into structured, analysis-ready tables. These tables support public-facing accountability tools that allow users to explore legislators, bills, committees, and voting trends.

## Goal

The primary objective of this project is to build a reproducible data pipeline that:
* Automates the ingestion of legislative data from authoritative sources
* Standardizes and integrates House and Senate roll call information
* Categorizes bills by committee topic
* Produces clean datasets usable in Looker Studio visualizations

With these outputs, we enable ACTonMass and the public to answer questions such as:

* How does each legislator vote across different topics?
* Which legislators miss the most votes?
* What trends exist across legislative sessions?
* How are roll call numbers connected to specific bills, amendments, or committees?

This work helps support legislative transparency and empowers organizations to track voter accountability effectively.

## Key Features

Full Legislative Data Pipeline
* A modular pipeline that gathers, parses, cleans, and integrates voting datasets from the Massachusetts Legislature.

Topic & Committee Categorization
* Bill and committee data are aligned to create topic categories for interactive filtering in Looker Studio dashboards.

Senate & House Roll Call Extraction
* Automated scraping of Senate data and PDF extraction/parsing of House roll call PDFs.

Looker Studio–Ready Outputs
* All output tables are cleaned, standardized, and formatted to be directly uploaded into Looker Studio dashboards.

## Datasets

Official roll call data for the Senate and House, accessed through:

Massachusetts Legislature Website:
* PDF documents containing House and Senate roll call information
* Legislator names, bill and amendment numbers, and vote type
* Unstructured and unlinked, inconsistently formatted over the years

Massachusetts Legislature Public API:
* Contains vote records, bill data, committee assignments
* Data often incomplete, inconsistent, or duplicated


### Project Data Storage

Due to file size restrictions:
* Final datasets are stored in the ACT on Mass Team B Google Drive
* Working data is stored locally or within private branches when running the pipeline (team-b-eda branch)

## Quick Start 
### Requirements.txt Instructions

To ensure all necessary libraries are installed, follow these steps:

1. Create a virtual environment (optional but recommended):
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  pip install --upgrade pip
  ```

2. Install the required libraries:
  ```bash
  pip install -r requirements.txt
  ```

3. The `requirements.txt` file should include the following libraries:
  ```
requests
pandas
numpy
openpyxl
ast
time
bs4
pdfplumber
glob
traceback
random
urllib
jupyter 
  ```

## Repository Structure 

### 1. EDA/
Purpose:
Exploratory and testing notebooks used during the initial development of the pipeline.

* /bill_exploration.ipynb - This imports committee data and topic categorization
  - This is there to compare a bill and their committee that wrote the bill to create a topic for which we can categorize our data with.
* The EDA Folder contains most of our testings scripts.
  - These are mainly as testing for what was needed.

### 2. dataImport/

Our code will generate different files of data organized into tables to be sent into a looker studio report/

* /dataImport - Contains all of the scripts needed to get the data information that we have in our looker.
##### Main Senate data collection method
* /dataImport/all_senate_data_import.ipynb
  - This imports the Senate's data and organizes it to fit the formatting needed
  - This has a way to import one general court (year) for all Senate data
  - It also generally imports bills and checks for roll calls though that is limited to only the Senate.
##### House data collection method - version 1
* /dataImport/Full_House_RollCall_scraper.ipynb
  - Gets the PDFs from the malegislature website to be able to get the roll call data for the House
* /dataImport/parse_house_rollcall_data.ipynb
  - This parses through the data gathered from Full_House_RollCall_scraper.ipynb to be able to get it in a readable format
* /dataImport/house_legislators_scraper.ipynb
  - This works through the data obtained by the parse_house_rollcall_data.ipynb file and adds the legislator data to it for the final data prep.
##### House data collection method - version 2 (for Looker dataset）
* /dataImport/house_pdf_collection.ipynb
  - Get all PDF files containing roll call records
* /dataImport/house_data_import.ipynb
  - Extract roll call information from PDFs (2003-2008, 2018-2025)
* /dataImport/house_2009_2017.ipynb
  - Extract roll call information from PDFs (2009-2017)
* /dataImport/legislator_info_merge.ipynb
  - Combining legislator information with roll-call voting
  
### 3. Data Outputs

Where the final datasets live:

* ACT on Mass Team B Google Drive (due to file size)
* Some test subsets exist in the repository’s team-b-eda branch
* The cleaned datasets include 2 main datasets: one for senate and one for house data

## **How to Use**

Reproducing the full dataset will take some time, as the pipeline processes both Senate and House legislative records. The main data files used for Looker Studio are generated through the notebooks located in the `dataImport` folder.

Follow the steps below **in order**:


### **1. Senate Data Import**

Run:

```
dataImport/all_senate_data_import.ipynb
```

This notebook downloads, extracts, and structures all Senate roll call data.


### **2. Scrape House Roll Call PDFs**

Run:

```
dataImport/Full_House_RollCall_scraper.ipynb
```

This script collects House roll call PDFs (single-page and combined files) from the Legislature website.


### **3. Parse House Roll Call PDFs**

Run:

```
dataImport/parse_house_rollcall_data.ipynb
```

This notebook extracts vote tables, metadata, and bill information from the scraped PDFs.


### **4. Add Legislator Data**

Run:

```
dataImport/house_legislators_scraper.ipynb
```

This adds House legislator names, districts, and metadata into the structured dataset.


### **5. Upload Final Tables to Looker Studio**

Once all scripts have been executed, the final processed datasets can be uploaded directly into **Looker Studio** to power interactive dashboards.

### **6. House Dataset Quick-Run Option**

For generating the House dataset specifically for Looker, you may simply run the following notebooks in order:

1. `dataImport/house_pdf_collection.ipynb`
2. `dataImport/house_data_import.ipynb`
3. `dataImport/house_2009_2017.ipynb`
4. `dataImport/legislator_info_merge.ipynb`
   
## Tools and Platforms 

* Processing: pandas, numpy, BeautifulSoup, PyPDF2
* Visualization: Google Looker Studio
* Environment: Jupyter Notebooks
* Storage: Google Drive (ACT ON MASS Team B Shared Folder)

## Challenges 

1. House PDF Complexity
The House publishes roll calls only as PDFs → requiring advanced text parsing and manual edge-case handling.

2. Inconsistent Formats
Senate vs. House data structures vary significantly and must be standardized.

3. Large Data Volume
Full sessions contain thousands of PDFs and roll calls, leading to long processing time and large output files.

## Recommendation for next steps 

* Complete data gaps: Fill remaining missing legislator names for full accountability coverage
* Enable public access: Deploy dashboard for Massachusetts voters to track representatives before elections
* Expand functionality: Add real-time updates, bill text integration, and Act on Mass priority issue tracking
