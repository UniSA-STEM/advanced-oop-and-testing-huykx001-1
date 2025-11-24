"""
File: systemHealthRecord.py
Description: This module represents the systemHeathRecord. It's a record for proving any illness/injuries.
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

    # Getters for the private attributes.
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_severity_level(self):
        return self.__severity_level

    def get_treatment(self):
        return self.__treatment

    # String conversion to print out the attributes.
    def __str__(self):
        return (f"\nname: {self.__name}\n"
                f"desc: {self.__description}\n"
                f"date: {self.__date}\n"
                f"severity: {self.__severity_level}\n"
                f"treatment: {self.__treatment}")
