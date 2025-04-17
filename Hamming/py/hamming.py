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


def hamming_decode(num_array: list[int], dim: int):
    chunks = []
    origin_num_array = []

    # seperate continuous data stream to chunk with dim elements
    for i in range(int(len(num_array) / dim)):
        chunks.append(num_array[i * dim:i * dim + dim])

    # process each chunk
    # if any chunk produce error, return False

    for c_idx, chunk in enumerate(chunks):
        bit_1_list = []
        parity_count = 0
        for idx, bit in enumerate(chunk):
            bit_1_list.append(idx) if bit else None

        for e in bit_1_list:
            parity_count ^= e

        if parity_count != 0:
            print(
                f"There is an error in encoded number array at idx {parity_count + dim*c_idx}"
            )
            print("Correcting the array...")
            chunks[c_idx][parity_count] ^= 0b01

    print(chunks)

    for chunk in chunks:
        for idx, bit in enumerate(chunk):
            if (not is_power_of_2(idx)) and (idx != 0):
                origin_num_array.append(bit)

    return origin_num_array


def hamming_code_demo():
    # 1. input
    hamming_degree = int(
        input("Input hamming degree (ex 16, 32, 64, 128...): "))

    number_of_e = int(
        input("Input number of elements in the array (> hamming degree): "))

    origin_bits = numpy.random.randint(0, 2, number_of_e)
    print(
        f"Generated a number array with {number_of_e} elements: \nOrigin = {origin_bits}"
    )

    # 2. encoding
    print(f"Encoding number array...")
    encoded_bits = hamming_encode(origin_bits, hamming_degree)
    print(
        f"Encode completed.\nHere is the hamming encoded version with {hamming_degree} degree: \nEncoded = {encoded_bits}"
    )

    # 3. Flip a bit to simulate an bit error
    fault_bits = encoded_bits.copy()

    error_bit = numpy.random.randint(0, number_of_e)
    fault_bits[error_bit] ^= 0b1
    print(
        f"Flip a bit at index {error_bit} from {encoded_bits[error_bit]} to {fault_bits[error_bit]}"
    )
    print(f"Fault array = {fault_bits}")

    # 4. Decoding
    print(f"Decoding number array...")
    decoded_bits = hamming_decode(fault_bits, hamming_degree)

    print(f"Decode completed, here is the original number array")
    print(f"Decoded = {decoded_bits[:number_of_e]}")  #ignoring padding bits
    # 5. Rechecking
    for idx, (e1, e2) in enumerate(zip(decoded_bits, origin_bits)):
        if e1 != e2:
            print("Recheck faied")
            print(
                f"Decoded array is different at bit {idx}: {e1} (expected) vs {e2} (decoded output)"
            )
            return

    # Done
    print("===========SUMMARY===========")
    print(
        f"Hamming code degree of {hamming_degree} with {number_of_e} elements")
    print(
        f"Flip a bit at index {error_bit} from {encoded_bits[error_bit]} to {fault_bits[error_bit]} in encoded bits"
    )
    print(f"Random origin = {[int(b) for b in origin_bits]}")
    print(f"Encoded =       {encoded_bits}")
    print(f"Fault array =   {fault_bits}")
    print(f"Decoded =       {decoded_bits[:number_of_e]}")

    print("Demo completed")


if __name__ == "__main__":
    hamming_code_demo()
