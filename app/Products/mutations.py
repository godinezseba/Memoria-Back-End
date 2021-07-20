mutations = f'''
  createCompany(values: CompanyInput!): Company

  createProductsByFile(file: String!, companyId: ID!, columns: JSON!, separator: String): Boolean
'''
