# -*- coding: utf-8 -*-
"""
Created on Tue Mar 9 10:09:52 2021
@author: 06_TranPhanTienAnh
"""
def giai_pt_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        return f"Phương trình có nghiệm kép: {-b/(2*a)}"
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return f"Nghiệm thứ nhất: {x1}, Nghiệm thứ hai: {x2}"

if __name__ == "__main__":
    a = float(input("Quý vị vui lòng nhập a: "))
    b = float(input("Quý vị vui lòng nhập b: "))
    c = float(input("Quý vị vui lòng nhập c: "))
    print(f"Nghiệm của phương trình: {giai_pt_bac_2(a, b, c)}")
