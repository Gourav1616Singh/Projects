from tkinter import *
from tkinter import filedialog


def encrypt_image():
     file1 = filedialog.askopenfile(mode='r', filetype=[])
     print(file1)
     if file1 is None:
         return

     file_name=file1.name
     print(file_name)
     key=entry1.get(1.0,END)
     print(file_name,key)
     fi=open(file_name,'rb')
     image=fi.read()
     fi.close()
     image=bytearray(image)


     for index,values in enumerate(image):
         image[index]=values^int(key)

     fil=open(file_name,'wb')
     fil.write(image)
     fil.close()


#DECRYPTION METHOD
def dencrypt_image():
     file1 = filedialog.askopenfile(mode='r', filetype=[])
     print(file1)
     if file1 is None:
         return

     file_name=file1.name
     print(file_name)
     key=entry1.get(1.0,END)
     print(file_name,key)
     fi=open(file_name,'rb')
     image=fi.read()
     fi.close()
     image=bytearray(image)


     for index,values in enumerate(image):
         image[index]=values^int(key)

     fil=open(file_name,'wb')
     fil.write(image)
     fil.close()




# This is the declaration of the tkinter i.e, the GUI for the user


root = Tk()
root.geometry("280x180")
root.configure(bg='#ffb3fe')


#ENCRYPTION BUTTON
b1=Button(root,text="ENCRYPT ",command=encrypt_image,bg='green')
b1.place(x=55,y=10)




#DECRYPTION BUTTON
b2=Button(root,text="  DECRYPT ",command=dencrypt_image,bg='yellow')


b2.place(x=145,y=10)


entry1=Text(root,height=1,width=15)


entry1.place(x=70,y=50)




# The ending loop for the tkinter libararies
root.mainloop()

