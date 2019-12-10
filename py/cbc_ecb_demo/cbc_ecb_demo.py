#!/usr/bin/python3

import sys
import os
from PIL import Image
from Crypto.Cipher import AES
from Crypto import Random
#import argparse


def check_args():
    try:
        if (len(sys.argv) != 4):
            raise Exception()
        elif (not os.path.isfile(sys.argv[1])):
            raise Exception("Input file must exist")
        elif (not sys.argv[3] in ['CBC', 'ECB']):
            raise Exception("Block cipher mode should be ECB or CBC")
        return (sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as ex:
        print ("Usage: %s"% sys.argv[0] + \
          "full_path_to_input_image full_path_to_output_image ECB|CBC")
        if len(ex.args) > 0:
            print("--" + str(ex))
        sys.exit(1)


def encrypt(input_filename, output_filename, cipher_mode):
    input_image = Image.open(input_filename)
    key = '0123456789ABCDEF'
    BLOCK_SIZE = 16
    mode = AES.MODE_CBC if cipher_mode == 'CBC' else AES.MODE_ECB
    iv = Random.new().read(AES.block_size)

    aes = AES.new(key, mode, iv)

    image_string = input_image.tobytes()
    image_padding_length = BLOCK_SIZE - len(image_string) % BLOCK_SIZE
    image_string += bytes(image_padding_length * b'~')

    encrypted = aes.encrypt(image_string)

    # create an image from the encrypted string
    encrypted_img = Image.frombuffer('L', input_image.size, encrypted, 'raw',
                                     'L', 0, 1)
    encrypted_img.save(output_filename, 'PNG')
    print("Encrypted using AES in " + cipher_mode + " mode and saved to \"" +
          output_filename + "\"!")


if __name__ == "__main__":
    args = check_args()
    encrypt(*args)
