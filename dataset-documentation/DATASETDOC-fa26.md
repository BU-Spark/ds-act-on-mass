Project Information
* What is the project name?

Act On Mass

* What is the link to your project’s GitHub repository?

https://github.com/BU-Spark/ds-act-on-mass/tree/fa25-team-b-eda/fa25-team-b

* What is the link to your project’s Google Drive folder?

(Spark!-Owned Folder)
https://drive.google.com/drive/folders/1I7e076N35iZQbr06d3kU_-kKzO84D84O?usp=drive_link

* In your own words, what is this project about? What is the goal of this project?

The goal of this project is to build an end-to-end data pipeline and a set of Looker Studio dashboards that make legislative voting data easier to collect, clean, explore, and interpret. By transforming unstructured Senate and House records into a structured, query-ready format, we enable Act on Mass and the public to efficiently track roll call votes, analyze legislative behavior, and uncover trends across sessions, committees, and topics.

* Who is the client for the project?

Act on Mass

* Who are the client contacts for the project?

Scotia Hille (Executive Director)

* What class was this project part of?

DS701

Dataset Information
* What data sets did you use in your project?
https://drive.google.com/drive/folders/1OUWr0nCNVn-fuCgMjx9DsKhQOeVVgq4u?usp=drive_link
* Data Dictionary

https://docs.google.com/document/d/1FmJKcThVYJ70bcMUeRIoyvhK-zTwKD5fw5aeNdkitRM/edit?usp=sharing
* Keywords / Tags

Domains:
* OCR
* Text Extraction
* NLP
* Data Parsing
* Tabular Data

Topics:
* Civic Tech, Voting,Government Transparency, Legislative Data, Accountability

Techniques:
* PDF scraping, Data cleaning
* Visualization
* API integration

Motivation:
The dataset was created to fill a major transparency gap in Massachusetts government. Roll call votes are publicly available but extremely difficult to access because:

* They are published only as individual PDF documents and are not linked to the bills or amendments they relate to. Names and formatting are inconsistent and there are no unified, analyzable dataset exists

The dataset aims to extract all roll call votes into a machine-readable form,Link votes to bills and amendments. we also want to allow public analysis of how legislators vote and power an interactive dashboard that supports transparency efforts

Composition
* What do instances represent?

Each instance represents:

* A single legislator’s vote
* On a roll call
* Linked to a bill or amendment

Additional instance types:
* Individual roll calls
* Bills snd/amendments
* Legislator metadata

* Data format

Raw data:
* PDF text from Massachusetts Legislature website

Processed data:
* Tabular CSV including fields such as:
rollcalls
name
vote
billnumber
amendment_number
Generalcourtnumber
Party
Room
EmailAddress
RoomNumber
Branch
Phone
District
MemberCode
LeadershipPosition
SessionParticipation
TotalYeas
TotalNays
TotalNV
AverageAttendance
Member1
Member2
Cordex
Member1Party
Member2Party
Member1Position
Member2Position
SameParty
AnyLeader
BothLeaders
CrossPartyHighSim
TotalVotes
YeaCount
NayCount
AbsentCount
MajorityLeaderCode
MajorityLeaderVote
AlignedWithLeaderCount
AlignmentRate
IsUnanimous
UnanimityVoteType
PartyAligned_D
PartyAligned_R

* Number of instances
809,482 total rows
* Does the dataset contain all instances?
It aims to include all roll calls for General Court sessions 181–194, but gaps may exist due to:

* Missing PDFs
* Formatting changes
* Scanned/non-text PDFs requiring OCR
* Missing information

Some PDFs lack:

* Bill  numbers
* Amendment numbers
* Motion text
* Legislator initials (ex:"Rogers")
* Errors or noise
* Duplicate legislator names
* OCR errors
* Inconsistent vote labels (Yea/Yes/Y,Nay/No/N, NV)
* Formatting differences between pages
* External resources
* Legislature PDFs
* Legislature API
* Open States API


  Confidential or sensitive data

None becayse all information is public legislative data.

* Identifiability

Legislators (public officials) can be identified by name; no private individuals included.

Dataset Snapshots
all_sessions_legislators

* Size: 201 kB
* Instances: 2478
* Fields: 10

house_full_sessions_cleaned_2

* Size: 94.6 MB
* Instances: 788,994
* Fields: 19

house_legislators_2019_2022

* Size: 139 kB
* Instances: 1,923
* Fields: 9

house_participation

* Size: 320 bytes
* Instances: 2
* Fields:  6

house_session_vote_summary

* Size: 363 bytes
* Instances: 12
* Fields: 4

senate_average_attendance

* Size: 209 bytes
* Instances: 8
* Fields: 2

senate_member_corr

* Size: 1.4 MB
* Instances: 13,228
* Fields: 12

senate_rollcall_alignment_summary

* Size: 169 KB
* Instances: 2,827
* Fields: 15

Collection Process
* Mechanisms
* PDFs scraped using Python (re,pdfplumber)
* Bill + committee metadata from legislature API
* Sampling Strategy
* Full-population dataset
* Timeframe

* Data collected in 2025
* Roll calls originate from the 194th General Court

Preprocessing
* Extract PDF text (pdfplumber or OCR)
* Segment roll calls
* Link roll calls to bills/amendments
* Clean and standardize legislator names
* Normalize vote codes (Y/N/P/NV)
* Remove duplicates
* Validate counts

Transformations
* PDF to structured tto tabular
* Join with bill metadata
* Normalize inconsistent fields

Raw Data
Stored in project Drive/GitHub.

Uses

* Tracking legislator voting behavior
* Missed vote analysis
* Linking votes to policy topics
* Civic transparency dashboards
* Trend analysis


* Could Be Used For

* Vote prediction models
* Topic modeling of bills
* Network analysis of voting blocs
* Legislative similarity scores

* Limitations

* OCR errors
* PDF format inconsistency

Distribution
* Access Type

External Open Access (Public Transparency Dataset)

Maintenance
* Contribution Mechanism

Future contributors can:

* Add new legislative sessions
* Improve parsing logic
* Update rosters
* Fix OCR errors
* Submit GitHub pull requests
