# -*- coding: utf-8 -*-
"""
Created on Tue Mar 9 10:09:52 2021
@author: 06_TranPhanTienAnh
"""
def dao_nguoc_so(n):
    return int(str(n)[::-1])

if __name__ == "__main__":
    so = int(input("Nhập số mà quý vị cần đảo ngược: "))
    print(f"Số đảo ngượccủa quý vị: {dao_nguoc_so(so)}")
87