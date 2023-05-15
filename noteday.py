import tkinter as tk
from tkinter import *
from time import strftime

#criando a tela principal
root = Tk()
root.title('FunNote')
Label(root, text = 'Or\'s funny notebook').pack(side = TOP, pady = 5)

#criando barra de menu
my_menu = Menu(root)
root.config(menu=my_menu)

#click comand func placeholder
def our_command():
    pass

# criando area de texto
text_area= tk.Text()
text_area.pack(fill=BOTH, expand=YES)

# create menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#criando um menu item editavel
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", \
                         accelerator="Ctrl+X", \
                         command=lambda: \
                                 self.editor.event_generate('<<Cut>>'))
edit_menu.add_command(label="Copy", \
                         accelerator="Ctrl+C", \
                         command=lambda: \
                                 self.editor.event_generate('<<Copy>>'))
edit_menu.add_command(label="Paste", \
                         accelerator="Ctrl+V", \
                         command=lambda: \
                                 self.editor.event_generate('<<Paste>>'))

#menu de seleção
select_menu = Menu(my_menu)
my_menu.add_cascade(label="Selection", menu=select_menu)
select_menu.add_command(label="Select all", command=our_command)
select_menu.add_command(label="Select block", command=our_command)
select_menu.add_separator()
select_menu.add_command(label="Selectlast block", command=our_command)

root.mainloop()
