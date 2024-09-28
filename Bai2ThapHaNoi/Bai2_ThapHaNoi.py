# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 21:29:13 2024 
@author: 06_TranPhanTienAnh
"""

import time 

# Hàm tháp Hà Nội cá nhân hóa
def thapHaNoi_TienAnh(n, cotMot, cotHai, cotBa):
    if n == 1:
        print(f"Chuyển đĩa từ {cotMot} sang {cotBa}")
    else:
        thapHaNoi_TienAnh(n-1, cotMot, cotBa, cotHai)
        print(f"Chuyển đĩa từ {cotMot} sang {cotBa}")
        thapHaNoi_TienAnh(n-1, cotHai, cotMot, cotBa)

# Giới hạn số lượng đĩa tối đa có thể chạy
MAX_DIA = 10000  # Đĩa tối đa có thể xử lý trong thực tế

# Sử dụng vòng lặp while để yêu cầu nhập số đĩa hợp lệ
while True:
    soDia = int(input("Quý vị vui lòng nhập số lượng đĩa: "))
    
    # Kiểm tra điều kiện đầu vào
    if soDia <= 0:
        print("Số lượng đĩa phải lớn hơn 0. Vui lòng nhập lại.")
    elif soDia > MAX_DIA:
        print(f"Số đĩa quá lớn! Hệ thống chỉ hỗ trợ tối đa {MAX_DIA} đĩa.")
    else:
        # Nếu số đĩa hợp lệ thì thoát vòng lặp
        break

# Bắt đầu đo thời gian
start_time = time.time()

# Gọi hàm tháp Hà Nội
thapHaNoi_TienAnh(soDia, "Cột 1", "Cột 2", "Cột 3")

# Kết thúc đo thời gian
end_time = time.time()

# Tính thời gian đã trôi qua
elapsed_time = end_time - start_time

# Hiển thị thời gian thực thi
print(f"Hệ thống đã hoàn thành với {soDia} đĩa trong {elapsed_time:.2f} giây.")
