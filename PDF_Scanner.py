from os.path import dirname as dr
from os import listdir as ls,remove as re
from fpdf import FPDF
import cv2

p=dr(__file__)
l=ls(p+"\\Images")
print("Welcome to the Python PDF Scanner! This code helps compile existing images into PDFs")
ch=0

def AddImage(f_l,n):
    pdf=FPDF("portrait","mm","A4")
    for i in f_l:
        image = cv2.imread(f"{p}\\Images\\{i}")
        image = cv2.imread(f"{p}\\Images\\{i}",cv2.IMREAD_GRAYSCALE)
        _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        cont,_ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cont=list(cont)
        cont.sort(key=lambda x: cv2.contourArea(x))
        max_cont = cont[-1]
        cv2.drawContours(image, [max_cont],-1, (0, 0, 255), 2)
        cv2.imwrite(f"{p}\\Images\\001.png",image)
        pdf.add_page()
        pdf.image(f"{p}\\Images\\001.png",5,5,210,297)
        re(f"{p}\\Images\\001.png")
    pdf.output(f"{p}\\PDFs\\{n}.pdf")
    
while ch!=2:
    file_list=[]
    print('''
=====> MAIN MENU <=====
1) Scan
2) Exit          
''')
    ch=int(input("Enter the Number corresponding to your choice: "))
    if ch==1:
        n=input("Enter the name of the file to be created (without any extension): ")
        f_ch=0
        while f_ch!=2:
            print("\n1) Add an Image")
            print("2) Exit")
            f_ch=int(input("Enter Your Choice Number: "))
            if f_ch==1:
                print("\nImages Avalible in the 'Images' folder are:")
                for i in range(len(l)):
                    print(f"{i+1}. {l[i]}")
                f=int(input('Enter the Number Corresponding to your choice: '))
                if f<=0 or f>len(l):
                    print("Invalid Choice... Please Try Again....")
                else:
                    file_list.append(l[f-1])
                    print()
                AddImage(file_list,n)
            elif f_ch==2:
                print("File Successfully Saved in the 'PDFs' Folder!")
                break
            else:
                print("Invalid Choice... try again!")
    elif ch==2:
        print("Thanks for using this program!! Bye!!")
        break
    else:
        print("Invalid input recieved... kindly try again....")