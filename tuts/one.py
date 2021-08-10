"""
This is a Fin Library

Author: SarathChandraC
E-Mail: csc111vs@gmail.com
"""

__author__ = "Sarath"
__email__ = "csc111vs@gmail.com"


class Person:
    """Person class for the library

    Attributes:
    -----------
    Private:
        __name : str
        This is a name
    Methods:
    --------
        get_older


    """
    def __init__(self, name, age, weight):
        """Constructor for Person

        :param name: The name of the person
        :param age: the age of the person
        :param weight: weight of the person
        """
        self.name = name
        self.age = age
        self.weight = weight

    def get_older(self, years):
        """Get older function
        :param years: how many years person is getting older
        :return: the new age

        """
        self.age += years
        return self.age