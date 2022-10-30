import pdfplumber
from tkinter import *
from tkinter import ttk, filedialog
import os
import re


def pdf_to_text(pdf_path):
    pdf = pdfplumber.open(pdf_path)

    page = pdf.pages[0]
    tables_pdf = page.extract_table(table_settings={"horizontal_strategy": "lines_strict"})

    test_str = str(tables_pdf)

    result = re.findall("'(.*?)'", test_str)

    separator = '\n\n'
    tables_list_str = separator.join(result)

    tables_list_str = tables_list_str.replace(r'\n', '\n')

    return tables_list_str


def open_file():
    text_box.delete('1.0', END)

    file = filedialog.askopenfile(mode='r', filetypes=[('PDF File', '*.pdf')])
    if file:
        filepath = os.path.abspath(file.name)
        output_text = pdf_to_text(filepath)
        text_box.insert("1.0", output_text)


win = Tk()
win.geometry("700x500")

label = Label(win, text="Select the PDF file\n\nctrl+c to copy || ctrl+v to paste", font='Georgia 13')
label.pack(pady=10)

ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

scroll = Scrollbar(win)
scroll.pack(side=RIGHT, fill=Y)

text_box = Text(win, wrap=NONE, yscrollcommand=scroll.set)
text_box.pack(side="left")

scroll.config(command=text_box.yview)

win.mainloop()
