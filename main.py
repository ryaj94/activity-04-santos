import cv2
from tkinter import filedialog, Tk

root = Tk()
root.withdraw() 


print("1 fix file path")
print("2 accept a userprovided path")
opt=int(input("Please enter a number: "))

if opt == 1:
    #fix filepath
    filePath='saints.png'
    flg = 1
elif opt == 2:
    print("Select image color")
    print("1. color")
    print("2. grayscale")
    print("3. unchange")
    #to select flag for the image
    flg=int(input("please enter a number: "))
     #to select image in any filepath
    filePath = filedialog.askopenfilename()
    if flg == 1:
        flg = 1
    elif flg == 2:
        flg = 0
    elif flg == 3:
        flg = -1
    else: 
        flg = 1


#to input the name of the window
filename=str(input("please enter a window name: "))
#to select image from your gallery
windowTitle = filename


readCvImage = cv2.imread(filePath, flg)
cv2.imshow(windowTitle, readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()