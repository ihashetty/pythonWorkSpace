"""Abstraction method"""


from abc import ABC, abstractmethod


class Electric(ABC):

    """abstract electronic class creayion"""
    @abstractmethod
    def play_vid(self):

        """playing video"""


class Laptop(Electric):

    """Laptop class"""

    def play_vid(self):

        """Playing video"""
        print("press play button from keyboard")


class Mobile(Electric):

    """mobile class"""
    def play_vid(self):

        """playing video"""
        print("press play button from keypad")


laptop = Laptop()
laptop.play_vid()

mobile = Mobile()
mobile.play_vid()
