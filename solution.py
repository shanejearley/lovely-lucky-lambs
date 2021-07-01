def henchmenAreNeeded(remaining_lambs, next_lamb_amount):
    return (remaining_lambs / next_lamb_amount) >= 1
    
def getNextCount(lamb_amount, prev_lamb_amount, method):
    methods = {
        'generous': lamb_amount * 2,
        'stingy': lamb_amount + prev_lamb_amount
    }
    return methods[method]
    
def getHenchmenCount(total_lambs, method):
    prev_lamb_amount = 0
    lamb_amount = 1
    henchman_count = 1
    remaining_lambs = total_lambs - lamb_amount
    next_lamb_amount = getNextCount(lamb_amount, prev_lamb_amount, method)
    while henchmenAreNeeded(remaining_lambs, next_lamb_amount):
        prev_lamb_amount = lamb_amount
        lamb_amount = next_lamb_amount
        henchman_count += 1
        remaining_lambs -= lamb_amount
        next_lamb_amount = getNextCount(lamb_amount, prev_lamb_amount, method)
    return henchman_count

def solution(total_lambs):
    stingy_count = getHenchmenCount(total_lambs, 'stingy')
    generous_count = getHenchmenCount(total_lambs, 'generous')
    return stingy_count - generous_count
