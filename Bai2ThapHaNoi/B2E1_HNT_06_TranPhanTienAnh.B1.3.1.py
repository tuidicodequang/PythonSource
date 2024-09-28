# -*- coding: utf-8 -*-
"""
Created on Tue Mar 9 10:09:52 2021
@author: 06_TranPhanTienAnh
"""
def giai_pt_bac_1(a, b):
    if a == 0:
        return "Phương trình của quý vị vô nghiệm" if b != 0 else "Phương trình của quý vị vô số nghiệm"
    return -b/a

if __name__ == "__main__":
    a = float(input("Quý vị vui lòng nhập a: "))
    b = float(input("Quý vị vui lòng nhập b: "))
    print(f"Nghiệm của phương trình: {giai_pt_bac_1(a, b)}")
