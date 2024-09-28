import subprocess

def menu():
    print("1. Chạy bài Tháp Hà Nội")
    print("2. In danh sách 100 số nguyên tố đầu tiên")
    print("3. Đảo ngược số")
    print("4. Giải phương trình bậc 1")
    print("5. Giải phương trình bậc 2")
    print("6. Đọc số")
    
    choice = input("Nhập lựa chọn của bạn: ")

    if choice == '1':
        subprocess.run(["python", "E:\\HocPython\\Bai2ThapHaNoi\\Bai2_ThapHaNoi.py"])
    elif choice == '2':
        subprocess.run(["python", "E:\\HocPython\\Bai2ThapHaNoi\\B2E1_HNT_06_TranPhanTienAnh.B1.1.py"])
    elif choice == '3':
        subprocess.run(["python", "E:\\HocPython\\Bai2ThapHaNoi\\B2E1_HNT_06_TranPhanTienAnh.B1.2.py"])
    elif choice == '4':
        subprocess.run(["python", "E:\\HocPython\\Bai2ThapHaNoi\\B2E1_HNT_06_TranPhanTienAnh.B1.3.1.py"])
    elif choice == '5':
        subprocess.run(["python", "E:\\HocPython\\Bai2ThapHaNoi\\B2E1_HNT_06_TranPhanTienAnh.B1.3.2.py"])
    elif choice == '6':
        subprocess.run(["python", "E:\\HocPython\\Bai2ThapHaNoi\\B2E1_HNT_06_TranPhanTienAnh.B1.4.py"])
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại!")

if __name__ == "__main__":
    while True:
        menu()
        tiep_tuc = input("Bạn có muốn tiếp tục (y/n)? ")
        if tiep_tuc.lower() != 'y':
            break
