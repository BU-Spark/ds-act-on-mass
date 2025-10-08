##Trying out different PDF parsing libraries

"""
#Tabula:
import tabula

test1_df = tabula.read_pdf("/Users/avivafoster/ds701/ds-act-on-mass/fa25-team-a/HouseRollCall25.pdf", pages = "all")
print(test1_df)

#Outcome has a lot of NaN instead of names
"""

"""
#pdfPlumber
import pdfplumber

test2_df = pdfplumber.open("/Users/avivafoster/ds701/ds-act-on-mass/fa25-team-a/HouseRollCall25.pdf")
print(test2_df.chars)

#Seems annoying to use
"""

"""
#PyPDF2; referenced https://www.geeksforgeeks.org/python/introduction-to-python-pypdf2-library/
import PyPDF2

with open("/Users/avivafoster/ds701/ds-act-on-mass/fa25-team-a/HouseRollCall25.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    text = reader.pages[0].extract_text()
    print(text)

#Seems really useful?? Outputs full lines from PDF. Though I'm not sure why the votes are after the names, I'm not mad about it
"""

#PyMuPDF
import pymupdf
import pandas as pd

doc = pymupdf.open("/Users/avivafoster/ds701/ds-act-on-mass/fa25-team-a/HouseRollCall25.pdf")
for page in doc:
    text = page.get_text()
    print(text)

#Outputs individual values from PDF, which I think would be the most useful/easy to manipulate as needed

#Referenced https://artifex.com/blog/extracting-tables-from-pdfs-with-pymupdf
page1 = doc[0]
tables = page1.find_tables(strategy = "text")
table1 = tables[0]
df = table1.to_pandas()
print(df)

print(df.shape) #Need to reshape/restructure to be just two columns, name and vote

#Need to generalize to work for any roll call sheet - call from API?