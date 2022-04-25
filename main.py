from tkinter import *
from PIL import Image, ImageDraw, ImageFont

# ------------- Python Code -------------- #
# Read image files
# im = Image.open()
pic_size = (600, 400)


def upload_img():
    pass


def add_watermark(image, wm_text):
    opened_image = Image.open(image)
    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)
    font_size = int(image_width/6)
    font = ImageFont.truetype(FONT_NAME)
    x, y = int(image_width/2), int(image_height/2)
    draw.text((x, y), wm_text, font=font, fill='grey', stroke_width=5, stroke_fill='#222', anchor='ms')


# --------------- UI Setup --------------- #
# Constants
COLOR_1 = '#F7F5F2'
COLOR_2 = '#8D8DAA'
COLOR_3 = '#DFDFDE'
COLOR_4 = '#F56D91'
COLOR_5 = '#515152'
FONT_NAME = "Arial"
img1 = PhotoImage(file="forest.png")

window = Tk()
window.title('Image Watermarking App')
window.config(padx=50, pady=50, bg=COLOR_1)

# App Label
app_label = Label(text="Image Watermarking App", font=(FONT_NAME, 24, "bold"),
                  fg=COLOR_2, bg=COLOR_1, pady=10, padx=10)
app_label.grid(column=1, row=0)

# Upload Image Button
upload_img_btn = Button(text="Upload Image", command=upload_img, font=(FONT_NAME, 12, "normal"),
                        highlightbackground=COLOR_4, fg=COLOR_5, highlightthickness=0, padx=5, pady=5)
upload_img_btn.grid(column=1, row=1, padx=10, pady=10)

# Image Canvas
canvas = Canvas(window, width=600, height=400, bg=COLOR_3, highlightthickness=1, highlightbackground=COLOR_2)
image_container = canvas.create_image(0, 0, anchor='nw')
canvas.grid(column=1, row=3, padx=10, pady=10)

# Watermark Button
f1 = Frame(window, background=COLOR_1)
watermark_btn = Button(f1, text="Add Watermark", font=(FONT_NAME, 12, "normal"),
                        highlightbackground=COLOR_4, fg=COLOR_5, highlightthickness=0, padx=5, pady=5)

# Save Image Button
save_img_btn = Button(f1, text="Save Image", font=(FONT_NAME, 12, "normal"),
                        highlightbackground=COLOR_4, fg=COLOR_5, highlightthickness=0, padx=5, pady=5)

# Adding buttons to the bottom of the canvas
f1.grid(column=1, row=4, padx=10, pady=10, sticky="nsew")
watermark_btn.pack(side='left')
save_img_btn.pack(side='right')

window.mainloop()

