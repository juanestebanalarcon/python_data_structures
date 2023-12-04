'''
Author: juanestebanalarcon
Exercise: Recursive function
'''

def pyramid_sum(lower_,upper_,margin_=0):
    blanks_=" "*margin_
    print(blanks_,lower_,upper_)
    if lower_>upper_:
        print(blanks_,0)
        return 0
    else:
        result = lower_+pyramid_sum(lower_+1,upper_,margin_+4)
        print(blanks_,result)
        return result
pyramid_sum(1,4)
