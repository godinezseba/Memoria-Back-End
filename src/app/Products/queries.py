queries = '''
  certifiers: [Certifier]

  companies: [Company]
  company(id: String!): Company

  """
  Get a list with products, depends in the filter used
  """
  products(filters: ProductsFilters): [Product]
  product(id: String!): Product
'''
