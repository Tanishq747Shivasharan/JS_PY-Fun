# Rail Fence Cipher Encryption
def rail_fence_encrypt(text, rails):
    # Create empty rails
    fence = []
    for i in range(rails):
        fence.append(["\n"] * len(text))

    direction_down = False
    row = 0
    col = 0
    # Fill characters in zig-zag
    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        fence[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1
    # Read rail-wise to get cipher
    result = ""
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] != "\n":
                result += fence[i][j]
    return result

# ---- Main Program ----
text = input("Enter Text: ")
rails = int(input("Enter Number of Rails: "))

encrypted = rail_fence_encrypt(text, rails)

print("Encrypted Text:", encrypted)