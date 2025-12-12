***Project Information*** 

* What is the project name?
  * Act on Mass Team A
* What is the link to your project’s GitHub repository?
  * https://github.com/BU-Spark/ds-act-on-mass
* What is the link to your project’s Google Drive folder? \*\**This should be a Spark\! Owned Google Drive folder \- please contact your PM if you do not have access\*\** 
  * https://drive.google.com/drive/folders/1p7KF_je0pw89cBUx8568RRYc8k8mKf-X?usp=share_link
* In your own words, what is this project about? What is the goal of this project?
  * This project is about improving Massachusetts government transparency through the act of compiling roll call votes on various bills and amendments into an easy to search format for public consumption. The data isn't necessarily unavailable, but it is stored in various formats and in various places, making it hard to get a comprehensive look on the voting record of a particular legislator or their trends over time. By doing the groundwork necessarily to assemble the data and present it in an easy to parse way, we aimed to create a tool that can increase public awareness of the day-to-day actions of their government representatives.
* Who is the client for the project?
  * The non-profit Act on Mass organization.
* Who are the client contacts for the project?
  * Scotia Hille, executive director of Act on Mass.
* What class was this project part of?
  * DS701 FA 2025

***Dataset Information***

* What data sets did you use in your project? Please provide a link to the data sets, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.
  * The dataset was compiled from MA House of Representative roll call vote PDF extracted from the [MALegislature website](https://malegislature.gov/Journal/House) as well as Senate roll call votes extracted directly from the [MALegislature API interface](https://malegislature.gov/api/swagger/index.html?url=/api/swagger/v1/swagger.json). These were compiled into a few CSV files that became Google BigQuery tables that were used to make the final Looker Studio visualization. A link to the Drive folder containing the final versions of the CSV files is [here](https://drive.google.com/drive/folders/1y57MGmealjp_GGHoZMbAQpeHUItc_NKc?usp=share_link)
* Please provide a link to any data dictionaries for the datasets in this project. If one does not exist, please create a data dictionary for the datasets used in this project.
  * [House Dataset Dictionary](house_datasetdictionary.csv)
  * [Senate Dataset Dictionary](senate_datasetdictionary.csv)
* What keywords or tags would you attach to the data set?
  * Domain(s) of Application: OCR, NLP, Summarization, Civic Tech, Voting

*The following questions pertain to the datasets you used in your project.*
*Motivation*

* For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.
  * The dataset was created to be as complete as possible given the resources available through the official Massachusetts government website. For the Senate, we retrieved roll call votes from 2015 to present day; for the house, 2003 to present day. For what was available, there is no gap to our knowledge. However, it is possible that the House or Senate clerks may have data in other formats (non-digital) that could expand the range of the current dataset. Additionally, this project created a dataset that is up-to-date as of October 13th, 2025 in terms of roll call votes, but does not include data from votes that took place after that date. Building out a data ingestion pipeline was a stretch goal for this project that was not realized this semester but would be a logical continuation of this work. For that reason, there is potential for expansion both in past data records and future incoming data, but for all intents and purposes of the project, there are no gaps in the expected dataset requested by the client.

*Composition*

* What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? What is the format of the instances (e.g., image data, text data, tabular data, audio data, video data, time series, graph data, geospatial data, multimodal (please specify), etc.)? Please provide a description.
  * The final dataset consists of two primary tables of denormalized roll call vote instances for both the House of Representatives and the Senate. Each row contains the value of the vote (yea, nay, etc.) as well as key details such as which bill the vote was for, who casted the vote, and information about the bill and the member who made the vote. The data is stored entirely in relational tabular data, in string, date, and numeric formats. No other alternative format is included in this dataset.
* How many instances are there in total (of each type, if appropriate)?
  * In the dataset for the House, there are 861,463 unique roll call vote instances. For the Senate, we retrieved 908,647 votes.
* Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).
  * Given the nature of the dataset, there is no concept of representativeness or sampling. The dataset includes every unique instance of a roll call vote cast for the years we had documentation for.
* What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.
  * Each data instance consists of text fields (of datatype string, int, or datetime) that contain all the necessary information for answering queries about a roll call vote. For example, beyond the vote value and the name of the representative who cast the vote, information about the date the vote took place, the bill name and number the vote was on, as well as political party and leadership role information for the voter are included in each data row.
* Is there any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include redacted text.
  * There are no missing fields for the critical fields of the dataset (vote value, representative name), but gaps in the data do exist. For example, for House roll call votes from 2009 - 2017, a time was not published for the vote but for all other years a time was given with each voting record. Because of this difference, the time is parsed and included as a column in the table, but is null for all voting records from these years. Additionally, some representatives never held leadership positions so null fields appear here. In some cases, data that should be present but is missing does appear. For example, some representatives appear without a district they represent in the data when it is expected that every representative has one. This is likely due to clerical errors on the governments side and could be remedied manually but due to the large nature of the voting data, was not handled in this case.
* Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them
  * There are no splits for training or testing for the data and this dataset is best kept together as it is for completeness. It is not a dataset for predictive modeling or any sort of quantitative analysis so there is no need for splits for this project.
* Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.
  * In the final dataset we were able to validate the House data for errors that may have been caused due to OCR parsing techniques on the PDF data. For example, certain names failed to parse correctly (i.e. O'day being read as 0'day). These issues were examined and validated against a dataset of which representatives appeared during each court sessions, as well as checked for duplicate votes in each roll call instance. These two checks allowed us to be confident that any OCR parsing errors were caught and each representative who is expected to cast a vote in a given year cast their vote, with no votes misattributed. For the Senate, since the data came through the API in a clean format, it was able to be handled with confidence with no expectation of unexpected errors (beyond missing data that is the fault of the government)
* Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources,
  * Are there guarantees that they will exist, and remain constant, over time;
    * This dataset is nearly guaranteed to be correct. It is possible for the government to publish a retraction or modification to an old roll call vote. However, these modifications are identified in a way that can be linked back to the original vote to be updated or replaced. This is something to be considered for a future data ingestion update to this project.
  * Are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created)?
    * The data for this dataset exists on the MA government servers, so beyond our archived version in Google Drive with the complete voting data for the years covered in the data, it is possible the data source may be affected if something were to happen to the government website. Everything is downloaded via an API or through the website so it would not be preserved through traditional web archive efforts (such as WayBack Machine), so preservation of our dataset, which has been given to the Act on Mass team is important.
  * Are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points as appropriate.
    * To our knowledge, there are no issues with the use of this dataset. All of the information is publically available on the MALegislature website and is simply compiled by us into one source.
* Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)? If so, please provide a description.
  * No privacy-sensitive data is contained in this report.
* Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.
  * There is nothing of that nature in this dataset.
* Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? If so, please describe how.
  * Any identifiable information about political representatives (full name, district, political affiliation) is all publically-available knowledge.
* Dataset Snapshot, if there are multiple datasets please include multiple tables for each dataset.

| Size of dataset (House) |  |
| :---- | :---- |
| Number of instances | 861,463 |
| Number of fields  | 19 |
| Labeled classes | N/A |
| Number of labels  | N/A |

| Size of dataset (Senate) |  |
| :---- | :---- |
| Number of instances | 908,647 |
| Number of fields  | 14 |
| Labeled classes | N/A |
| Number of labels  | N/A |

*Collection Process*

* What mechanisms or procedures were used to collect the data (e.g., API, artificially generated, crowdsourced \- paid, crowdsourced \- volunteer, scraped or crawled, survey, forms, or polls, taken from other existing datasets, provided by the client, etc)? How were these mechanisms or procedures validated?
  * The House PDFs were downloaded via mass-requests on the [House Journal webpage](https://malegislature.gov/Journal/House) where they can be manually downloaded normally. To ensure completeness, every possible day of the year was used from 2003 to the present day (October 13th, 2025) to ensure that any existing House votes were retrieved and downloaded. For the Senate, a similar process was used but instead of retrieving by day of the year, the API for the Senate that was used allowed for votes to be queried by General Court session then an automatically incrementing document number. This allowed us to be sure that all possible data for both legislative bodies were retireved.
* If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?
  * No sampling was used in this dataset.
* Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.
  * This dataset represents the years 2003 - 2025 for the House (up to October 13th, 2025) and 2015 - 2025 (up to the same date) for the Senate. Within this years, the data is complete for roll call votes and should remain unchanged unless a past vote is retracted or modified, upon which a new document is published showing that, which could be handled in an extended pipeline.

*Preprocessing/cleaning/labeling*

* Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.
  * Very slight cleaning was done to the dataset, particularly the House of Representative data that was collected using OCR methods. This included matching representative names (while keeping consideration for names that included inconsistent use of ASCII characters, especially Spanish characters) to unique representative codes, removal of additional text that appeared with representative names in the PDF files (dashes and astericks) and fixing OCR parsing errors that may have arised (especially names with values that were incorrectly read such as O being read a 0).
* Were any transformations applied to the data (e.g., cleaning mismatched values, cleaning missing values, converting data types, data aggregation, dimensionality reduction, joining input sources, redaction or anonymization, etc.)? If so, please provide a description.
  * Beyond the previously mentioned cleaning tasks, the only major transformation was the association of each vote with a member code value that the MA government uses to uniquely track each representative who has ever served in either the House or Senate. To do this, once all the names for each vote were cleaned and parsed, simple matching logic was used to check if last names and first names matched a directory of representatives we had for each General Court legislative session. This matching process allowed us to use the member codes instead of the representative's whole name for better voting trend aggregation, since there were cases where representatives stylized or spelled their names slightly different from year to year. For example, representative Gomez would sometimes have their name with the Spanish accented o character in some votes but not others. Matching both of these names with the same unique member code allowed us to then aggregate votes correctly and not end up with unexpected votes assigned to different representatives when they are the same person in actuality.
* Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.
  * Raw data was stored in a subfolder of our [Spark Google Drive folder](fa25-team-a/processing/senate_data_cleaning/senate_data_cleaning.ipynb)
* Is the code that was used to preprocess/clean the data available? If so, please provide a link to it (e.g., EDA notebook/EDA script in the GitHub repository).
  * [Senate Cleaning Notebook](../processing/senate_data_cleaning/senate_data_cleaning.ipynb) and [House Cleaning Notebook](../processing/house_data_cleaning/merge_house_rep_data.ipynb).

*Uses*

* What tasks has the dataset been used for so far? Please provide a description.
  * The dataset has only been used in the Looker Studio project that is the final deliverable for this project.
* What (other) tasks could the dataset be used for?
  * The dataset could be used for additional visualizations or dashboards beyond what we created, but is unlikely to be particularly useful for predictive or modeling tasks, since it mostly is just historical records of voting data.
* Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?
  * The only noteworthy mention about the data collection is the fact that the House of Representative has had a tendency to change the formatting slightly for PDF records year-to-year with no explanation as to why. We even contacted the House clerk to see if there was any reasoning but none was given. For that reason, hard coded parsers for data ingestion are discouraged (without extensive testing for robustness) and potential expansion to using a vision AI model can help avoid issues with changes that may or may not come in the future to the House data format.
* Are there tasks for which the dataset should not be used? If so, please provide a description.
  * Although it may not be suited for certain predictive tasks, there is nothing explicitly stopping the data from being used so no restrictions on its use are given.

*Distribution*

* Based on discussions with the client, what access type should this dataset be given (eg., Internal (Restricted), External Open Access, Other)?
  * The dataset in an easy to consume form through Looker Studio will be publically available. There is no issue with making it public and a link to the data itself will likely be provided (at the discretion of Act on Mass) but it is better consumed in a dashboard form due to the size and nature of the data.

*Maintenance* 

* If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description.
  * The best way to expand on the data (especially regarding data ingestion) would be to download the full CSV files of the House and Senate votes, and use that as a base for a data ingestion pipeline to then add new records into this dataset. This repository can be forked and expanded on for that purpose or a new repository can be used, but building off the base datasets included in this project is recommended.

*Other*

* Is there any other additional information that you would like to provide that has not already been covered in other sections?
  * None
