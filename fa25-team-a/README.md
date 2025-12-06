
<h1 align="center">
  <br>
  <a href="https://www.bu.edu/spark/" target="_blank"><img src="https://www.bu.edu/spark/files/2023/08/logo.png" alt="BUSpark" width="200"></a>
  <br>
  ACT on MASS - Team A
  <br>
</h1>

<h4 align="center">Creating a searchable Roll Call vote dataset and dashboard for MA government transparency </h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#project-description">Project Description</a> •
  <a href="#data-locations">Data Locations</a>
</p>

## Key Features

This project involved sourcing and processing data about Roll Call votes for both the Massachusetts House of Representatives and Senate. The steps taken for collecting, parsing, and cleaning this data can be found in the highlighted directories below.

* fa25-team-a/data: Contains the final cleaned House and Senate Roll Call datasets, as well as supplementary .csv files containing Representative information, and Bill information which can be mapped to Roll Call votes in order to provide greater context (i.e. tracking the votes of a single representative over time, or votes on the same bill over multiple instances).
  * Currently, data is being stored in our SPARK Shared Google drive as per the request of our Technical Project Manager until we are completely done with the project and data is finalized.
* fa25-team-a/eda: Contains initial data parsing attempts, API investigations, research into which PDF parsing libraries would be effective for completion of this task.
  * While EDA typically indicates exploratory investigation of a dataset for key features and points of interest, since our project did not come with an existing dataset, our use of EDA in this case reflects our initial attempts into problem solving and developing solutions for the problems.
* fa25-team-a/processing/senate_data_extraction: Contains a Jupyter notebook for for extracting Senate Roll Call data via the [RollCalls API endpoint](https://malegislature.gov/api/swagger/index.html?url=/api/swagger/v1/swagger.json#/RollCalls) provided by the MA government as well as other important data for legislators, bill details, which are used throughout the project for enhancing our dataset.
  * The RollCalls API provides a nice mapping of Bills to Representatives to Votes, so with some work (in the notebooks contained in this directory) we created a denormalized dataset that can be easily queried to answer key questions about voting patterns dating back to 2015 (the oldest year of data available on the API)
  * For an unknown reason, the RollCalls API contained data for the Senate but not the House, resulting in the differing data collection and parsing methods.
* fa25-team-a/processing/senate_data_cleaning: Contains a Jupyter notebook that cleans and combines the various sources of data parsed in the senate_data_extraction step into a singular denormalized dataset that is used in our final visualization.
  * The final normalized dataset combines not just the votes of each member of the Senate on a given roll call instance, but also combines the representative information to add information about political party or legislator leadership rolls, as well as key bill details such as name or committee to create a final comprehensive Senate Roll Call dataset.
* fa25-team-a/processing/house_data_extraction: Contains 2 Jupyter notebooks for scraping and then parsing Roll Call votes from the House of Representatives over the years of 2002 to 2025.
  * The House Roll Call votes are provided as a PDF transcription, in varying formats so multiple methods are defined depending on the year the PDF was created in.
  * While most PDFs could be read using a PDF text parsing library (i.e. PyMuPDF), some were stored as an embedded image and required OCR methods to extract the vote data effectively.
* fa25-team-a/processing/house_data_cleaning: Contains a single Jupyter notebook for cleaning and matching representative names into the data that was parsed from the House Roll Call PDFs.
  * This representative merging step is essential to the House parsing process (but not needed in the Senate data, since the roll call votes from the API come with a unique code that identifies which member made the vote) since the PDF only gives a last name for each vote. Since representatives with duplicate last names exist over the years, this step replaces the last name given with each vote with the matching unique member code used by the legislature for identification.
  * On top of representative matching, this step also includes removing miscellaneous parsing artifacts from the PDF parsing and small fixes and tasks unique to this dataset.
* Final Visualization: The cleaned House and Senate Roll Call vote data is presented using a [Google Looker Studio Dashboard](https://lookerstudio.google.com/s/rehxBi-Cql0) as per the request of the client organization.
  * The Looker Studio uses our parsed dataset stored in a Google BigQuery instance for easy retrieval and querying for advanced analysis of the results.

## How To Use

To clone and run this application, you'll need <a href="https://git-scm.com" target="_blank">Git</a>

From your command line:

```bash
# Clone this repository
$ git clone https://github.com/BU-Spark/ds-act-on-mass.git

# Recommended: Initialize a virtual environment
python -m venv .venv

# Start the virtual environment
source .venv/bin/activate #POSIX
.venv/Scripts/activate.bat # Windows Command Prompt
.venv/Scripts/activate.ps1 # Windows PowerShell

# Navigate into the team-a subfolder of this project
cd fa25-team-a

# Install dependencies
pip install -r requirements.txt
```

Once dependencies are installed, the project data can be reproduced by proceeding running the following notebooks in this suggested order:

```python
fa25-team-a/processing/senate_data_extraction/fa25-team-a/senate_data_extraction.ipynb
fa25-team-a/processing/senate_data_cleaning/senate_data_cleaning.ipynb
fa25-team-a/processing/house_data_extraction/scrape_house.ipynb
fa25-team-a/processing/house_data_extraction/parse_house.ipynb
fa25-team-a/processing/house_data_cleaning/merge_house_rep_data.ipynb
```

After these steps are completed, the following .csv files should reflect the expected final output that would then be uploaded to BigQuery and linked into Looker Studio as per our methods for visualizations.

```python
fa25-team-a/data/final/MA_senate_rollcall_votes_denorm.csv
fa25-team-a/data/final/hjrollcallvotes_final.csv
fa25-team-a/data/final/hjbills_final.csv
fa25-team-a/data/final/MA_legislature_members.csv
```

Some other files may be present in the "final" folder but are used for creation of the senate_roll_call_votes_denorm.csv file and are not expected to be used for the final visualization.

## Project Description

The Act on MASS project seeks to improve the transparency of Massachusetts state legislators by providing an easy to use dashboard of Roll Call vote data so a member of the public could know easily how their representatives vote on issues that matter to them.

Whenever a bill is brought to the House or Senate and a vote is taken (not just for final approval, but for votes on amendments, reviewing portions of a bill etc.), the vote is taken and saved in various locations. For the House of Representatives, Roll Call votes are published in House Journal PDFs that can be accessed online. Roll Call votes in the Senate appear in Senate Journals, but not as clearly as the House and are more easily accessed via MA Legislature provided SwaggerAPIs.

Due to this inconsistency on how the data is stored and presented to the public, ACT on MASS seeks to compile and present a complete data set of available Roll Call votes so interested parties can find answers to key questions such as how a representative voted on bills of a specific issue, how their votes may change over time, or how many votes they missed over the years in an interactable and easy-to-use dashboard presentation.

## Data locations

The dataset used for this project is an original creation by the team, primarily derived from the following two sources, but compiled and cleaned via our scraping and parsing methods.

* Location 1: [MA Legislature Roll Call Vote API](https://malegislature.gov/api/swagger/index.html?url=/api/swagger/v1/swagger.json#/SenateJournals)
  * This API was parsed for all Senate Roll Call vote data from 2015 to present day and stored in the file data/MA_senate_rollcall_votes_denorm.csv (not currently in the Repo as noted in Key Features section but will be at final submission).
* Location 2: [MA Legislature House Journals](https://malegislature.gov/Journal/House)
  * This website contains selectable links for each House Journal published as a PDF by the MA legislature, which contains Roll Call votes for a period of time. These PDFs were automatically scraped and parsed into a single data file hjrollcallvotes_cleanedv1.csv (not currently in the repository as noted).
