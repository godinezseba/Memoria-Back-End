from pandas import DataFrame, qcut
from app.Products.schema.Company import CompanyDAO


def create_label():
  companies = CompanyDAO().list()
  # create a dataframe
  map_deforestation = {1: 1, 2: 3, 3: 5}
  df = DataFrame(list(zip(
      [i['_id'] for i in companies],
      [i['ratingData']['CO2'] for i in companies],
      [i['ratingData']['water'] for i in companies],
      [map_deforestation[i['ratingData']['deforestation']] for i in companies]
  )), columns=['_id', 'CO2', 'water', 'deforestation'])
  # get the label for the footprints
  df['labelCO2'] = qcut(df['CO2'], 5, labels=range(1, 6)).astype("int")
  df['labelwater'] = qcut(
      df['water'], 5, labels=range(1, 6)).astype("int")
  # the final result
  df['label'] = (df
                 .loc[:, ['labelCO2', 'labelwater', 'deforestation']]
                 .mean(1)
                 .astype("int"))

  mapped_companies = [{
      '_id': row['_id'],
      'labels':
      {
          'labelCO2': row['labelCO2'],
          'labelwater': row['labelwater'],
          'label': row['label'],
      }} for _, row in df.iterrows()]

  CompanyDAO().update_many(mapped_companies)
  return 'ok'
