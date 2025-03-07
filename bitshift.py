def multiply(a, b):
    # Explanation: In binary, each digit represents a power of 2. Left-shifting a number by n positions appends n zeros to its binary representation. For example, 5 (binary 101) shifted left by 1 becomes 1010 (10 in decimal), equivalent to 5 × 2¹ = 10. Each left shift doubles the number, so shifting by n positions multiplies the original number by 2ⁿ.
    result = 0
    while b > 0:
        if b & 1: 
            result += a
        a = a << 1 
        b = b >> 1 
    return result

