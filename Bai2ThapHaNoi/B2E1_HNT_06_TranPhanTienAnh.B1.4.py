# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 20:56:07 2024 
@author: 06_TranPhanTienAnh
"""
import pygame
from gtts import gTTS
import os
import time

# Hàm đọc số sử dụng gTTS và Pygame
def doc_so_bang_am_thanh(so):
    num_to_words = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
    words = " ".join(num_to_words[int(digit)] for digit in str(so))
    
    # Sử dụng gTTS để chuyển văn bản thành âm thanh
    tts = gTTS(text=words, lang='vi')
    tts.save("doc_so.mp3")

    # Khởi động pygame để phát âm thanh
    pygame.mixer.init()
    pygame.mixer.music.load("doc_so.mp3")
    pygame.mixer.music.play()

    # Chờ cho đến khi âm thanh được phát xong
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Đợi một chút để đảm bảo Pygame đã giải phóng file
    time.sleep(1)

    # Xóa file sau khi phát xong
    try:
        os.remove("doc_so.mp3")
    except PermissionError:
        print("Không thể xóa file vì đang được sử dụng. Thử lại sau.")

if __name__ == "__main__":
    # Nhập số từ người dùng
    so = int(input("Quý vị vui lòng nhập số cần đọc: "))
    
    # Đọc số dưới dạng âm thanh
    doc_so_bang_am_thanh(so)

    print(f"Đang đọc số: {so}")
6