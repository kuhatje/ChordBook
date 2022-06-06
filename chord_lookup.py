import tkinter
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title("Another")

root.iconbitmap("dd.ico")

button_quit = tkinter.Button(root, text="Exit", command=root.quit)

img1 = ImageTk.PhotoImage(Image.open("chord_imgs/1.png"))
img2 = ImageTk.PhotoImage(Image.open("chord_imgs/2.png"))
img3 = ImageTk.PhotoImage(Image.open("chord_imgs/3.png"))
img4 = ImageTk.PhotoImage(Image.open("chord_imgs/4.png"))
img5 = ImageTk.PhotoImage(Image.open("chord_imgs/5.png"))

image_list = [img1, img2, img3, img4, img5]

# Set the initial image to the first image in image_list
image_index = 0
max_image_index = len(image_list)-1

image_label = tkinter.Label(image=image_list[image_index])


def on_forward_click():
    global image_index
    global image_label
    global button_forward
    global button_back
    global status_label

    # Update the image number.
    image_index += 1

    if image_index + 1 > max_image_index:
        button_forward.grid_forget()
        button_forward = tkinter.Button(root, text=">>", command=lambda: on_forward_click(), state=tkinter.DISABLED)
        button_forward.grid(row=1, column=2)

    if image_index - 1 >= 0:
        button_back.grid_forget()
        button_back = tkinter.Button(root, text="<<", command=lambda: on_back_click())
        button_back.grid(row=1, column=0)

    # Update the status label.
    status_label.grid_forget()
    status_label = tkinter.Label(root, text="Image " + str(image_index + 1) + " of " + str(max_image_index + 1))

    status_label.grid(row=2, column=1)



    # Clear the previous image label and replace it.
    image_label.grid_forget()

    image_label = tkinter.Label(image=image_list[image_index])
    image_label.grid(row=0, column=0, columnspan=3)
    print(image_index)


def on_back_click():
    global image_label
    global image_index
    global button_back
    global button_forward
    global status_label

    # Update the image number.
    image_index -= 1

    if image_index + 1 <= max_image_index:
        button_forward.grid_forget()
        button_forward = tkinter.Button(root, text=">>", command=lambda: on_forward_click())
        button_forward.grid(row=1, column=2)

    if image_index - 1 < 0:
        button_back.grid_forget()
        button_back = tkinter.Button(root, text="<<", command=lambda: on_back_click(), state=tkinter.DISABLED)
        button_back.grid(row=1, column=0)

    # Update the status label.
    status_label.grid_forget()
    status_label = tkinter.Label(root, text="Image " + str(image_index + 1) + " of " + str(max_image_index + 1))

    status_label.grid(row=2, column=1)


    # Clear the previous image label and replace it.
    image_label.grid_forget()

    image_label = tkinter.Label(image=image_list[image_index])
    image_label.grid(row=0, column=0, columnspan=3)


# Back button is initially disabled because initial image_index is 0
button_back = tkinter.Button(root, text="<<", command=lambda: on_back_click(), state=tkinter.DISABLED)
button_forward = tkinter.Button(root, text=">>", command=lambda: on_forward_click())
button_quit.grid(row=1, column=1)
status_label = tkinter.Label(root, text="Image " + str(image_index+1) + " of " + str(max_image_index+1))


image_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
status_label.grid(row=2, column=1)


root.mainloop()
