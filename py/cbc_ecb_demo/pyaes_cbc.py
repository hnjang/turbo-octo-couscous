#!/usr/bin/python3

import sys
import os
import pyaes

# A 256 bit (32 byte) key
key = b"This_key_for_demo_purposes_only!"

# For some modes of operation we need a random initialization vector
# of 16 bytes
iv = b"InitializationVe"

aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
plaintext = b"TextMustBe16Byte"
ciphertext = aes.encrypt(plaintext)

# '\xd6:\x18\xe6\xb1\xb3\xc3\xdc\x87\xdf\xa7|\x08{k\xb6'
print (repr(ciphertext))


# The cipher-block chaining mode of operation maintains state, so
# decryption requires a new instance be created
aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
decrypted = aes.decrypt(ciphertext)

# True
print (decrypted == plaintext)

