"""
File: systemHealthRecord.py
Description: A brief description of this Python module.
Author: Kim Xuyen Huynh
ID: 110442620
Username: Huykx001
This is my own work as defined by the University's Academic Integrity Policy.
"""


class SystemHealthRecord:
    """
    Constructor for the class SystemHealthRecord with private attributes such as
    name, desc, date, severity level, and treatment
    """

    def __init__(self, name, date, description, severity_level, treatment):
        self.__name = name
        self.__description = description
        self.__date = date
        self.__severity_level = severity_level
        self.__treatment = treatment

    # String conversion to print out the attributes.
    def __str__(self):
        return (f"{self.__name}\n"
                f"{self.__description}\n"
                f"{self.__date}\n"
                f"{self.__severity_level}\n"
                f"{self.__treatment}")
