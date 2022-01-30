import pandas as pd

def clean_qb_data(data: pd.DataFrame, categories: list()):

  # Create data subset for radar chart
  data_radar = data[['Player', 'Tm'] + categories]
  print(data_radar.head())

  # all object in table are objects
  data_radar.dtypes

  # Convert data to numerical (floats) values
  for i in categories:
    data_radar[i] = pd.to_numeric(data[i])
  print(data_radar.head())

  # Filter by passing yards
  data_radar_filtered = data_radar[data_radar['Yds'] > 1500]
  data_radar_filtered = data_radar_filtered.reset_index(drop=True)

  # Remove ornamental characters for achievements (pro bowl / All pro)
  data_radar_filtered['Player'] = data_radar_filtered['Player'].str.replace('*', '')
  data_radar_filtered['Player'] = data_radar_filtered['Player'].str.replace('+', '')
  
  # Split first and last names

  data_radar_filtered.insert(1, 'First','N/A')
  data_radar_filtered.insert(1, 'Last','N/A')
  for i in range(len(data_radar_filtered)):
    data_radar_filtered['First'][i] = data_radar_filtered['Player'][i].split(' ')[0]
    data_radar_filtered['Last'][i] = data_radar_filtered['Player'][i].split(' ')[1]

  # Create columns with percentile rank
  for i in categories:
    data_radar_filtered[i + '_Rank'] = data_radar_filtered[i].rank(pct=True)
  # We need to flip the rank for interceptions
  data_radar_filtered['Int_Rank'] = 1 - data_radar_filtered['Int_Rank']

  return data_radar_filtered

def clean_rb_data(data: pd.DataFrame, categories: list()):

  # Create data subset for radar chart
  data_radar = data[['Player', 'Tm'] + categories]
  print(data_radar.head())

  # all object in table are objects
  data_radar.dtypes

  # Convert data to numerical (floats) values
  for i in categories:
    data_radar[i] = pd.to_numeric(data[i])
  print(data_radar.head())

  # Filter by passing yards
  data_radar_filtered = data_radar[(data_radar['Yds'] > 200)]
  data_radar_filtered = data_radar_filtered.reset_index(drop=True)

  # Remove ornamental characters for achievements (pro bowl / All pro)
  data_radar_filtered['Player'] = data_radar_filtered['Player'].str.replace('*', '')
  data_radar_filtered['Player'] = data_radar_filtered['Player'].str.replace('+', '')
  
  # Split first and last names

  data_radar_filtered.insert(1, 'First','N/A')
  data_radar_filtered.insert(1, 'Last','N/A')
  for i in range(len(data_radar_filtered)):
    data_radar_filtered['First'][i] = data_radar_filtered['Player'][i].split(' ')[0]
    data_radar_filtered['Last'][i] = data_radar_filtered['Player'][i].split(' ')[1]

  # Create columns with percentile rank
  for i in categories:
    data_radar_filtered[i + '_Rank'] = data_radar_filtered[i].rank(pct=True)
  # We need to flip the rank for age
  data_radar_filtered['Age'] = 1 - data_radar_filtered['Age']

  return data_radar_filtered

def clean_rec_data(data: pd.DataFrame, categories: list()):

  # Create data subset for radar chart
  data_radar = data[['Player', 'Tm'] + categories]
  print(data_radar.head())

  # all object in table are objects
  data_radar.dtypes

  # Convert data to numerical (floats) values
  data_radar['Ctch%'] = data_radar['Ctch%'].str.replace('%', '')
  for i in categories:
    data_radar[i] = pd.to_numeric(data_radar[i])
  print(data_radar.head())

  # Filter by passing yards
  data_radar_filtered = data_radar[(data_radar['Yds'] > 200)]
  data_radar_filtered = data_radar_filtered.reset_index(drop=True)

  # Remove ornamental characters for achievements (pro bowl / All pro)
  data_radar_filtered['Player'] = data_radar_filtered['Player'].str.replace('*', '')
  data_radar_filtered['Player'] = data_radar_filtered['Player'].str.replace('+', '')
  
  # Split first and last names

  data_radar_filtered.insert(1, 'First','N/A')
  data_radar_filtered.insert(1, 'Last','N/A')
  for i in range(len(data_radar_filtered)):
    data_radar_filtered['First'][i] = data_radar_filtered['Player'][i].split(' ')[0]
    data_radar_filtered['Last'][i] = data_radar_filtered['Player'][i].split(' ')[1]

  # Create columns with percentile rank
  for i in categories:
    data_radar_filtered[i + '_Rank'] = data_radar_filtered[i].rank(pct=True)

  return data_radar_filtered