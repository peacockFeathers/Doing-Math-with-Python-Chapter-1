'''
Bit-Byte Unit Converter
'''

def bits_to_bytes():

    bits = input('Enter the number of bits, so I can convert them to bytes: ')
    bits = int(bits)
    print('{0} bits equals {1} bytes, {2} bits.'.format(bits, int(bits/8), bits%8)) 
    # Roadmap: 
    # * Convert between bps and kbps, mbps
    # * Singular/plural bit/bits; byte/byteså
    
if __name__ == '__main__':

    bits_to_bytes()
