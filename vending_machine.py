'''
Even-Odd Vending Machine Challenge

input: integer
work: determine whether number is even or odd
output:
- 'even' or 'odd'
- next NEXT even or odd numbers
'''

def vend(input):

    NEXT = 9
    
    # If input is even, print 'even'
    if input % 2 == 0:
        print("even")
    else:
        print("odd")
        
    counter = 0    
    
    while counter < NEXT * 2:
        counter += 2
        print(input + counter)
        
if __name__ == '__main__':
    vend(2)
    vend(1)
