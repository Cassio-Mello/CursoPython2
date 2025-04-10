'''
📚 Exercício: Sistema de Controle de Biblioteca
Crie um programa em Python para gerenciar os livros de uma biblioteca. O sistema deve permitir:

📌 Funcionalidades:
Adicionar livro

O usuário informa: título, autor e ano de publicação.

Armazene os livros em um dicionário onde a chave é o título e o valor é outro dicionário com os demais dados.

Buscar livro por título

O usuário digita o título e o sistema mostra os dados do livro, se encontrado.

Listar todos os livros

Mostra todos os livros cadastrados com título, autor e ano.

Remover livro

O usuário informa o título e o livro é removido da biblioteca.

Sair do programa
'''

#dicio nario biblioteca

# books = {}

# #função par adicionar livro
# def add_book():
#     title = input('Enter title: ')
#     author = input('Enter author: ')
#     year_of_publication = input('Enter year of publication: ')
#     category = input('Enter category: ')
#     status = input('Enter status (Avaliable or leased): ')

#     books[title] = {'author' : author, 'year_of_publication' : year_of_publication, 'category' : category, 'status' : status} 

#     print(f'{title} successfully added! ✅')

# #Função para buscar por titulo
# def search_by_title():
#     title = input('\n🔎 Enter the title for search: ')

#     book = books.get(title)  # tenta pegar o livro pelo título

#     if book:
#         print(f'\n📙 Title "{title}" found!😀')
#         print(f'    Author: {book.get("author")}')
#         print(f'    Year of publication: {book.get("year_of_publication")}')
#         print(f'    Category: {book.get("category")}')
#         print(f'    Status: {book.get("status")}')
#     else:
#         print('❌ Title not found 😔!')

# def list_all():

#     if books:
#         for title, data in books.items():
#             print(f'Title: {title} ')
#             print(f'    Author: {data["author"]}')
#             print(f'    Year of publication: {data["year_of_publication"]}')
#             print(f'    Category: {data["category"]}')
#             print(f'    Status: {data["status"]}')
#     else:
#         print('📭Empty library')


# def rent_a_book():
#     book_for_rent = input('📘 Enter the title to rent: ')

#     if book_for_rent in books:
#         status = books[book_for_rent]["status"].lower()
        
#         if status == "available":
#             books[book_for_rent]["status"] = "Leased"
#             print(f'✅ The book "{book_for_rent}" was successfully rented!')
#         elif status == "leased":
#             print(f'❌ Sorry, the book "{book_for_rent}" is already leased.')
#         else:
#             print(f'⚠️ Unknown status for book "{book_for_rent}".')
#     else:
#         print('❌ Title not found 😔!')

import tkinter as tk
from tkinter import messagebox, simpledialog

books = {}

# Funções principais
def add_book():
    title = simpledialog.askstring("Add Book", "Enter book title:")
    if not title: return
    author = simpledialog.askstring("Add Book", "Enter author:")
    year = simpledialog.askstring("Add Book", "Enter year of publication:")
    category = simpledialog.askstring("Add Book", "Enter category:")
    status = simpledialog.askstring("Add Book", "Enter status (Available or Leased):")

    if title and author and year and category and status:
        books[title] = {
            'author': author,
            'year_of_publication': year,
            'category': category,
            'status': status.capitalize()
        }
        messagebox.showinfo("Success ✅", f'"{title}" added successfully!')
    else:
        messagebox.showwarning("Warning ⚠️", "All fields must be filled!")

def search_by_title():
    title = simpledialog.askstring("Search Book", "Enter title to search:")
    if title in books:
        book = books[title]
        message = (
            f'Title: {title}\n'
            f'Author: {book["author"]}\n'
            f'Year: {book["year_of_publication"]}\n'
            f'Category: {book["category"]}\n'
            f'Status: {book["status"]}'
        )
        messagebox.showinfo("Book Found 📚", message)
    else:
        messagebox.showerror("Not Found ❌", "Book not found!")

def list_all():
    if books:
        all_books = ""
        for title, book in books.items():
            all_books += (
                f'\n📘 {title}\n'
                f'  Author: {book["author"]}\n'
                f'  Year: {book["year_of_publication"]}\n'
                f'  Category: {book["category"]}\n'
                f'  Status: {book["status"]}\n'
            )
        messagebox.showinfo("Library 📚", all_books)
    else:
        messagebox.showinfo("Empty 📭", "Library is empty.")

def rent_a_book():
    title = simpledialog.askstring("Rent Book", "Enter title to rent:")
    if title in books:
        if books[title]["status"].lower() == "available":
            books[title]["status"] = "Leased"
            messagebox.showinfo("Rented ✅", f'Book "{title}" successfully rented!')
        else:
            messagebox.showwarning("Unavailable ❌", f'Book "{title}" is already leased.')
    else:
        messagebox.showerror("Not Found ❌", "Book not found!")

# Criando a janela principal
app = tk.Tk()
app.title("📚 Digital Library")
app.geometry("300x400")

# Estilo dos botões padrão
button_style = {
    "width": 25,
    "height": 2,
    "bg": "#4CAF50",
    "fg": "white",
    "font": ("Arial", 10, "bold")
}

# Título
label = tk.Label(app, text="📖 Library Manager", font=("Arial", 14, "bold"))
label.pack(pady=20)

# Botões principais
tk.Button(app, text="➕ Add Book", command=add_book, **button_style).pack(pady=5)
tk.Button(app, text="🔎 Search Book", command=search_by_title, **button_style).pack(pady=5)
tk.Button(app, text="📋 List All Books", command=list_all, **button_style).pack(pady=5)
tk.Button(app, text="📕 Rent Book", command=rent_a_book, **button_style).pack(pady=5)

# Botão de sair com estilo direto (sem usar button_style)
tk.Button(
    app,
    text="❌ Exit",
    command=app.quit,
    width=25,
    height=2,
    bg="red",
    fg="white",
    font=("Arial", 10, "bold")
).pack(pady=20)

# Inicia o programa
app.mainloop()

