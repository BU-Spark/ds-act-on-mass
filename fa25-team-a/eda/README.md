# README for Team A EDA

The eda folder is can be mapped to the following file tree:

📦eda
 ┣ 📂designing_relational_schema
 ┃ ┣ 📜schema.md
 ┃ ┗ 📜scrape_representatives.ipynb
 ┣ 📂senate_api
 ┃ ┣ 📜api_coverage_check.py
 ┃ ┗ 📜senate_api_coverage.csv
 ┣ 📂senate_data_parsing_methods
 ┃ ┣ 📜Senate_data.ipynb
 ┃ ┗ 📜TODO.md
 ┣ 📂testing_pdf_parsing_libraries
 ┃ ┗ 📜pdf-parsing.py
 ┗ 📜README.md

 Each subfolder within the main eda folder corresponds to an individual team member's contributions to our exploratory data analysis. Each team member has a section below that describes in further detail what work was done in their EDA process and how it contributes to the larger team product.

 Since this project is based around collecting data in an unstructured format (pdf files) and through an API that had uncertainty over its usability, our EDA work centered around figuring out how we are going to get the data we need and identifying what parts of the data would be most useful for us and what we can ignore, rather than being focused on analysis of an existing dataset.

 After this step of our project, we have identified the method and source for our data more clearly and our next steps will be to assemble and clean our ideal dataset.

## Senate API Coverage Checking (Jason Nguyen)

This script tests Approach 1 (API-based extraction) for the Massachusetts Legislature Senate Roll Call data. The script's goal is to see how much of the Senate’s (2025–2026) roll call data is accessible through the official Massachusetts Legislature API. By running this script, we can see which roll call numbers (1–100) return valid data and which do not. This helps the team decide whether to rely on the API or use an alternative data source such as the PDF files.

## House Roll Call PDF Parsing Library Exploration (Aviva Foster)

## Senate Data Alternative Parsing Method Exploration (Prashanthi Geesala)

## Relational Data Schema Design (Gregory Knapp)

Within the ```designing_relational_schema``` subfolder, there are two files: ```schema.md``` and ```scrape_representatives.ipynb```.

schema.md is a markdown file with a text description of the ideal relational database that we will need in order to accomplish our task of not only scraping and collecting the roll call vote data from the pdf documents but structuring it in a way that will allow us to organize the visualizations to show how representatives vote over time, on certain types of bills, and more. By organizing the data into relational tables, this will allow us to perform the proper joins and unions needed to display data in Google Looker Studio dynamically based on what the user wants to know.

While preparing the schema, I realized that we may need some additionally data parsed from the legislature API that isn't readily available in the pdfs of roll call votes, the primary one being information about representatives that may be helpful to have (District, Branch, Party Affiliation). The ```scrape_representatives.ipynb``` file serves to provide an example of how this data can be mass-scraped from the MALegislature website and saved to a csv for future use. Although this file is specialized for the representatives, it can serve as a helpful tool for our team when we get to scraping the files we need since as a framework or examples for others to work off of for scraping off different API endpoints.
