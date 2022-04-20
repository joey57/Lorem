from readfiles import text_file

def read_file():
   with open(text_file,"r") as handle:
    data = handle.read()
    return data

def main():
  print("Hello welcome to file handling")