# -*- coding: utf-8 -*-
"""exercise2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ozgwyi2KkSs3cBTPUTV8BVhSP_rl9Xp1
"""

import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))
def relu(x):
  if x > 0:
    return x
  else:
    return 0
def elu(x):
  if x > 0:
    return x
  else:
    return 0.01 * (math.exp(x) - 1)
def is_number(x):
  try:
    float(x)
  except ValueError:
    return False
  return True
def exercise2():
  x = input("Input x = ")
  if is_number(x) == False:
    print("x must be a number")
    return
  else:
    x = float(x)
    function = input("Input activation Function ( sigmoid | relu | elu ) : ")
    if (function == "sigmoid"):
      print(f"{function}: f({x}) = {sigmoid(x)}")
      return
    elif (function == "relu"):
      print(f"{function}: f({x}) = {relu(x)}")
      return
    elif (function == "elu"):
      print(f"{function}: f({x}) = {elu(x)}")
      return
    else:
      print(f"{function} is not supported")
print ( round ( sigmoid (3) , 2) )