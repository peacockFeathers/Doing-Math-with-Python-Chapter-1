'''
Bit-Byte Unit Converter
'''

def bits_to_bytes():

    bits = input('Enter the number of bits, so I can convert them to bytes: ')
    bits = int(bits)
    print('{0} bits equals {1} bytes.'.format(bits, int(bits/8)))
    
if __name__ == '__main__':

    bits_to_bytes()
