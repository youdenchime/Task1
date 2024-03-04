# Inaitialize empty lists,set, and dictionary 
books_list=[]
author_set=set()
books_dict={} 
#Add books
books_list.append("Python Programming")
author_set.add("Jhon Smith")
books_dict["Python Programming"]="Jhon smith"
books_list.append("data structures and algorithms")
author_set.add("Jane Doe")
books_dict["data structure and algorithms"]="Jane Doe"
books_list.append("Machine Learning Basics")
author_set.add("Alice Johnson")
books_dict["Machine Learing Basics"]="Alice John"
#search for a book
search_title=input("enter the title of the book to search")
if search_title in books_list:
    print(f"Book found! Author:{books_dict[search_title]}")
else:
    print("Book not found!")
# Display all books
print("List of Books:")
for book in books_list:
    print(book)
# Remove a book
remove_title= input("Enter the title of the book to remove or else enter to skip:")
if remove_title in books_list:
    remove_author=books_dict[remove_title] 
    books_list.remove(remove_title)
    author_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book Remove successfully")
    print("Book Available:",books_list)
else:
    print("Book not Found!")