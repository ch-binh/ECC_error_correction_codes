import numpy

from hamming import *


def hamming_code_demo_1_bit_error(degree: int, num_e: int):
    # 1. input
    hamming_degree = degree
    number_of_e = num_e

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
    if decoded_bits == [0]:
        print("There is more than 1 bit error, cant not correct")
    else:
        print(f"Decode completed, here is the original number array")
        print(
            f"Decoded = {decoded_bits[:number_of_e]}")  #ignoring padding bits
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


def hamming_code_demo_2_bits_error(degree: int, num_e: int):
    # 1. input
    hamming_degree = degree
    number_of_e = num_e

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

    # 3. Flip 2 bits to simulate an bit error
    fault_bits = encoded_bits.copy()

    bit1, bit2 = numpy.random.choice(len(encoded_bits), size=2, replace=False)
    fault_bits[bit1] ^= 1
    fault_bits[bit2] ^= 1
    print(f"Flipped bits at indices {bit1} and {bit2}")
    print(f"Fault array = {fault_bits}")

    # 4. Decoding
    print(f"Decoding number array...")
    decoded_bits = hamming_decode(fault_bits, hamming_degree)
    
    
    print("===========SUMMARY===========")
    print(
        f"Hamming code degree of {hamming_degree} with {number_of_e} elements")
    print(f"Flipped bits at indices {bit1} and {bit2}")
    print(f"Random origin = {[int(b) for b in origin_bits]}")
    print(f"Encoded =       {encoded_bits}")
    print(f"Fault array =   {fault_bits}")
    
    if decoded_bits == [0]:
        print("There is more than 1 bit error in one chunk, cant not correct")
        print("Demo completed")
        return
    print(f"Two bits in different chunks of {hamming_degree} elements, able to correct:")
    print(f"Decoded =       {decoded_bits[:number_of_e]}")
    print("Demo completed")


if __name__ == "__main__":
    hamming_degree = int(
        input("Input hamming degree (ex 16, 32, 64, 128...): "))

    number_of_e = int(
        input("Input number of elements in the array (> hamming degree): "))

    print("========================================================")
    print("=========================DEMO1==========================")
    hamming_code_demo_1_bit_error(hamming_degree, number_of_e)
    print("========================================================")
    print("=========================DEMO2==========================")
    hamming_code_demo_2_bits_error(hamming_degree, number_of_e)
