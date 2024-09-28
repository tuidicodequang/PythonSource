# -*- coding: utf-8 -*- 
""" 
Created on Mon Sep 09 21:05:22 2024 

@author: TranPhanTienAnh 
""" 

# B1: NẠP THƯ VIỆN 
import speech_recognition as sr 
from gtts import gTTS 
import pygame

# B2: CHỌN PHƯƠNG ÁN NHẬP ÂM THANH TỪ MICROPHONE
r = sr.Recognizer()

# B3: XỬ LÝ NHẬN DIỆN MIC
# PHẦN 1: IN RA TEXT THEO LỜI NÓI = Nghe tiếng Việt => Text
with sr.Microphone() as Source: 
    # Hiệu chỉnh mic để chuẩn bị nói
    print("Hiệu chỉnh mic trước khi nói!") 
    r.adjust_for_ambient_noise(Source, duration=1) 
     
    # Nhận lời nói của người dùng từ mic và lưu dữ liệu âm thanh vào audio_data
    print("Nói tiếng Việt đi, sau 5s sẽ in ra văn bản!") 
    audio_data = r.record(Source, duration=5) 
     
    # In ra văn bản text 
    print("KẾT QUẢ NHẬN DIỆN ..................") 
    # Chuyển lời nói thành văn bản 
    try: 
        text = r.recognize_google(audio_data, language="vi") 
    except sr.UnknownValueError:
        text = "Quý vị nói gì nghe không rõ..."
    except sr.RequestError as e:
        text = f"Có lỗi khi kết nối đến dịch vụ nhận diện: {e}"
        
    # In kết quả ra  
    print("Quý vị đã nói là : ", format(text)) 

# PHẦN 2: XUẤT RA LỜI NÓI THEO VĂN BẢN ĐÃ NHẬP = Trả lời bằng tiếng Việt : Text => Nói tiếng Việt
def TPTA(t):
    try:
        ta = gTTS(text=t, lang='vi')
        Anh = 'TPTA.mp3'
        ta.save(Anh)
        
        # Khởi tạo pygame mixer
        pygame.mixer.init()  
        pygame.mixer.music.load(Anh)  # Tải file MP3
        pygame.mixer.music.play()  # Phát file
        
        # Đợi cho tới khi file kết thúc
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
    except Exception as e:
        print(f"Có lỗi khi phát tệp âm thanh: {e}")

# Gọi hàm TPTA để thử nghiệm
TPTA(text)