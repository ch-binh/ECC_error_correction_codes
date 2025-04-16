import numpy
import math


def exp_of_2(n: int):
    if n <= 0 or (n & (n - 1)) != 0:  # negative or not power of 2
        return False, None
    # Count the position of the only set bit
    exponent = 0
    while n > 1:
        n >>= 1
        exponent += 1
    return exponent


def is_power_of_2(n: int):
    return n > 0 and (n & (n - 1)) == 0


def set_parity_bits(chunk, dim):
    bit_idx = 1
    while (bit_idx < dim):
        parity = 0
        for idx, val in enumerate(chunk):
            if idx & bit_idx == bit_idx and val:
                parity ^= 1
        chunk[bit_idx] = parity
        bit_idx *= 2


def set_overall_parity(chunk):
    chunk[0] = sum(chunk[1:]) % 2


def hamming_encode(num_array: list[int], dim: int):
    chunk = []
    bit_idx = 0
    hamming_array = []
    hamming_array_len = len(num_array) + (1 + int(math.log(dim, 2))) * (int(
        len(num_array) / dim))
    
    print(hamming_array_len)
    # padding 0
    num_array = list(num_array)
    for _ in range(dim - (hamming_array_len % dim)):
        num_array.append(0)

    for val in num_array:
        while (bit_idx == 0 or is_power_of_2(bit_idx)):
            chunk.append(0b0)
            bit_idx += 1
        chunk.append(int(val))
        bit_idx += 1
        if bit_idx == dim:
            # fill in the parity
            set_parity_bits(chunk, dim)
            # Overall parity at position 0 (optional depending on spec)
            set_overall_parity(chunk)
            hamming_array.extend(chunk)
            chunk = []
            bit_idx = 0

    return hamming_array


def hamming_code_demo():
    #while True:
    matrix_dim = int(input("Input matrix dimension (ex 16, 32, 64, 128...): "))

    bits = numpy.random.randint(0, 2, matrix_dim)
    print(bits)

    result = hamming_encode(bits, 16)
    print(result)
    print(len(result))


if __name__ == "__main__":
    print("Hello me")
    hamming_code_demo()
