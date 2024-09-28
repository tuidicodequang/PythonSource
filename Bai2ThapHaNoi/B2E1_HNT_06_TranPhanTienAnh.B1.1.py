# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 07:59:40 2024 
@author: 06_TranPhanTienAnh
"""
def in_so_nguyen_to():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < 100:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    print("100 số nguyên tố đầu tiên của quý vị là:", primes)

if __name__ == "__main__":
    in_so_nguyen_to()
