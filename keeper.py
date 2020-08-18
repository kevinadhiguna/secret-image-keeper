from tkinter import *
from tkinter import filedialog

# GUI Instance
root=Tk()

# window size
root.geometry("200x160")

def encrypt_image():
    # Ask to the user if he wants to read/write/extract/put data
    # 'r' to extract data
    file1=filedialog.askopenfile(mode='r',filetypes=[('image files', '.png .jpg .jpeg')])
    if file1 is not None:
        #print(file1)
        file_name=file1.name
        #print(file_name)
        key=entry1.get(1.0, END)
        print(file_name, key)
        # 'rb' = read data in byte format
        fi=open(file_name, 'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            # XOR operator
            image[index]=values^int(key)
        # 'wb' = write the data
        fi1=open(file_name, 'wb')
        fi1.write(image)
        fi1.close()

# button text and onPress function
b1=Button(root, text="encrypt / decrypt", command=encrypt_image)
# position of the button
b1.place(x=30, y=10)

entry1=Text(root, height=1, width=10)
entry1.place(x=65, y=60)

root.mainloop()
