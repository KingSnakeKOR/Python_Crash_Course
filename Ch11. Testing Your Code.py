# 11-1
def city_country(city, country):
    #print(city.title() + ", " + country.title())
    return city.title() + ", " + country.title()

import unittest

class city_countryTestCase(unittest.TestCase):
    def test_city_country(self):
        xyz = city_country("seoul", "south korea")
        self.assertEqual(xyz, 'Seoul, South Korea')

unittest.main()

# 11-2
def city_country(city, country, population):
    return city.title() + ", " + country.title() + " - population " + str(population)

def city_country(city, country, population = ""):
    if population:
        return city.title() + ", " + country.title() + " - population " + str(population)
    else:
        return city.title() + ", " + country.title()

class city_countryTestCase(unittest.TestCase):
    def test_city_country(self):
        xyz = city_country("seoul", "south korea", 33363336)
        self.assertEqual(xyz, 'Seoul, South Korea - population 33363336')

# 11-3
class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary
        print(self.first_name + self.last_name + str(self.annual_salary))

    def give_raise(self, bonus = 5000):
        self.annual_salary += bonus
        print(self.first_name + self.last_name + str(self.annual_salary))

zyz = Employee('ryan', 'kim', 1000)
zyz.give_raise()
zyz.give_raise(3000)

import unittest

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.testing = Employee('ryan', 'kim', 1000)

    def test_give_default_raise(self):
        self.testing.give_raise()
        self.assertEqual(self.testing.annual_salary, 6000)

    def test_give_custom_raise(self):
        self.testing.give_raise(3000)
        self.assertEqual(self.testing.annual_salary, 4000)

unittest.main()