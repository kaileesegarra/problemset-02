"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import tabulate

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def quadratic_multiply(x, y):
    # Base cases
    if x.decimal_val == 0 or y.decimal_val == 0:
        return 0

    if len(x.binary_vec) == 1 and len(y.binary_vec) == 1:
        return x.decimal_val * y.decimal_val

    # Pad binary vectors so they are equal and even in length
    x_vec, y_vec = pad(x.binary_vec, y.binary_vec)
    m = len(x_vec) // 2

    # Split x into a,b and y into c,d
    a, b = split_number(x_vec)
    c, d = split_number(y_vec)

    # Four recursive multiplications
    ac = quadratic_multiply(a, c)
    ad = quadratic_multiply(a, d)
    bc = quadratic_multiply(b, c)
    bd = quadratic_multiply(b, d)

    # ac * 2^(2m) + (ad + bc) * 2^m + bd
    return (
        bit_shift(BinaryNumber(ac), 2 * m).decimal_val
        + bit_shift(BinaryNumber(ad + bc), m).decimal_val
        + bd
    )

def subquadratic_multiply(x, y):
    # Base cases
    if x.decimal_val == 0 or y.decimal_val == 0:
        return 0

    if len(x.binary_vec) == 1 and len(y.binary_vec) == 1:
        return x.decimal_val * y.decimal_val

    # Pad binary vectors so they are equal and even in length
    x_vec, y_vec = pad(x.binary_vec, y.binary_vec)
    m = len(x_vec) // 2

    # Split x into a,b and y into c,d
    a, b = split_number(x_vec)
    c, d = split_number(y_vec)

    # Three recursive multiplications
    ac = subquadratic_multiply(a, c)
    bd = subquadratic_multiply(b, d)

    combined = subquadratic_multiply(
        BinaryNumber(a.decimal_val + b.decimal_val),
        BinaryNumber(c.decimal_val + d.decimal_val)
    )

    middle = combined - ac - bd

    # ac * 2^(2m) + middle * 2^m + bd
    return (
        bit_shift(BinaryNumber(ac), 2 * m).decimal_val
        + bit_shift(BinaryNumber(middle), m).decimal_val
        + bd
    )

## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 4

# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))
    
if __name__ == "__main__":
    compare_multiply()
