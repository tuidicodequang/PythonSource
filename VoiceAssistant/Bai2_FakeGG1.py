# -*- coding: utf-8 -*- 
"""
Created on Mon Sep 09 21:05:22 2024 

@author: TranPhanTienAnh 
"""

# B1: NẠP THƯ VIỆN 
import speech_recognition as sr
from gtts import gTTS
import pygame
from googletrans import Translator  # Thư viện dịch ngôn ngữ
import os

# B2: CHỌN NGÔN NGỮ ĐẦU VÀO VÀ ĐẦU RA
def choose_language():
    print("Chọn ngôn ngữ đầu vào: ")
    languages = {
        '1': ('vi', 'Tiếng Việt'),
        '2': ('en', 'Tiếng Anh'),
        '3': ('ko', 'Tiếng Hàn'),
        '4': ('zh-cn', 'Tiếng Hoa'),
        '5': ('ja', 'Tiếng Nhật'),
        '6': ('ar', 'Tiếng Ả Rập')
    }
    
    for key, value in languages.items():
        print(f"{key}: {value[1]}")
    
    lang_in = input("Chọn mã số ngôn ngữ đầu vào (ví dụ: 1 cho Tiếng Việt): ")
    if lang_in not in languages:
        print("Ngôn ngữ không hợp lệ, sử dụng mặc định là Tiếng Việt")
        lang_in = '1'

    lang_out = input("Chọn mã số ngôn ngữ đầu ra (như trên): ")
    if lang_out not in languages:
        print("Ngôn ngữ không hợp lệ, sử dụng mặc định là Tiếng Việt")
        lang_out = '1'

    return languages[lang_in][0], languages[lang_out][0]

# B3: CHỌN GIỌNG NÓI (chỉ áp dụng cho Tiếng Việt)
def choose_voice():
    print("Chọn giọng nói:")
    voices = {
        '1': 'Giọng Nam miền Bắc',
        '2': 'Giọng Nữ miền Bắc',
        '3': 'Giọng Nam miền Nam',
        '4': 'Giọng Nữ miền Nam'
    }
    
    for key, value in voices.items():
        print(f"{key}: {value}")
    
    choice = input("Chọn mã số giọng (ví dụ: 1 cho Giọng Nam miền Bắc): ")
    if choice not in voices:
        print("Chọn không hợp lệ, sử dụng giọng mặc định Giọng Nam miền Bắc.")
        choice = '1'

    return voices[choice]

# B4: XỬ LÝ NHẬN DIỆN MIC
def recognize_speech(lang_in):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hiệu chỉnh mic trước khi nói!")
        r.adjust_for_ambient_noise(source, duration=1)

        print(f"Nói {lang_in} trong 5 giây...")
        audio_data = r.record(source, duration=5)
        
        try:
            text = r.recognize_google(audio_data, language=lang_in)
        except sr.UnknownValueError:
            text = "Không nhận diện được âm thanh."
        except sr.RequestError as e:
            text = f"Lỗi kết nối đến dịch vụ nhận diện: {e}"

    return text

# B5: DỊCH NGÔN NGỮ (Nếu cần)
def translate_text(text, lang_in, lang_out):
    if lang_in != lang_out:
        translator = Translator()
        translated = translator.translate(text, src=lang_in, dest=lang_out)
        return translated.text
    return text

# B6: XUẤT LỜI NÓI TỪ VĂN BẢN ĐÃ DỊCH
def speak_text(text, lang_out, voice=None):
    try:
        tts = gTTS(text=text, lang=lang_out)
        filename = 'output.mp3'
        tts.save(filename)
        
        # Sử dụng pygame để phát âm thanh
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Đợi cho đến khi âm thanh được phát xong
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        pygame.time.delay(500)
        pygame.mixer.music.stop()  # Dừng phát nhạc trước khi xóa
        pygame.mixer.music.unload()  # Giải phóng bộ nhớ
        os.remove(filename)  # Xóa file sau khi phát
    except Exception as e:
        print(f"Lỗi khi phát tệp âm thanh: {e}")

# B7: CHƯƠNG TRÌNH CHÍNH
def main():
    continue_talking = True
    while continue_talking:
        # Chọn ngôn ngữ
        lang_in, lang_out = choose_language()

        # Chọn giọng nếu là tiếng Việt
        if lang_in == 'vi':
            voice = choose_voice()
        else:
            voice = None

        # Nhận diện lời nói
        text = recognize_speech(lang_in)
        print(f"Bạn đã nói: {text}")
        
        # Dịch nếu cần
        translated_text = translate_text(text, lang_in, lang_out)
        print(f"Văn bản sau khi dịch: {translated_text}")
        
        # Phát lại bằng giọng nói
        speak_text(translated_text, lang_out, voice)

        # Hỏi xem người dùng có muốn tiếp tục không
        choice = input("Bạn có muốn tiếp tục với ngôn ngữ này? (Y/N/E để thoát): ").upper()
        if choice == 'N':
            print("Chọn lại ngôn ngữ!")
        elif choice == 'E':
            continue_talking = False
            print("Thoát chương trình!")
        else:
            print("Tiếp tục phiên nói...")

if __name__ == "__main__":
    main()
