#!/usr/bin/env python3
#python 3.6.5

decode_this = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
import codecs

def combine_xor(str1,str2):
	"Combine str1 and str2 (both hex) via XOR."
	import codecs
	buf1 = codecs.decode(str1,"hex")
	buf2 = codecs.decode(str2,"hex")
	buf1 = int.from_bytes(buf1,byteorder='big')
	buf2 = int.from_bytes(buf2,byteorder='big')
	buf3 = (buf1 ^ buf2)
	buf3 = buf3.to_bytes(50,byteorder='big')
	return codecs.encode(buf3,"hex")

hexcharlist = [x for x in range(0,10)]+['a','b','c','d','e','f']

hexchars = [str(x)+str(y) for x in hexcharlist for y in hexcharlist]

for character in hexchars:
	print(character)
	result = combine_xor(decode_this,character)
	print(result)
