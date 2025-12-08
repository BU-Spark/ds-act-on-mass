##Trying out different PDF parsing libraries
#This is the same information as in the `pdf-parsing.ipynb` file
#Initial exploration:

#creating relative file path
from pathlib import Path
current_directory = Path().absolute()
parent1 = current_directory.parent
parent2 = parent1.parent
file = parent2 / 'data/rawpdfs' / 'HouseRollCall25.pdf'

"""
#Tabula:
import tabula

test1_df = tabula.read_pdf(file, pages = "all")
print(test1_df)

#Outcome has a lot of NaN instead of names
"""

"""
#pdfPlumber
import pdfplumber

test2_df = pdfplumber.open(file)
print(test2_df.chars)

#Seems annoying to use
"""

"""
#PyPDF2; referenced https://www.geeksforgeeks.org/python/introduction-to-python-pypdf2-library/
import PyPDF2

with open(file, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    text = reader.pages[0].extract_text()
    print(text)

#Seems really useful?? Outputs full lines from PDF. Though I'm not sure why the votes are after the names, I'm not mad about it
"""

#PyMuPDF
import pymupdf
import pandas as pd

doc = pymupdf.open(file)
for page in doc:
    text = page.get_text()

#Outputs individual values from PDF, which I think would be the most useful/easy to manipulate as needed

#Referenced https://artifex.com/blog/extracting-tables-from-pdfs-with-pymupdf
page1 = doc[0]
tables = page1.find_tables(strategy = "text")
table1 = tables[0]
df = table1.to_pandas()


#Need to reshape/restructure to be just two columns, name and vote


#Renaming columns
df_new = df.rename(columns = {df.columns[0]: 0, df.columns[1]: 1, df.columns[2]: 2, df.columns[3]: 3, df.columns[4]: 4, df.columns[5]: 5, df.columns[6]: 6, df.columns[7]: 7})

#Creating lists of votes and names
votes = []
names = []
for column in df_new:
    if (column + 2) % 2 == 0:
        for row in df_new[column][3:43]:
            if row != "":
                votes.append(row)
    else:
        for row in df_new[column][3:43]:
            if row != "":
                names.append(row)

#Creating dataframe out of lists
data = list(zip(names, votes))
df_final = pd.DataFrame(data, columns = ["Name", "Vote"])


#Need to generalize to work for any roll call sheet - call from API?

#Just combined all the above code into a function
def parse_pdf(file_path):
    doc = pymupdf.open(file_path)
    page1 = doc[0]
    tables = page1.find_tables(strategy = "text")
    table1 = tables[0]
    df = table1.to_pandas()
    df_new = df.rename(columns = {df.columns[0]: 0, df.columns[1]: 1, df.columns[2]: 2, df.columns[3]: 3, df.columns[4]: 4, df.columns[5]: 5, df.columns[6]: 6, df.columns[7]: 7})

    votes = []
    names = []
    for column in df_new:
        if (column + 2) % 2 == 0:
            for row in df_new[column][3:43]:
                if row != "":
                    votes.append(row)
        else:
            for row in df_new[column][3:43]:
                if row != "":
                    names.append(row)

    data = list(zip(names, votes))
    return (pd.DataFrame(data, columns = ["Name", "Vote"]))

#Trying with more data:
# print(parse_pdf("/Users/avivafoster/ds701/ds-act-on-mass/fa25-team-a/combined2025_RollCalls.pdf"))
#Isn't working since the new document was read in with more/inconsistent columns
#Would PyPDF2 be more useful after all?? Maybe using regexes etc...