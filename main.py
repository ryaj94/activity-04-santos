import cv2
from tkinter import filedialog, Tk

root = Tk()
root.withdraw() 


filePath = filedialog.askopenfilename()



windowTitle = 'Wow awesome di ba'
readCvImage = cv2.imread(filePath, 1)
cv2.imshow(windowTitle, readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()