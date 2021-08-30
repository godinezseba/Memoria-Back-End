from pandas import DataFrame, qcut
from app.Products.schema.Product import ProductDAO


def create_labels(products: list, label_name: str):
  # create a dataframe
  map_deforestation = {1: 1, 2: 3, 3: 5}
  df = DataFrame(list(zip(
      [i['_id'] for i in products],
      [i['ratingData']['CO2'] for i in products],
      [i['ratingData']['water'] for i in products],
      [map_deforestation[i['ratingData']['deforestation']] for i in products]
  )), columns=['_id', 'CO2', 'water', 'deforestation'])
  # get the label for the footprints
  df['labelCO2'] = qcut(df['CO2'], 5, labels=range(1, 6)).astype("int")
  df['labelwater'] = qcut(
      df['water'], 5, labels=range(1, 6)).astype("int")
  # the final result
  df['label'] = (df
                 .loc[:, ['labelCO2', 'labelwater', 'deforestation']]
                 .mean(1))

  mapped_products = [{
      '_id': row['_id'],
      label_name:
      {
          'labelCO2': row['labelCO2'],
          'labelwater': row['labelwater'],
          'label': row['label'],
      }} for _, row in df.iterrows()]

  return mapped_products


def create_label_category(category: str):
  products = ProductDAO().list({'category': category})
  ProductDAO().update_many(create_labels(products, 'categoryLabels'))
  return 'ok'


def create_label_global():
  products = ProductDAO().list()
  ProductDAO().update_many(create_labels(products, 'globalLabels'))
  return 'ok'
