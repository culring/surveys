"""
Contains the SingleAnswer class.
"""

import enum


class SingleAnswer(enum.Enum):
    """
    Enum specifying all possible answers to survey questions.
    """

    YES = 'T'
    NO = 'F'
    UNKNOWN = 'U'
