def for_three():
        """ Number pattern '3' using Python for loop"""
        for row in range(7):
                for col in range(4):
                        if row%3==0 and col>0 and col<3 or col==3 and row%3!=0 or col==0 and row in (1,5):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_three():
                
        """ Number pattern '3' using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<4:
                        if row%3==0 and col>0 and col<3 or col==3 and row%3!=0 or col==0 and row in (1,5):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

