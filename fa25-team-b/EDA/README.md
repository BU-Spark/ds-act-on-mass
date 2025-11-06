Exploratory Data Analysis

The SenateImport file shows an initial step-by-step explanation of what is required to get the roll call information on a MA Senate voted document through the MA Legislature API. It explains how to read the outputs at a surface level and how these files can be chained to get the roll call information and the individuals who voted in it. 

The Full_House_RollCall_Scraper is a scraper to get all the pdfs available on the MAlegislature website

The parse_house_rollcall_data file contains a method to parse through all the pdfs and retreive roll call data, as well as a method to extract specific bill/amendment data as well as displays a few visualizations for specific bill/amendment and senator etc.

The open states import file shows the method to obtain MA House bills through the OpenStates API.

The 2025 roll call file extracts 2025 year to dateroll call data from the pdf available malegislature website,and shows a method to extract specific bill/amendment data as well as displays a couple visualizations for it.

The eda File has information on how to scan through a document, organize it and then check for roll call information.

The dataExploration file downloads all documents in a general court iterates through them and find valid bill numbers and extracts the roll call number.
