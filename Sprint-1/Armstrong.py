import math
import string
class  Armstrong:
    def __init__(self):
        pass

    @staticmethod
    def is_armstrong( x: int) -> string:
        count = int(math.log10(x) + 1)
        totalsum = 0
        orgnumber =  x
        while orgnumber != 0:
            totalsum = totalsum + ( (orgnumber % 10 )** count)
            orgnumber = orgnumber//10

        if totalsum == n:
            return  str (n) + " is an armstrong number"
        else:
            return str(n) + " is not an armstrong number"

    @staticmethod
    def is_armstrong1(x: int) -> bool:
            count = len(str(x))
            total_sum = sum(int(digit) ** count for digit in str(n))  # Sum of powers
            return total_sum == x

    @staticmethod
    def find_armstrong(x : int , y : int) -> list[int]:
           #creating a list to store all armstrong numbers
           armstrong_list = []
           for number in range(x , y ):
               count = len(str(number))
               total_sum = sum( int(digit) ** count for digit in str(number))
               if total_sum == number:
                   armstrong_list.append(number)
           return armstrong_list

if __name__ == '__main__':
    n = int(input("Enter the number to check for Armstrong: "))
    obj1 = Armstrong()
    range1 = int(input("Enter the first range:"))
    range2 = int(input("Enter the second range:"))

    res = obj1.find_armstrong(range1 , range2)
    print(res)
