import time
import math

from primelib.primelib import generate_prime_list2


class DigitCancellingFractions:

    def __init__(self):
        self.combination = []
        self.fraction_example = list()
        self.answer = 0
        self.prime_list = generate_prime_list2(25)

    def run1(self):
        for numerator_count in range(10,100):
            numerator_digit = str(numerator_count)
            for denominator_count in range(numerator_count+1,100):
                denominator_digit = str(denominator_count)
                if not(denominator_count % 10 == 0 or numerator_count % 10 == 0):
                    if (numerator_digit[0] == denominator_digit[0] and numerator_count/denominator_count == int(numerator_digit[1])/int(denominator_digit[1])) or \
                        (numerator_digit[0] == denominator_digit[1] and numerator_count/denominator_count == int(numerator_digit[1])/int(denominator_digit[0])) or \
                        (numerator_digit[1] == denominator_digit[0] and numerator_count/denominator_count == int(numerator_digit[0])/int(denominator_digit[1])) or \
                        (numerator_digit[1] == denominator_digit[1] and numerator_count/denominator_count == int(numerator_digit[0])/int(denominator_digit[0])):    
                    
                       self.fraction_example.append([numerator_count, denominator_count]) 
                     
        numerator = math.prod([fraction[0] for fraction in self.fraction_example])
        denominator = math.prod([fraction[1] for fraction in self.fraction_example])
        greatest_common_divisor = math.gcd(numerator, denominator)
        self.answer = denominator / greatest_common_divisor
    


if __name__ == "__main__":
    dcf = DigitCancellingFractions()
    tstart = time.time()
    dcf.run1()
    print('Answer = ',dcf.answer)
    tend = time.time()
    print('Run time for Q33 = ', tend - tstart, 's')

