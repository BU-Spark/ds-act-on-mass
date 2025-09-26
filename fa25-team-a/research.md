# Team A Research

## Problem Analysis
Aviva:
From client/project description: "This project aims to develop a data pipeline and interactive visualizations to streamline legislative vote tracking and analysis."

Current issues:
- Roll call votes, when taken, are published as individual PDFs & unlinked from relevant legislation
    - Note: It is possible to download combined PDFs of all the roll call votes from a particular year, but this is just a consolidation of the individual PDFs, and it is still difficult to discern/understand/find the legislation each vote is connected to. Would it be easier or harder to process a full year at once..?



## Potential Solutions
Aviva:
- The Massachusetts Legislature Public API [https://malegislature.gov/api/swagger/index.html?url=/api/swagger/v1/swagger.json#/], provided by the client, allows us to pull Roll Calls by document number. Each Roll Call includes a heading with the relevant bill number and a short note on what was being voted on. Bills can be searched by bill or docket number using the API. Would we be able to pull roll calls, identify the bill number, and pull the relevant bill in order to more clearly associate legislature with voting records?
- Generally will need something to read PDFs into a more workable format; roll calls are in the format of a list of names (several columns of names to a page), each name preceded by their vote (Y - Yes/N - No/P - Present/X - Not Voting)
- Can use as potential references the vote/bill tracking websites of other comparable states, such as New York [https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=A04762&term=2025&Summary=Y&Floor%26nbspVotes=Y] and Ohio [https://www.ohiosenate.gov/legislation/136/hb43/votes]. (These links refer to specific but random bills, just to use as examples.)