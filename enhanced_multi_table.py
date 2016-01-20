'''
Multiplication table printer
'''

def multi_table(n):
    
    ROWS = 12
    
    for i in range(1, ROWS):
        print('{0} x {1} = {2}'.format(n, i, n*i))
        
if __name__ == '__main__':
    number = input('Enter a number to print its multiplication table: ')
    multi_table(float(number))
