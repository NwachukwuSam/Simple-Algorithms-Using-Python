
def raiseToPower(number, power):
    answer=1
    for i in range(1, power):
        answer*=number
        return answer

raiseToPower(2,5)
