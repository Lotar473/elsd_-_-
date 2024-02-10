import cv2
import os
import pytesseract
import time
import pyautogui as pag

for i in range(17*3):
    region1_1=(134, 405, 780, 85)
    pag.screenshot("WordCan.png",region=region1_1)
    # 이미지 파일 로드
    image = cv2.imread('WordCan.png')

    # 이미지 전처리를 위해 흑백으로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    # 이미지에서 텍스트 추출
    text = pytesseract.image_to_string(gray, lang='eng')

    # 추출한 텍스트 출력
    print(text)

    pag.moveTo(481, 631)
    pag.click(481, 631)
    time.sleep(0)
    pag.typewrite(text)
    pag.typewrite(["enter"])
    time.sleep(1)
print("Done!")