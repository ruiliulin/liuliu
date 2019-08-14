# 11-1 城市和国家 和11-2 人口数量
import unittest
from city_functions import city_country_name

class CnameTestCase(unittest.TestCase):

    def test_city_country(self):
        cname = city_country_name('santiago', 'chile')
        self.assertEqual(cname, 'Santiago, Chile')

    def test_city_country_population(self):
        cname = city_country_name('santiago', 'chile', 5000000)
        self.assertEqual(cname, "Santiago, Chile -population 5000000")

if __name__ == '__main__':
    unittest.main()