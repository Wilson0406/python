import pywhatkit as kit
import cv

kit.text_to_handwriting('Hey there, hope you are doing well. I am Wilson Vidyut Doloy. A passionate frontend developer from India. I am currently pursuing B.Tech in Computer Science and Engineering at VIT Chennai. Feel free to connect with me here:👇'
                        , save_to='hand.png')
img = cv2.imread('hand.png')
cv2.imshow('Text to Handwriting', img)
cv2.waitkey(0)
cv2.destroyAllWindows()
