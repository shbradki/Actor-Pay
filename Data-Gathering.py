import csv
import pandas as pd

from bs4 import BeautifulSoup

import requests


data = pd.read_csv("Actor-Data.csv")


def Add_Row(CSV_File, Name, Pay, Title, Role, Year, Star, Costar, Genre):

    new_data = pd.DataFrame({
    'Actor': [Name],
    'Pay': [Pay],
    'Movie Title': [Title],
    'Role': [Role],
    'Year': [Year],
    'Star?': [Star],
    'Costar?': [Costar],
    'Genre': [Genre],
    })

    CSV_File = pd.concat([CSV_File, new_data], ignore_index=True)
    return CSV_File

#data = Add_Row(data, 'Selena Gomez', 150000, 'Montecarlo', 'Star', 2003, 'Yes', 'No', 'Drama')
#data.to_csv('Actor-Data.csv', index=False)

url1 = 'https://www.imdb.com/title/tt1067774/fullcredits?ref_=tt_ov_st_sm'

reqs = requests.get(url1)
soup = BeautifulSoup(reqs.text, 'lxml')
table = soup.find('table', 'cast_list')
# print(table)
# soup = BeautifulSoup(table.text , 'lxml')
all_a = soup.find('a')
print(all_a)




# print(data)
