from pandas import DataFrame, qcut
from app.Products.schema.Product import ProductDAO


def create_label_global():
  products = ProductDAO().list()
  # create a dataframe
  map_deforestation = {1: 1, 2: 3, 3: 5}
  df = DataFrame(list(zip(
      [i['_id'] for i in products],
      [i['ratingData']['CO2'] for i in products],
      [i['ratingData']['water'] for i in products],
      [map_deforestation[i['ratingData']['deforestation']] for i in products]
  )), columns=['_id', 'CO2', 'water', 'deforestation'])
  # get the label for the footprints
  df['globalLabelCO2'] = qcut(df['CO2'], 5, labels=range(1, 6)).astype("int")
  df['globalLabelwater'] = qcut(
      df['water'], 5, labels=range(1, 6)).astype("int")
  # the final result
  df['globalLabel'] = (df
                       .loc[:, ['globalLabelCO2', 'globalLabelwater', 'deforestation']]
                       .mean(1)
                       .astype("int"))

  maped_products = [{
      '_id': row['_id'],
      'ratingData':
      {
          'globalLabelCO2': row['globalLabelCO2'],
          'globalLabelwater': row['globalLabelwater'],
          'globalLabel': row['globalLabel'],
      }} for _, row in df.iterrows()]

  ProductDAO().update_many(maped_products)
  return 'ok'
