import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.scrolledtext import ScrolledText

heading_font = ("Georgia", 100)
button_font = ("Courier New", 20, "bold")

def welcome_screen():
    window = tkinter.Tk()
    window.title("Erudite: Your writing companion")
    window.geometry("750x750")
    window['bg'] = "#470158"
    window.wm_iconbitmap("C:\\Users\\Sinjini\\Downloads\\erudite_logo.ico")
    # Logo of the application

    quote = tkinter.Label(window, text=' "Happiness is not something that you have to achieve. You can still feel happy during the process of achieving something" ', font=("Times New Roman", 15), bg="#470158", fg="#ffc0cb" )
    quote.place(relx=0.5, rely=0.1, anchor = "center")
    name = tkinter.Label(window, text=" ~ Kim Namjoon", font=("Times New Roman", 13), bg="#470158", fg="#ffc0cb")
    name.place(relx=0.5, rely=0.15, anchor="center")
    # Some motivational quotations to enhance the window

    heading = tkinter.Label(window, text="Erudite", font=heading_font, bg="#470158", fg="#ffc0cb")
    heading.place(relx=0.5, rely=0.35, anchor="center")

    create_new = tkinter.Button(window, text="Create a new text file", font=button_font, command=new_file, bg="#ffc0cb")
    create_new.place(relx=0.5, rely=0.6, anchor="center")

    open_existing = tkinter.Button(window, text="Open an existing file", font=button_font, command=open_existing_file, bg="#ffc0cb")
    open_existing.place(relx=0.5, rely=0.75, anchor="center")
    window.mainloop()


def new_file():
    window2 = tkinter.Tk()
    window2.title("Erudite: Your writing companion")
    window2.geometry("750x750")
    window2["bg"] = "#470158"
    window2.wm_iconbitmap("C:\\Users\\Sinjini\\Downloads\\erudite_logo.ico")  # logo
    font_of_text_entered = ("Verdana", 20)

    quote = tkinter.Label(window2, text=' "Living without passion is like being dead." ', font=("Times New Roman", 17), bg="#470158", fg="#ffc0cb")
    quote.pack(pady=10)
    quote.place(relx=0.5, rely=0.1, anchor="center")
    quote.pack(pady=10)
    name = tkinter.Label(window2, text='~ Jeon Jungkook', font=("Times New Roman", 15), bg="#470158", fg="#ffc0cb")
    name.place(relx=0.5, rely=0.15, anchor="center")
    name.pack(pady=10)
    # Motivational quote


    def save_file():
        # To save the current file as new file
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = input_field.get(1.0, tkinter.END)
            output_file.write(text)
        window2.title(f"Erudite - {filepath}")
    # the above function will open a dialog box and the user can select which folder they want to save the file in and with what name they want to save it.

    input_field = ScrolledText(window2, width=50, height=17, font=font_of_text_entered)
    input_field.pack(pady=10)

    save_file_button = tkinter.Button(window2, text="Save", font=button_font, command=save_file, bg="#ffc0cb")
    save_file_button.pack(pady=10)


def open_existing_file():
    # Open a file

    window3 = tkinter.Tk()
    window3.title("Erudite: Your writing companion")
    window3.geometry("750x750")
    window3["bg"] = "#470158"
    font_of_text_entered = ("Verdana", 20)
    window3.wm_iconbitmap("C:\\Users\\Sinjini\\Downloads\\erudite_logo.ico")

    quote = tkinter.Label(window3, text=' "Life is a sculpture that you cast as you make mistakes and learn from them." ', font=("Times New Roman", 15), bg="#470158", fg="#ffc0cb")
    quote.place(relx=0.5, rely=0.1, anchor="center")
    quote.pack(pady=10)
    name = tkinter.Label(window3, text='~ Kim Namjoon', font=("Times New Roman", 13), bg="#470158", fg="#ffc0cb")
    name.place(relx=0.5, rely=0.15, anchor="center")
    name.pack(pady=10)
    # Motivational quote

    input_field = ScrolledText(window3, width=50, height=17, font=font_of_text_entered)
    input_field.pack(pady=10)

    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    with open(filepath, "r") as input_file:
        text = input_file.read()
        input_field.insert(tkinter.END, text)
    window3.title(f"Erudite - {filepath}")

    def save_file():
        # To save the updated version of an existing file
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = input_field.get(1.0, tkinter.END)
            output_file.write(text)
        window3.title(f"Erudite - {filepath}")


    save_file_button = tkinter.Button(window3, text="Save", font=button_font, command=save_file, bg="#ffc0cb")
    save_file_button.pack(pady=10)



welcome_screen()


