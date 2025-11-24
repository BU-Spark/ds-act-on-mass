
<h1 align="center">
  <br>
  <a href="https://www.bu.edu/spark/" target="_blank"><img src="https://www.bu.edu/spark/files/2023/08/logo.png" alt="BUSpark" width="200"></a>
  <br>
  ACTonMass Team B <change to project name>
  <br>
</h1>

<h4 align="center">A gathering of legislator's votes on bills in Massachussets </h4> <change to repo short description>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#project-description">Project Description</a> •
  <a href="#data-locations">Data Locations</a>
</p>

## Key Features
Our code will generate different files of data organized into tables to be sent into a looker studio report/
You should also include a short description of what each part of your code does. (Detailed description in the readme of each directory, if applicable)
* /bill_exploration.ipynb - This imports committee data and topic categorization
  - This is there to compare a bill and their committee that wrote the bill to create a topic for which we can categorize our data with.
* /EDA - The EDA Folder currently contains most of our important scripts.
  - These will later be separated to have the final scripts outside of this folder and instead be in the main team folder.
* /EDA/all_senate_data_import.ipynb
  - This imports the Senate's data and organizes it to fit the formatting needed
  - This has a way to import one general court (year) for all Senate data
  - It also generally imports bills and checks for roll calls though that is limited to only the Senate.
* /EDA/Full_House_RollCall_scraper.ipynb
  - Gets the PDFs from the malegislature website to be able to get the roll call data for the House
* /EDA/parse_house_rollcall_data.ipynb
  - This now parses through the data gathered from Full_House_RollCall_scraper.ipynb to be able to get it in a readable format

## How To Use

Currently it will take a while to reproduce everything we have gotten.
The main data files to add to our Looker Studio are written in <a href="#key-features">Key Features</a>. 
Run through all of those and as of writing this that would give most if not all the data needed to be added to Looker studio.
Potentially might need to merge the datasets in Looker.
 
## Project Description

This project aims to develop a data pipeline and interactive visualizations to streamline legislative vote tracking and analysis.
We are attempting to create a cleaned dataset that contains roll call voters, bill names, amendments and various other information pieces on the legislator and bills.

We are creating Interactive visualizations on looker studio that enable users to search for legislators and view their voting history, track missed votes and voting patterns, and filter by topic or bill type 22.
Our visualizations are attempting to answer questions such as:
How does each legislator vote?
How many votes do legislators miss, and how often?
What trends exist in roll call voting over time?
How are roll call numbers linked to specific bills and amendments?
What patterns emerge across different legislative sessions?


## Data locations

Currently for our actual data it is either located in our team-b-eda branch under data. Or it is located in the cloud storage tied to Looker studio.
