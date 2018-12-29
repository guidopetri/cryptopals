#!/usr/bin/env python3
#python 3.6.5

# Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it the string:

# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:

# 686974207468652062756c6c277320657965
# ... should produce:

result = b"746865206b696420646f6e277420706c6179"

import codecs

def combine_xor(str1,str2):
	"Combine str1 and str2 (both hex) via XOR."
	import codecs
	buf1 = codecs.decode(str1,"hex")
	buf2 = codecs.decode(str2,"hex")
	buf1 = int.from_bytes(buf1,byteorder='big')
	buf2 = int.from_bytes(buf2,byteorder='big')
	buf3 = (buf1 ^ buf2)
	buf3 = buf3.to_bytes(18,byteorder='big')
	return codecs.encode(buf3,"hex")

str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"

buf1 = codecs.decode(str1,"hex")
buf2 = codecs.decode(str2,"hex")

buf3 = combine_xor(buf1,buf2)
str3 = codecs.encode(buf3,"hex")

assert str3 == result
print("Test passed")

