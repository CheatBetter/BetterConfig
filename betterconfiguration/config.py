"""
Copyright 2023 CheatBetter

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Join Us
"""

"""

BetterConfig - CheatBetter

A easy to use configuration system for python, allows you to create custom config templates
and preset ones

"""

from typing import Optional, Any

"""

Base config class, used to build off more configuration classes for templates

"""

"""

   Gets a value from the variable the user sets
   :param name The name of the variable that has the value

"""


def get_value(self, name: str):
    getattr(self, name)


"""

   Creates a variable with the name and value you set
   :param name The name the variable will be
   :param value The value of the variable

"""


def create_value(self, name: str, value: Any):
    setattr(self, name, value)

class BaseConfig:
    """
    Base config class, takes up to 10 variables and values

    :param name Used to identify the config structure through name

    """
    def __init__(self, *args) -> None:
        if len(args) > 0:
            create_value(self, args[0], args[1])
        if len(args) > 2:
            create_value(self, args[2], args[3])
        if len(args) > 4:
            create_value(self, args[4], args[5])
        if len(args) > 6:
            create_value(self, args[6], args[7])
        if len(args) > 8:
            create_value(self, args[8], args[9])