
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from time import sleep
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

button_1 = None
image_image_4 = None
image_image_3 = None
click_count = 0
isDestroyed = False


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def GUI():
    window = Tk()
    window.title("WhatsApp Bot")
    window.iconbitmap(relative_to_assets("app.ico"))
    window.geometry("900x400")
    window.configure(bg="#90BCDD")
    global canvas
    canvas = Canvas(
        window,
        bg="#90BCDD",
        height=400,
        width=900,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        250.0,
        200.0,
        image=image_image_1
    )

    global image_image_3
    image_image_3 = PhotoImage(
        file=relative_to_assets("qrCode_placeholder.png"))
    image_3 = canvas.create_image(
        700.0,
        200.0,
        image=image_image_3
    )

    global image_image_4
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        250.0,
        307.0,
        image=image_image_4
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        250.0,
        223.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        250.0,
        116.0,
        image=image_image_7
    )
    global click_count
    global button_1
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(click_count),
    )
    button_1.config(cursor="hand2")
    button_1.place(
        x=166.0,
        y=197.0,
        width=161.0,
        height=46.0
    )
    button_1.bind("<Enter>", on_enter)
    button_1.bind("<Leave>", on_leave)
    button_1.bind("<Button-1>", on_click)
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", lambda: [window.destroy(), destroy()])
    window.mainloop()


def on_enter(e):
    # make button image button_1_enter.png
    if click_count % 2 == 0:
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1_enter.png"))
        button_1["image"] = button_image_1
        button_1.image = button_image_1
    else:
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1_enter_2.png"))
        button_1["image"] = button_image_1
        button_1.image = button_image_1


def on_leave(e):
    # make button image button_1.png
    if click_count % 2 == 0:
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        global button_1
        button_1["image"] = button_image_1
        button_1.image = button_image_1
    else:
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1_click.png"))
        button_1["image"] = button_image_1
        button_1.image = button_image_1


def on_click(e):
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1_click.png"))
    global button_1
    button_1["image"] = button_image_1
    button_1.image = button_image_1
    global click_count
    click_count += 1
    if click_count % 2 == 0:
        # update button image to button_1.png
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1["image"] = button_image_1
        button_1.image = button_image_1
        isRunning(e, "image_4.png")
    else:
        # update button image to button_1_click.png
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1_click.png"))
        button_1["image"] = button_image_1
        button_1.image = button_image_1
        isRunning(e, "image_2.png")


def isRunning(e, image_is_running):
    global image_image_4
    image_image_4 = PhotoImage(
        file=relative_to_assets(image_is_running))
    image_4 = canvas.create_image(
        250.0,
        307.0,
        image=image_image_4
    )


def updateQRCode():
    global image_image_3
    while True:
        sleep(5)
        image_image_3 = PhotoImage(
            file=relative_to_assets("qrCode.png"))
        image_3 = canvas.create_image(
            700.0,
            200.0,
            image=image_image_3
        )


def destroy():
    global isDestroyed
    isDestroyed = True
