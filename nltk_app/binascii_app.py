import binascii

text = "Simply Easy Learning"
text = str.encode(text)

# Converting binary to ascii
data_b2a = binascii.b2a_uu(text)
print("**Binary to Ascii**")
print(data_b2a)

# Converting back from ascii to binary
data_a2b = binascii.a2b_uu(data_b2a)
print("**Ascii to Binary**")
print(data_a2b)
