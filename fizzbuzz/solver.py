# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from fizzbuzz import FizzBuzz


class Int2String(ABC):
	@abstractmethod
	def convert(self, number):
		pass
		
class Displayer(ABC):
	@abstractmethod
	def display(self, number):
		pass


class ProblemSolver(Int2String, Displayer):
	
	def convert(self, number):
		return FizzBuzz.convert(self, number)

	def display(self, number):
		for i in range(1, number+1):
			resultat = self.convert(i)
			print(resultat, end=" ")
			

#problemSolver = ProblemSolver()
#problemSolver.display(100)
