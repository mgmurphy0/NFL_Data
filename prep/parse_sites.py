# https://towardsdatascience.com/using-machine-learning-to-predict-fantasy-football-points-72f77cb0678a
# https://towardsdatascience.com/scraping-nfl-stats-to-compare-quarterback-efficiencies-4989642e02fe

# Import scraping modules
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Import data manipulation modules
import pandas as pd

import requests


def pull_team_data():

  '''Pull team data from pro football reference'''

  ## TODO: Finish creating this function. Include team as input.

  url = 'https://www.pro-football-reference.com/teams/buf/2020.htm'
  html = requests.get(url)

  stats_page = BeautifulSoup(html.content,'html.parser')

  column_headers = stats_page.find_all('tr')[0]
  column_headers = [i.getText() for i in column_headers.findAll('th')]
  print(column_headers)


def pull_qb_data() -> pd.DataFrame:
  
  '''Pull quarterback data from pro football reference'''
  
  # URL of page
  url = 'https://www.pro-football-reference.com/years/2020/passing.htm'
  html = requests.get(url)

  stats_page = BeautifulSoup(html.content,'html.parser')

  column_headers = stats_page.find_all('tr')[0]
  column_headers = [i.getText() for i in column_headers.findAll('th')]
  print(column_headers)

  # Collect table rows
  rows = stats_page.findAll('tr')[1:]

  # Get stats from each row
  qb_stats = []
  for i in range(len(rows)):
    qb_stats.append([col.getText() for col in rows[i].findAll('td')])
  data = pd.DataFrame(qb_stats,columns=column_headers[1:])

  # Rename sack yards column to `Yds_Sack`
  new_columns = data.columns.values
  new_columns[-6] = 'Yds_Sack'
  data.columns = new_columns

  return data

def pull_rb_data() -> pd.DataFrame:

  '''Pull runningback data from pro football reference'''

  # URL of page
  url = 'https://www.pro-football-reference.com/years/2020/rushing.htm'
  html = requests.get(url)

  stats_page = BeautifulSoup(html.content,'html.parser')

  column_headers = stats_page.find_all('tr')[1]
  column_headers = [i.getText() for i in column_headers.findAll('th')]
  print(column_headers)

  # Collect table rows
  rows = stats_page.findAll('tr')[2:]

  # Get stats from each row
  rb_stats = []
  for i in range(len(rows)):
    rb_stats.append([col.getText() for col in rows[i].findAll('td')])
  data = pd.DataFrame(rb_stats,columns=column_headers[1:])
  
  # Remove all non running backs
  data = data[(data['Pos'] == 'RB') | (data['Pos'] == 'rb')]

  return data

def pull_rec_data(position: str is None) -> pd.DataFrame:

  '''Pull receiving data from pro football reference
  Inputs: position - rb, wr, or te to specify which position group to look at'''

  # URL of page
  url = 'https://www.pro-football-reference.com/years/2020/receiving.htm'
  html = requests.get(url)

  stats_page = BeautifulSoup(html.content,'html.parser')

  column_headers = stats_page.find_all('tr')[0]
  column_headers = [i.getText() for i in column_headers.findAll('th')]
  print(column_headers)

  # Collect table rows
  rows = stats_page.findAll('tr')[1:]

  # Get stats from each row
  rec_stats = []
  for i in range(len(rows)):
    rec_stats.append([col.getText() for col in rows[i].findAll('td')])
  data = pd.DataFrame(rec_stats,columns=column_headers[1:])

  if position == 'rb':
    # Remove all non running backs
    data = data[(data['Pos'] == 'RB') | (data['Pos'] == 'rb')]
  elif position == 'wr':
    # Remove all non wide receivers
    data = data[(data['Pos'] == 'WR') | (data['Pos'] == 'wr')]
  elif position == 'te':
    # Remove all non tight ends
    data = data[(data['Pos'] == 'TE') | (data['Pos'] == 'te')]
  if None:
    # Remove all non running backs
    data = data[(data['Pos'] == 'WR') | (data['Pos'] == 'wr') | (data['Pos'] == 'TE') | (data['Pos'] == 'te')]

  return data

def pull_fantasy_data():

  '''Pull fantasy data from pro football reference for all players'''

  # URL of page
  url = 'https://www.pro-football-reference.com/years/2020/fantasy.htm'
  html = requests.get(url)

  stats_page = BeautifulSoup(html.content,'html.parser')

  column_headers = stats_page.find_all('tr')[1]
  column_headers = [i.getText() for i in column_headers.findAll('th')]
  print(column_headers)

  # Collect table rows
  rows = stats_page.findAll('tr')[1:]

  # Get stats from each row
  stats = []
  for i in range(len(rows)):
    stats.append([col.getText() for col in rows[i].findAll('td')])
  data = pd.DataFrame(stats,columns=column_headers[1:])

  return data