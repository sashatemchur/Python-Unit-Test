import unittest
from pars import Pars
import json


    
class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = Pars()
        
    def test_file(self):
        with open("data.json", "r", encoding="UTF-8") as data:
            data = data.read()
        if data != '':
            return True
        self.assertEqual(self.calculator.pars(), True)
        
    def test_api(self):    
        with open("data.json", "r", encoding="UTF-8") as data: 
            output_data = json.load(data)
        self.assertEqual(self.calculator.api(), output_data)
        
        
if __name__ == "__main__":
    unittest.main()