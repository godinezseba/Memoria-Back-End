queries = '''
  """
  With the request.header.token the system check if
  it is valid, and then find the user by the uid
  """
  me: User

  """
  Only admin users can get users information
  """
  users: [User]
  user(id: ID): User
'''
