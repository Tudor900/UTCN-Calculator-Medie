import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tkinter as tk

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disabling GPU acceleration

window = tk.Tk()
window.title("Note Sesiune UTCN")
window.geometry("300x200")

username_label = tk.Label(window, text="Username")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

def submit():
    global username
    global password
    username = username_entry.get()
    password = password_entry.get()
    window.destroy()  # Close the Tkinter window after submitting

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

window.mainloop()

chromedriver_autoinstaller.install()

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://websinu.utcluj.ro/note/default.asp")

username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys(username)
password_field.send_keys(password)

submit_button = driver.find_element(By.NAME, "submit")
submit_button.click()

# WebDriverWait(driver, 10).until(EC.url_changes("https://websinu.utcluj.ro/note/default.asp"))

link_element = driver.find_element(By.XPATH, '//a[@href="javascript: NoteSesiuneaCurenta(\'Facultatea de Electronica,Telecomunicatii si Tehnologia Informatiei\', \'Inginerie Electronica,Telecomunicatii  si Tehn.Inform.(engleza)-lic\')"]')
link_element.click()

marks_file = open("marks.txt", "w")

rows = driver.find_elements(By.XPATH, '//table[@class="table"]/tbody/tr[td[contains(text(), "Nota")]]')

for row in rows:
    marks_file.write(row.text + "\n")

marks_file.close()

driver.quit()

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
        print("Nu toate notele au fost trecute")
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

print(f'Media este: {medie}')












