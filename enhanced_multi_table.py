'''
Multiplication table printer
'''

def multi_table(n, rows):
    
    rows += 1 # The range function doesn't print the last iteration it reaches.
    '''
    For example: a 5 x 5 table would only get up to 5 x 4 = 20 without the above line.
    '''
    
    for i in range(1, rows):
        print('{0} x {1} = {2}'.format(n, i, n*i))
        
if __name__ == '__main__':
    number = input('Enter a number to print its multiplication table: ')
    rows = input('Enter the number of rows the multiplication table should be: ')
    
    multi_table(float(number), int(rows))
