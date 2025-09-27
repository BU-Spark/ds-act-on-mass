# Team A Research

## Problem Analysis

**Aviva:**

From client/project description: "This project aims to develop a data pipeline and interactive visualizations to streamline legislative vote tracking and analysis."

Current issues:

- Roll call votes, when taken, are published as individual PDFs & unlinked from relevant legislation
  - Note: It is possible to download combined PDFs of all the roll call votes from a particular year, but this is just a consolidation of the individual PDFs, and it is still difficult to discern/understand/find the legislation each vote is connected to. Would it be easier or harder to process a full year at once..?

**Greg:**

At first glace the problem seems very straight forwards; most of the confusion is just with the extent of how exactly the client wants the final product to look like. Specfically, questions I have after looking into the project

Data collection: The process seems straightforward as the client gave us a concrete site and APIs to automate scraping. However, a few questions came up.

- How far back do they want us to go?
- Do they want automation or do they just want what is currently there and leave it at that
- How do they want us to handle the Senate votes?

The last question is my biggest one. The house votes are very clearly given in the role call documents, but despite the senate journals saying they include role calls, I could not find a vote listing after looking through about 100 of them. The website does include bills which do come with votes.

Visualization: The client requested us to use Google Looker Studio for visualizations, so no decision making is needed. After testing it out for the first time, a few questions came up.

- Is CSV the correct format for the output of our pdf scraping? If the client ends up wanting automation, we may need an additional component to the pipeline to import into Looker Studio instead of manually scraping and uploading CSVs.

**Jason:**

- 

## Potential Solutions

**Aviva:**

- The Massachusetts Legislature Public API [https://malegislature.gov/api/swagger/index.html?url=/api/swagger/v1/swagger.json#/], provided by the client, allows us to pull Roll Calls by document number. Each Roll Call includes a heading with the relevant bill number and a short note on what was being voted on. Bills can be searched by bill or docket number using the API. Would we be able to pull roll calls, identify the bill number, and pull the relevant bill in order to more clearly associate legislature with voting records?
- Generally will need something to read PDFs into a more workable format; roll calls are in the format of a list of names (several columns of names to a page), each name preceded by their vote (Y - Yes/N - No/P - Present/X - Not Voting)
- Can use as potential references the vote/bill tracking websites of other comparable states, such as [New York](https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=A04762&term=2025&Summary=Y&Floor%26nbspVotes=Y) and [Ohio](https://www.ohiosenate.gov/legislation/136/hb43/votes). (These links refer to specific but random bills, just to use as examples.)

**Greg:**

- For reading PDFs, the following libraries are worth exploring: tabula-py, pdfplumber, pypdf, PyMuPDF
- Any scraping and downloading can be done using BeautifulSoup + Requests library in Python. Unless we really end up needing to use some strange sites for Senate data, we should not need to use Selenium.
- The challenge will be seeing which library deals with the lack of visual structure in the pdf, as the text is clearly formatted in a table, but there are no visual lines to reference for each field.
- If the Senate Journals do not clearly contain parsable role call votes, we can scrape the [Bills and Laws](https://malegislature.gov/Bills/Search) section of the website.
- Alternatively, a website like [LegiScan](https://legiscan.com/MA/bill/S3/2025) gives a table for each vote that would be very easy to parse (automated scraping would be harder though, since it is not just mass downloading pdfs).
- Questions about the inputs into Looker Studio and automation can be addressed in client meetings, for now, it is safe to assume that for an initial Minimal Viable Product, parsing a single house role call vote into a PDF, into a CSV file that is manually uploaded into Looker Studio and turned into a visualization is a good place to start.

**Jason:**

- 