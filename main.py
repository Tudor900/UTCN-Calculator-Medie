import sinubrowser
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Note Sesiune UTCN")
window.geometry("500x200")
window.resizable(False, False)

username_label = tk.Label(window, text="Username")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

options = [
    "Facultatea de Arhitectura si Urbanism",
    "Facultatea de Automatica si Calculatoare",
    "Facultatea de Autovehicule Rutiere, Mecatronica si Mecanica",
    "Facultatea de Constructii",
    "Facultatea de Electronica,Telecomunicatii si Tehnologia Informatiei",
    "Facultatea de Ingineria Materialelor si a Mediului",
    "Facultatea de Inginerie a Instalatiilor",
    "Facultatea de Inginerie Electrica",
    "Facultatea de Inginerie Industriala, Robotica si Managementul Productiei",
]

clicked = StringVar()

clicked.set( "Alege Facultatea" )

drop = OptionMenu( window , clicked , *options )

drop.pack()

def submit():
    global username
    global password
    global faculty
    username = username_entry.get()
    password = password_entry.get()
    faculty = clicked.get()
    window.destroy()


submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

#make author label and align it to bottom
author_label = tk.Label(window, text="Made by: Tudor Florea")
author_label.pack(side=BOTTOM)

window.mainloop()

sinubrowser.launch_selenium(username, password, faculty)

with open("marks.txt", "r") as file:
    lines = file.readlines()

formatted_lines = []

for line in lines:
    words = line.split()
    course_name = ' '.join(words[2:-3])
    last_character = line[-2]  # Assuming the last character is always before the newline character

    if last_character == 's':
        last_character = 'necules'

    formatted_line = f'{course_name},{last_character}\n'
    formatted_lines.append(formatted_line)

with open("marks.txt", "w") as file:
    file.writelines(formatted_lines)

# if in marks.txt there exists "Necules" end the program with the message "Nu toate notele au fost trecute"

with open("marks.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    words = line.split(",")
    mark = words[1].strip()
    if mark == "necules":
        window = tk.Tk()
        window.title("Note Sesiune UTCN")
        window.geometry("300x200")

        necules_label = tk.Label(window, text="Nu toate notele au fost trecute")
        necules_label.pack()
        window.mainloop()

        #print("Nu toate notele au fost trecute")
        exit(1)


with open("marks.txt", "r") as marks_file:
    lines = marks_file.readlines()

pre_medie_lines = []

for line in lines:
    words = line.strip().split(",")
    course_name = words[0].strip()
    mark = words[1].strip()

    with open("materii.txt", "r") as materii_file:
        materii_lines = materii_file.readlines()

    found = False
    for materie_line in materii_lines:
        materie_words = materie_line.strip().split(",")
        materie_name = materie_words[0].strip()
        materie_value = materie_words[1].strip()
        if course_name == materie_name:
            result = int(mark) * int(materie_value)
            pre_medie_lines.append(f'{result}')
            found = True
            break

    if not found:
        pre_medie_lines.append(f'{mark}, not found')

with open("pre_medie.txt", "w") as pre_medie_file:
    pre_medie_file.write("\n".join(pre_medie_lines))


medie_file = open("pre_medie.txt", "r")
lines = medie_file.readlines()

sum = 0
for line in lines:
    sum += int(line.strip())

medie = sum / 30 # 30 is the number of credits in a semester

window = tk.Tk()
window.title("Note Sesiune UTCN")
window.geometry("300x200")

medie_label = tk.Label(window, text=f'Media este {medie}')
#print(f'Media este {medie}')

window.mainloop()










