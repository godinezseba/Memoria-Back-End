mutations = '''
  """
  Only admin users can create companies
  """
  createCompany(values: CompanyInput!): Company

  """
  Endpoint that create multiple products of a company,
  by the moment its only csv in base64
  """
  createProductsByFile(values: ProductFileInput!): Boolean
  updateProduct(id: ID!, data: ProductInput): Product
'''
