# 17/04/2025

## INTRODUCTION

Hamming Code is an error-detection and error-correction coding technique used in digital communication and data storage systems. It was invented by Richard Hamming in 1950 to ensure that data transmitted over unreliable or noisy channels can be checked for errors and corrected if necessary.

### Key Concepts:
1. **Parity Bits**: Hamming Code introduces additional bits (called parity bits) into the data to help detect and correct errors. These parity bits are strategically placed in the data stream.

2. **Error Detection and Correction**: 
   - Hamming Code can detect up to **two-bit errors** and correct **one-bit errors**.
   - It uses a mathematical relationship between the parity bits and the data bits to identify the position of an error.

3. **Redundancy**: The number of parity bits required depends on the length of the data. For example, for `m` data bits, the number of parity bits `r` is determined by the formula:
   ```
   2^r >= m + r + 1
   ```
   This ensures that the code can cover all possible error scenarios.

4. **Positioning of Parity Bits**: Parity bits are placed at positions that are powers of 2 (e.g., 1, 2, 4, 8, etc.) in the binary representation of the data.

### Applications:
- Memory systems (e.g., ECC RAM)
- Satellite communication
- Data transmission over unreliable networks

### When not to use
Use Hamming for lightweight, single-bit protection in low-error environments.
Don’t use it when reliability, robustness, or detection is mission-critical.

## RESULTS
```c
// One error only
===========SUMMARY===========
Hamming code degree of 16 with 32 elements
Flip a bit at index 31 from 1 to 0 in encoded bits
Random origin = [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
Encoded =       [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
Fault array =   [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
Decoded =       [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
Demo completed

// Multiple errors but only one in each chunk
===========SUMMARY===========
Hamming code degree of 16 with 32 elements
Flipped bits at indices 24 and 33
Random origin = [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0]
Encoded =       [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
Fault array =   [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
Two bits in different chunks of 16 elements, able to correct:
Decoded =       [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0]
Demo completed

//  For >1 bits error in one chunk
===========SUMMARY===========
Hamming code degree of 16 with 32 elements
Flipped bits at indices 30 and 31
Random origin = [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0]
Encoded =       [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0]
Fault array =   [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0]
There is more than 1 bit error in one chunk, cant not correct
Demo completed
```