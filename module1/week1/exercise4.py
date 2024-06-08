# -*- coding: utf-8 -*-
"""excercise4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16FmySsiX8dhueg8-iVYwmzxiKpt-9sCB
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def approx_sin(x, n):
  sum = 0
  for i in range(n):
    sum = sum + ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
  return sum
def approx_cos(x, n):
  sum = 0
  for i in range(n):
    sum = sum + ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
  return sum
def approx_sinh(x, n):
  sum = 0
  for i in range(n):
    sum = sum + (x ** (2 * i + 1)) / factorial(2 * i + 1)
  return sum
def approx_cosh(x, n):
  sum = 0
  for i in range(n):
    sum = sum + (x ** (2 * i)) / factorial(2 * i)
  return sum

approx_cos ( x =3.14 , n =10)

