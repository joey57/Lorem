text_file = "test.txt"
def read_file(text_file):
  '''
  Function that reads a file and returns the data from the text file
  '''
  with open(text_file,"r") as handle:
    data = handle.read()
    return data

def count_file(text_file):
  '''
  Function that counts the number of times a word is used
  '''
  handle = open(text_file,"r")
  data = handle.read()
  counter = 0
  for word in data.split():
     if word == "Lorem":
       counter += 1
  return data

def read_file(text_file):
  '''
  Function that reads a text file and returns the data from the text file
  Raises: FileNotFoundError: If it cannot find the file
  '''
  try:
    with open(text_file,"r") as handle:
      data = handle.read()
      return data
  except FileNotFoundError:
    return None    