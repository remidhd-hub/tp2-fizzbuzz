# -*- coding: utf-8 -*-

class FizzBuzz:

    def convert(self, number):
        """Retourne 'Fizz', 'Buzz', 'FizzBuzz' ou le nombre"""
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)


