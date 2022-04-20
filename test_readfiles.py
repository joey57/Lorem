from distutils import text_file
import unittest
import readfiles

class TestReadFiles(unittest.TestCase):
  '''
  Class to test the functions on the readfiles module
  Args:unittest.TestCase: class from the unittest module to create unit tests
  '''
  def test_get_data(self):
    '''
    Test case to confirm that we are getting data from the file
    '''
    with open("test.txt", "r")as handle:
      data = handle.read()
      self.assertEqual(data,readfiles.read_file("test.txt"))

  def test_get_count(self):
    '''
    Test case to count how many times a word being used 
    '''    
    with open("test.txt", "r") as handle:
      data = handle.read()
      self.assertEqual(data,readfiles.count_file("test.txt"))
  

  def test_nonfile(self):
    '''
    Test to confirm that an exception is raised when a wrong file is inputted
    '''    
    self.assertEqual(None,readfiles.read_file("tests.txt"))


if __name__ == "__main__":
    unittest.main()   