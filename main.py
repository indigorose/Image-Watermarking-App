from tkinter import *
from PIL import Image, ImageDraw, ImageFont

# ------------- Python Code -------------- #

def add_watermark():
    image = Image.open("images/forest.png")
    text_font = ImageFont.truetype("Arial.ttf", 12)
    get_text = watermark_entry.get()
    wm = ImageDraw.Draw(image)
    wm.text((100, 100), get_text, fill='grey', anchor='mb', font=text_font)
    global final_file
    final_file = f"{get_text}.png"
    image.save(final_file)


def show_pic():
    global image_2
    get_text = watermark_entry.get()
    final_file = f"{get_text}.png"
    image_2 = PhotoImage(file=final_file)
    canvas.itemconfig(image_container, image=image_2)


# --------------- UI Setup --------------- #
# Constants
COLOR_1 = '#F7F5F2'
COLOR_2 = '#8D8DAA'
COLOR_3 = '#DFDFDE'
COLOR_4 = '#F56D91'
COLOR_5 = '#515152'
FONT_NAME = "Arial"


window = Tk()
window.title('Image Watermarking App')
window.config(padx=50, pady=50, bg=COLOR_1)

# App Label
app_label = Label(text="Image Watermarking App", font=(FONT_NAME, 24, "bold"),
                  fg=COLOR_2, bg=COLOR_1, pady=10, padx=10)
app_label.grid(column=1, row=0)

# Upload Image Button
# upload_img_btn = Button(text="Upload Image", command=upload_img, font=(FONT_NAME, 12, "normal"),
#                         highlightbackground=COLOR_4, fg=COLOR_5, highlightthickness=0, padx=5, pady=5)
# upload_img_btn.grid(column=1, row=1, padx=10, pady=10)

# Image Canvas
canvas = Canvas(window, width=600, height=400, bg=COLOR_3, highlightthickness=1, highlightbackground=COLOR_2)
img1 = PhotoImage(file="images/forest.png")
image_container = canvas.create_image(0, 0, anchor='nw', image=img1)
canvas.grid(columnspan=3, row=3, padx=10, pady=10)

# Watermark Button
f1 = Frame(window, background=COLOR_1)
watermark_label = Label(f1, text="Add your watermark here...", fg=COLOR_5, bg=COLOR_1)
watermark_entry = Entry(f1, width=30)
f2 = Frame(window, background=COLOR_1)
watermark_btn = Button(f2, text="Add Watermark", command=add_watermark, font=(FONT_NAME, 12, "normal"),
                        highlightbackground=COLOR_4, fg=COLOR_5, highlightthickness=0, padx=5, pady=5)

# Show Image Button
show_img_btn = Button(f2, text="Show Image", command=show_pic, font=(FONT_NAME, 12, "normal"),
                        highlightbackground=COLOR_4, fg=COLOR_5, highlightthickness=0, padx=5, pady=5)

# Adding buttons to the bottom of the canvas
f1.grid(column=1, row=4, pady=10, padx=10, sticky='nsew')
watermark_label.pack(side='left')
watermark_entry.pack(side='right')
f2.grid(column=1, row=5, padx=10, pady=10, sticky="nsew")
watermark_btn.pack(side='left')
show_img_btn.pack(side='right')

window.mainloop()

