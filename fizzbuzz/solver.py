# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from fizzbuzz import FizzBuzz


class Int2String(ABC):
	@abstractmethod
	def convert(self, number):
		pass
		
class Displayer(ABC):
	@abstractmethod
	def display(self, text):
		pass


class ProblemSolver:
	def __init__(self, converter:Int2String, displayer:Displayer):
		self.converter = converter
		self.displayer = displayer
	
	def solve(self, n=100):
		for i in range(1, n+1):
			text = self.converter.convert(i)
			self.displayer.display(text)
