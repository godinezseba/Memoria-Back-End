queries = '''
  certifiers: [Certifier]

  companies: [Company]
  company(id: ID!): Company

  """
  Get a list with products, depends in the filter used
  """
  products(filters: ProductsFilters, sort: ProductSort): [Product]
  product(id: ID!): Product
'''
