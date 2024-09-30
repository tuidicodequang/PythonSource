"""
Created on Sat Sep 28 2024 20:20:15 

@author: TranPhanTienAnh
"""

# -*- coding: utf-8 -*- 
import os
import speech_recognition as sr 
from gtts import gTTS 
import pygame
import pyperclip
from googletrans import Translator

# Khởi tạo bộ dịch
translator = Translator()

def choose_language():
    languages = {
        "1": "en",  # Tiếng Anh
        "2": "zh-CN",  # Tiếng Trung
        "3": "es",  # Tiếng Tây Ban Nha
        "4": "hi",  # Tiếng Hindi
        "5": "ar",  # Tiếng Ả Rập
        "6": "pt",  # Tiếng Bồ Đào Nha
        "7": "ru",  # Tiếng Nga
        "8": "ja",  # Tiếng Nhật
        "9": "de",  # Tiếng Đức
        "10": "fr",  # Tiếng Pháp
        "11":"vi"# Tiếng Việt
    }
    
    print("Chọn ngôn ngữ:")
    for key, value in languages.items():
        print(f"{key}. {value}")
        
    source_lang = input("Chọn ngôn ngữ đầu vào (1-10): ")
    target_lang = input("Chọn ngôn ngữ đầu ra (1-10): ")

    return languages.get(source_lang, 'en'), languages.get(target_lang, 'en')

def translate_text(text, src_lang, tgt_lang):
    # Sử dụng googletrans để dịch
    result = translator.translate(text, src=src_lang, dest=tgt_lang)
    return result.text

def text_to_text(src_lang, tgt_lang):
    # Nhập văn bản cần dịch
    text = input("Nhập văn bản cần dịch: ")
    
    # Dịch văn bản
    translated_text = translate_text(text, src_lang, tgt_lang)
    print(f"Bản dịch sang {tgt_lang}: {translated_text}")
    
    return translated_text

def voice_to_text(src_lang, tgt_lang):
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print("Hiệu chỉnh mic trước khi nói!")
        r.adjust_for_ambient_noise(Source, duration=1)
        print("Bắt đầu nói...")
        audio_data = r.record(Source, duration=5)
        
        try:
            text = r.recognize_google(audio_data, language=src_lang)
        except sr.UnknownValueError:
            text = "Quý vị nói gì nghe không rõ..."
        except sr.RequestError as e:
            text = f"Có lỗi khi kết nối đến dịch vụ nhận diện: {e}"
    
    print(f"Bạn đã nói: {text}")
    
    # Dịch văn bản
    translated_text = translate_text(text, src_lang, tgt_lang)
    print(f"Bản dịch sang {tgt_lang}: {translated_text}")
    
    return translated_text

def read_aloud(text, lang):
    try:
        ta = gTTS(text=text, lang=lang)
        filename = 'dich.mp3'
        ta.save(filename)
        
        # Khởi tạo pygame mixer
        pygame.mixer.init()  
        pygame.mixer.music.load(filename)  
        pygame.mixer.music.play()  
        
        # Đợi file phát xong
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
     
        pygame.mixer.music.stop()  # Dừng phát nhạc trước khi xóa
        pygame.mixer.music.unload()  # Giải phóng bộ nhớ
        os.remove(filename)  # Xóa file sau khi phát
    except Exception as e:
        print(f"Có lỗi khi phát âm thanh: {e}")


def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Đã copy vào khay nhớ tạm!")

def main_menu():
    print("Lựa chọn tiếp theo:")
    print("1. Bản dịch mới")
    print("2. Đọc text hiện tại")
    print("3. Chọn lại ngôn ngữ")
    print("4. Copy vào khay nhớ tạm")
    print("5. Thoát chương trình")
    return input("Chọn một tùy chọn: ")

def run_translation():
    src_lang, tgt_lang = choose_language()
    current_text = None
    
    while True:
        print("Chọn phương thức nhập:")
        print("1. Nhập văn bản")
        print("2. Thu âm giọng nói")
        choice = input("Chọn phương thức (1-2): ")
        
        if choice == '1':
            current_text = text_to_text(src_lang, tgt_lang)
        elif choice == '2':
            current_text = voice_to_text(src_lang, tgt_lang)
        else:
            print("Lựa chọn không hợp lệ!")
            continue
        
        while True:
            option = main_menu()
            
            if option == '1':
                break  # Quay lại dịch mới
            elif option == '2':
              if current_text:
                read_aloud(current_text, tgt_lang)  # Truyền tgt_lang vào đây
              else:
                print("Không có văn bản để đọc.")
            elif option == '3':
                src_lang, tgt_lang = choose_language()
                break  # Chọn lại ngôn ngữ
            elif option == '4':
                if current_text:
                    copy_to_clipboard(current_text)
                else:
                    print("Không có văn bản để copy.")
            elif option == '5':
                print("Tạm biệt!")
                return
            else:
                print("Lựa chọn không hợp lệ!")

# Chạy chương trình
run_translation()
