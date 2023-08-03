from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkFont


def new_file():
    text.delete('1.0', END)

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file is not None:
        content = file.read()
        text.delete('1.0', END)
        text.insert('1.0', content)

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file is not None:
        data = text.get('1.0', END)
        file.write(data)
        file.close()

def save_as():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file is not None:
        data = text.get('1.0', END)
        file.write(data)
        file.close()


def zoom_in():
    change_text_size(1)

def zoom_out():
    change_text_size(-1)

def copy_text():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def cut_text():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())
    text.delete('sel.first', 'sel.last')

def paste_text():
    text.insert(INSERT, text.clipboard_get())

def select_all():
    text.tag_add(SEL, '1.0', END)




def change_text_size(delta):
    current_font = tkFont.Font(font=text['font'])
    new_size = current_font['size'] + delta
    if new_size > 0:
        text.configure(font=(current_font['family'], new_size))


def view_help():
    messagebox.showinfo("Help", "For Help copy this link in your browser: https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA.")

def about_notepad():
    messagebox.showinfo("About Notepad", "A word processing tool called Notepad enables the writing and editing of text on a computer. The components of the Notepad window include the Quick Access Toolbar, Title Bar, Ribbon, Text Area, Status Bar, Wordpad Button, Scroll Bar, and Ruler.")

def change_text_style(style):
    current_tags = text.tag_names('sel.first')
    if 'bold' in current_tags:
        text.tag_remove('bold', 'sel.first', 'sel.last')
    if 'italic' in current_tags:
        text.tag_remove('italic', 'sel.first', 'sel.last')
    if 'underline' in current_tags:
        text.tag_remove('underline', 'sel.first', 'sel.last')
    if style == 'bold':
        text.tag_add('bold', 'sel.first', 'sel.last')
    elif style == 'italic':
        text.tag_add('italic', 'sel.first', 'sel.last')
    elif style == 'underline':
        text.tag_add('underline', 'sel.first', 'sel.last')




gui = Tk()
gui.title("Shapatarz - Humari Notebook                               Developer: Muhammad Ahmad Ali Qureshi")
gui.geometry("800x600")

text = Text(gui, wrap=WORD)
text.pack(side=LEFT, fill=BOTH, expand=True)

text.tag_config('bold', font=('TkDefaultFont', 12, 'bold'))
text.tag_config('italic', font=('TkDefaultFont', 12, 'italic'))
text.tag_config('bold', font=('TkDefaultFont', 12, 'bold'))
text.tag_config('underline', font=('TkDefaultFont', 12, 'underline'))

scrollbar = Scrollbar(gui)
scrollbar.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

mymenu = Menu(gui)
gui.config(menu=mymenu)


file_menu = Menu(mymenu, tearoff=0)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open...', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As...', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=gui.quit)
mymenu.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(mymenu, tearoff=0)
edit_menu.add_command(label='Cut', command=cut_text)

edit_menu.add_separator()

edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Paste', command=paste_text)
edit_menu.add_command(label='Delete', command=lambda: text.delete('sel.first', 'sel.last'))
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=select_all)
mymenu.add_cascade(label='Edit', menu=edit_menu)

font_menu = Menu(mymenu, tearoff=0)
font_menu.add_command(label='Bold', command=lambda: change_text_style('bold'))
font_menu.add_command(label='Italic', command=lambda: change_text_style('italic'))
font_menu.add_command(label='Underline', command=lambda: change_text_style('underline'))


font_menu.add_separator()
font_menu.add_command(label='Increase Font Size', command=lambda: change_text_size(2))
font_menu.add_command(label='Decrease Font Size', command=lambda: change_text_size(-2))
mymenu.add_cascade(label='Font', menu=font_menu)

view_menu = Menu(mymenu, tearoff=0)
# add zoom in and out commands to the view menu
view_menu.add_command(label="Zoom In", command=zoom_in)
view_menu.add_command(label="Zoom Out", command=zoom_out)
mymenu.add_cascade(label="View", menu=view_menu)


help_menu = Menu(mymenu, tearoff=0)
help_menu.add_command(label='View Help', command=view_help)
help_menu.add_command(label='About Notepad', command=about_notepad)
mymenu.add_cascade(label='Help', menu=help_menu)

gui.mainloop()
