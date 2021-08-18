def merge_values(original: dict, new_values: dict):
  """
if a value in a dictionary is also
a dictionary we want to keep the old
information inside it
  """
  for key, value in new_values.items():
    if isinstance(value, dict):
      original[key] = merge_values(original.get(key, dict()), value)
    else:
      original[key] = value
  return original
