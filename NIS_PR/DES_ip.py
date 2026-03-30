# DES Initial Permutation (IP)

# Standard DES IP Table (1-indexed)
IP = [
    58, 50, 42, 34, 26, 18, 10,  2,
    60, 52, 44, 36, 28, 20, 12,  4,
    62, 54, 46, 38, 30, 22, 14,  6,
    64, 56, 48, 40, 32, 24, 16,  8,
    57, 49, 41, 33, 25, 17,  9,  1,
    59, 51, 43, 35, 27, 19, 11,  3,
    61, 53, 45, 37, 29, 21, 13,  5,
    63, 55, 47, 39, 31, 23, 15,  7
]

def apply_initial_permutation(hex_input):
    # Step 1: Convert hex to 64-bit binary string
    bin_str = bin(int(hex_input, 16))[2:].zfill(64)

    print(f"Hex Input      : {hex_input.upper()}")
    print(f"Binary Input   : {bin_str}")

    # Step 2: Apply the IP table (1-indexed, so subtract 1)
    output_bits = ""
    for pos in IP:
        output_bits += bin_str[pos - 1]

    print(f"Binary Output  : {output_bits}")

    # Step 3: Convert output bits back to hex
    output_hex = hex(int(output_bits, 2))[2:].upper().zfill(16)
    print(f"Hex Output     : {output_hex}")

    return output_hex

# Input: 0X0003 0000 0000 0001
hex_input = "0003000000000001"
apply_initial_permutation(hex_input)