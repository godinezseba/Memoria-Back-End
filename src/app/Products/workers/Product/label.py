from pandas import DataFrame, qcut
from numpy import isnan, nan

from app.Products.schema.Product import ProductDAO
from app.Products.schema.Company import CompanyDAO


def define_labels(df: DataFrame, column: str):
  not_null = df[column].notnull()
  df.loc[not_null, f'label{column}'] = qcut(
      df[column][not_null], 5, labels=range(1, 6), duplicates='drop').astype("int")


def map_deforestation(value):
  dict_deforestation = {1: 1, 2: 3, 3: 5, 1.0: 1, 2.0: 3, 3.0: 5}
  try:
    return dict_deforestation[value]
  except:
    return None


def create_labels(products: list, label_name: str):
  # create a dataframe
  df = DataFrame(list(zip(
      [i['_id'] for i in products],
      [i['ratingData']['CO2'] for i in products],
      [i['ratingData']['water'] for i in products],
      [map_deforestation(i['ratingData']['deforestation']) for i in products],
      [i['companyId'] for i in products],
  )), columns=['_id', 'CO2', 'water', 'deforestation', 'companyId'])
  # get the label for the footprints
  define_labels(df, 'CO2')
  define_labels(df, 'water')
  # the final result
  df['label'] = (df
                 .loc[:, ['labelCO2', 'labelwater', 'deforestation']]
                 .mean(1))

  # check the case with null values
  companiesId = df[
      df['CO2'].isnull()
      | df['water'].isnull()
      | df['deforestation'].isnull()]['companyId'].unique().tolist()
  if len(companiesId) > 0:
    companies = CompanyDAO().list(filters={'ids': companiesId})
    companies_map = {str(company['_id']): company['labels']['label']
                     if company.get('labels') else 5.0 for company in companies}

    def check_label(row):
      product = row.to_dict()
      f = (isnan(product['labelCO2'])
           + isnan(product['labelwater'])
           + isnan(product['deforestation'])) / 3
      if f != 0:
        return ((1 - f) * product['label']) + (f * companies_map[product['companyId']])
      return product['label']
    df['label'] = [check_label(row) for _, row in df.iterrows()]

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
