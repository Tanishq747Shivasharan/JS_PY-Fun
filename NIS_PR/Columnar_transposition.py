# Simple Columnar Transposition Encryption

text = input("Enter Plain Text: ")
key = input("Enter Key: ")

col = len(key)
text_len = len(text)

# Calculate number of rows
row = text_len // col
if text_len % col != 0:
    row += 1

# Fill matrix row-wise
matrix = []
k = 0

for i in range(row):
    temp = []
    for j in range(col):
        if k < text_len:
            temp.append(text[k])
            k += 1
        else:
            temp.append('X')   # Padding
    matrix.append(temp)

# Encryption: Read column-wise
cipher = ""

for i in range(col):
    for j in range(row):
        cipher += matrix[j][i]

print("Encrypted Text:", cipher)
