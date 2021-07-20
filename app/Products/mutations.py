mutations = '''
  """
  Only admin users can create companies
  """
  createCompany(values: CompanyInput!): Company

  """
  Endpoint that create multiple products of a company,
  by the moment its only csv in base64
  """
  createProductsByFile(file: String!, companyId: ID!, columns: JSON!, separator: String): Boolean
'''
