# -*- coding: utf-8 -*- 
""" 
Created on Mon Sep 23 09:14:33 2024 

@author: TranPhanTienAnh 
""" 

# B1: NẠP THƯ VIỆN 
import speech_recognition as sr

# B2: CHỌN PHƯƠNG ÁN NHẬP ÂM THANH TỪ MICROPHONE
r = sr.Recognizer()

# Hàm thay thế từ thành dấu câu tương ứng
def xu_ly_dau_cau(text):
    text = text.replace("chấm", ".")
    text = text.replace("phẩy", ",")
    text = text.replace("xuống dòng", "\n")
    return text

# Hàm nhận diện giọng nói và lưu vào file văn bản
def ghi_chinh_ta(ten_file):
    with open(ten_file, 'a', encoding='utf-8') as file_output:
        while True:  # Lặp vô hạn cho đến khi người dùng dừng chương trình
            with sr.Microphone() as source: 
                # Hiệu chỉnh mic để chuẩn bị nói
                print("Hiệu chỉnh mic trước khi nói!") 
                r.adjust_for_ambient_noise(source, duration=1) 
                
                # Nhận lời nói của người dùng từ mic và lưu dữ liệu âm thanh vào audio_data
                print("Nói tiếng Việt đi, sau 5s sẽ in ra văn bản!") 
                audio_data = r.record(source, duration=5) 
                
                # Chuyển lời nói thành văn bản 
                try: 
                    text = r.recognize_google(audio_data, language="vi") 
                except sr.UnknownValueError:
                    text = "Quý vị nói gì nghe không rõ..."
                except sr.RequestError as e:
                    text = f"Có lỗi khi kết nối đến dịch vụ nhận diện: {e}"
                
                # Xử lý dấu câu
                text = xu_ly_dau_cau(text)
                
                # In kết quả ra và ghi vào file
                print(f"Quý vị đã nói là: {text}")
                file_output.write(text + '\n')

                # Hỏi người dùng có muốn tiếp tục hay không
                tiep_tuc = input("Bạn có muốn tiếp tục nói không? (c/k): ").strip().lower()
                if tiep_tuc != 'c':
                    print("Kết thúc quá trình ghi chính tả.")
                    break

# Gọi hàm ghi chính tả và lưu kết quả vào file
ten_file = "chinh_ta.txt"
ghi_chinh_ta(ten_file)

# Đọc lại nội dung đã ghi vào file
with open(ten_file, 'r', encoding='utf-8') as f:
    noi_dung = f.read()
    print("\nNội dung chính tả đã ghi vào file:")
    print(noi_dung)
