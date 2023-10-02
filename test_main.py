from main.py import *


## Feel free to add your own tests here.
def test_multiply():
  assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2

  assert quadratic_multiply(BinaryNumber(15), BinaryNumber(15)) == 15 * 15
  assert quadratic_multiply(BinaryNumber(64), BinaryNumber(64)) == 64 * 64
  assert quadratic_multiply(BinaryNumber(310), BinaryNumber(290)) == 310 * 290
