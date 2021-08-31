mutations = '''
  """
  Only admin users can create/update companies
  """
  createCompany(values: CompanyInput!): Company
  updateCompany(id: ID!, values: CompanyInput!): Company

  """
  Only admin users can create certifiers
  """
  createCertifier(values: CertifierInput!): Certifier

  """
  Endpoint that create multiple products of a company,
  by the moment its only csv in base64
  """
  createProductsByFile(values: ProductFileInput!): Boolean
  updateProduct(id: ID!, data: ProductInput): Product
'''
