
<h1 align="center">
  <br>
  <a href="https://www.bu.edu/spark/" target="_blank"><img src="https://www.bu.edu/spark/files/2023/08/logo.png" alt="BUSpark" width="200"></a>
  <br>
  ACT on MASS - Team A
  <br>
</h1>

<h4 align="center">Creating a searchable Roll Call vote dataset and dashboard for MA government transparency </h4> <change to repo short description>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#project-description">Project Description</a> •
  <a href="#data-locations">Data Locations</a>
</p>

## Key Features

This project involved sourcing and processing data about Roll Call votes for both the Massachusetts House of Representatives and Senate. The steps taken for collecting, parsing, and cleaning this data can be found in the highlighted directories below.

* /data - Contains the final cleaned House and Senate Roll Call datasets, as well as supplementary .csv files containing Representative information, and Bill information which can be mapped to Roll Call votes in order to provide greater context (i.e. tracking the votes of a single representative over time, or votes on the same bill over multiple instances).
  * Currently, data is being stored in our SPARK Shared Google drive as per the request of our Technical Project Manager until we are completely done with the project and data is finalized.
* /eda/house_pdf_parsing - Contains 2 Jupyter notebooks for collecting and then parsing Roll Call votes from the House of Representatives from 2002 to 2025.
  * The House Roll Call votes are provided as a PDF transcription, in varying formats so multiple methods are defined depending on the year the PDF was created in.
  * While most PDFs could be read using a PDF text parsing library (i.e. PyMuPDF), some were stored as an embedded image and required OCR methods to extract the vote data effectively.
* /eda/senate_data_parsing_methods - Jupyter notebooks for extracting Senate Roll Call data via the [RollCalls API endpoint](https://malegislature.gov/api/swagger/index.html?url=/api/swagger/v1/swagger.json#/RollCalls) provided by the MA government.
  * The RollCalls API provides a nice mapping of Bills to Representatives to Votes, so with some work (in the notebooks contained in this directory) we created a denormalized dataset that can be easily queried to answer key questions about voting patterns dating back to 2015 (the oldest year of data available on the API)
  * For an unknown reason, the RollCalls API contained data for the Senate but not the House, resulting in the differing data collection and parsing methods.
* /processing - Contains notebooks for cleaning data collected for the Senate and House Roll Calls.
  * While the data from the Roll Call APIs was already mostly clean (only a few bill to vote mappings were missing, which were resolved), the House data contained multiple issues that needed to be fixed before the data could be used for visualization.
  * The House Roll Call data required manual matching of Representative Last Names to a unique Member Code used internally by the MA government for identifying a representative in their system (see processing/merge_house_rep_data.ipynb) as well as manual cleaning tasks for removing artifacts from the PDF parsing process (see clean_house.ipynb).
* Final Visualization - The cleaned House and Senate Roll Call vote data is presented using a [Google Looker Studio Dashboard](https://lookerstudio.google.com/u/1/reporting/afd48d3a-aad0-4cd9-94ba-6e7ea71454b5/page/qU5cF) as per the request of the client organization.
  * Currently, the data is being uploaded to Looker Studio from cleaned .csv files containing Representative, Bill, and Roll Call vote data, but is currently being shifted to a Google Cloud solution, for easier long term adoption by Act on MASS at the project's conclusion.

## How To Use

To clone and run this application, you'll need <a href="https://git-scm.com" target="_blank">Git</a>
From your command line:

```bash
# Clone this repository
$ git clone [repo link]

# Recommended: Initialize a virtual environment
python -m venv .venv

# Start the virtual environment
source .venv/bin/activate #POSIX
.venv/Scripts/activate.bat # Windows Command Prompt
.venv/Scripts/activate.ps1 # Windows PowerShell

# Install dependencies
pip install -r requirements.txt
```

Currently, all of the work for this project is contained in Jupyter Notebooks, not full Python scripts since the project focus was collection and presentation of a dataset.

Conversion of this workflow into reusable Python scripts is an endgoal of the project, but is placed after thorough completion of the clients initial request of a complete dataset of Roll Call votes for the House and Senate and an easy method to display them on the organization website.

Instructions on running the entire pipeline via Python scripts will be updated here once that point is reached.

The work can be recreated by proceeding through the Jupyter notebooks in the order indicated in the Key Features section of this README.

## Project Description

The Act on MASS project seeks to improve the transparency of Massachusetts state legislators by providing an easy to use dashboard of Roll Call vote data so a member of the public could know easily how their representatives vote on issues that matter to them.

Whenever a bill is brought to the House or Senate and a vote is taken (not just for final approval, but for votes on amendments, reviewing portions of a bill etc.), the vote is taken and saved in various locations. For the House of Representatives, Roll Call votes are published in House Journal PDFs that can be accessed online. Roll Call votes in the Senate appear in Senate Journals, but not as clearly as the House and are more easily accessed via MA Legislature provided SwaggerAPIs.

Due to this inconsistency on how the data is stored and presented to the public, ACT on MASS seeks to compile and present a complete data set of available Roll Call votes so interested parties can find answers to key questions such as how a representative voted on bills of a specific issue, how their votes may change over time, or how many votes they missed over the years in an interactable and easy-to-use dashboard presentation.

## Data locations

In this section, you should include the location of all of your datasets for the project (if applicable)

<a href="dataset-documentation">Dataset Documentation</a>

The dataset used for this project is an original creation by the team, primarily derived from the following two sources, but compiled and cleaned via our scraping and parsing methods.

* Location 1: [MA Legislature Roll Call Vote API](https://malegislature.gov/api/swagger/index.html?url=/api/swagger/v1/swagger.json#/SenateJournals)
  * This API was parsed for all Senate Roll Call vote data from 2015 to present day and stored in the file data/MA_senate_rollcall_votes_denorm.csv (not currently in the Repo as noted in Key Features section but will be at final submission).
* Location 2: [MA Legislature House Journals](https://malegislature.gov/Journal/House)
  * This website contains selectable links for each House Journal published as a PDF by the MA legislature, which contains Roll Call votes for a period of time. These PDFs were automatically scraped and parsed into a single data file hjrollcallvotes_cleanedv1.csv (not currently in the repository as noted).
