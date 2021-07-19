queries = '''
  companies: [Company]
  company(id: String!): Company

  """
  Get a list with products, depends in the filter used
  """
  products: [Product]
  product(id: String!): Product
'''
