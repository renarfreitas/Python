#TreeView
from tkinter import *
from tkinter import ttk

app = Tk()

app.title("CFB Cursos")
app.geometry("600x300")

listaNomes = [['0', 'Brertilda', '9875'], ['1', 'Crisloid', '2341'], ['0', 'Julsivam', '3784']]

tv = ttk.Treeview(app, columns = ('id', 'nome', 'fone'), show = 'headings')
tv.column('id', minwidth = 0, width = 50)
tv.column('nome', minwidth = 0, width = 250)
tv.column('fone', minwidth = 0, width = 100)

tv.heading('id', text = 'ID')
tv.heading('nome', text = 'NOME')
tv.heading('fone', text = 'TELEFONE')
tv.pack()

for (i, n, f) in listaNomes:
  tv.insert("","end", values = (i, n, f))
app.mainloop()