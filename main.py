"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time


class BinaryNumber:
  """ done """

  def __init__(self, n):
    self.decimal_val = n
    self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
    return ('decimal=%d binary=%s' %
            (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec):
  if len(binary_vec) == 0:
    return BinaryNumber(0)
  return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
  return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
  # append n 0s to this number's binary string
  return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
  # pad with leading 0 if x/y have different number of bits
  # e.g., [1,0] vs [1]
  if len(x) < len(y):
    x = ['0'] * (len(y) - len(x)) + x
  elif len(y) < len(x):
    y = ['0'] * (len(x) - len(y)) + y
  # pad with leading 0 if not even number of bits
  if len(x) % 2 != 0:
    x = ['0'] + x
    y = ['0'] + y
  return x, y

def subquadratic_multiply(x, y):
  return _subquadratic_multiply(x, y).decimal_val

def _subquadratic_multiply(x, y):
  xvec = x.binary_vec
  yvec = y.binary_vec
  xvec, yvec = pad(xvec, yvec)

  if x.decimal_val <= 1 and y.decimal_val <= 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)

  # 4 recursive calls
  x_left, x_right = split_number(xvec)
  y_left, y_right = split_number(yvec)
  # x_L * y_L
  left_product = _subquadratic_multiply(x_left, y_left)
  # x_R * y_R
  right_product = _subquadratic_multiply(x_right, y_right)
  # x_L + x_R
  left_right_sum = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
  # y_L + y_R
  right_left_sum = BinaryNumber(y_left.decimal_val + y_right.decimal_val)

  # (x_L + x_R) * (y_L + y_R)
  middle_term = _subquadratic_multiply(left_right_sum, right_left_sum)

  # (x_L + x_R) * (y_L + y_R) - (x_L * y_L) - (x_R * y_R)
  middle_term_complete = BinaryNumber(middle_term.decimal_val -
                                      left_product.decimal_val -
                                      right_product.decimal_val)

  # 2^{n/2} ((x_L + x_R) * (y_L + y_R) - (x_L * y_L) - (x_R * y_R))
  middle_term_shifted = bit_shift(middle_term_complete, len(xvec) // 2)

  # 2^n (x_L * y_L)
  left_product = bit_shift(left_product, len(xvec))

  return BinaryNumber(left_product.decimal_val +
                      middle_term_shifted.decimal_val +
                      right_product.decimal_val)


def time_multiply(x, y, f):
  start = time.time()
  # multiply two numbers x, y using function f
  return (time.time() - start) * 1000
