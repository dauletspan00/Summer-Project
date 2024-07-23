from bookstore import *
from customer import *
from transaction import *
from printer import *

printer = Printer()
bookstore = Bookstore()
stack = TransactionStack()

queue = CustomersQueue(stack)


item1 = Item("123", "title1", "author1", 5, 1000)
item2 = Item("124", "title2", "author2", 8, 1000)
item3 = Item("125", "title3", "author3", 7, 1000)
item4 = Item("126", "title4", "author4", 9, 4000)
item5 = Item("135", "title5", "author5", 3, 1001)

bookstore.add_item(item1)
bookstore.add_item(item2)
bookstore.add_items([item3, item4, item5])

customer1 = Customer("name1", "bachelor", "MCM", 3)
customer2 = Customer("name2", "phd", "mcm", 2)
customer3 = Customer("name3", "master", "mcm", 2)

queue.push(customer1, "author", "author2")
queue.push(customer2, "price", 1000)
queue.push(customer3, "title", "title2")
queue.push(customer2, "price", 1001)

queue.done()
queue.done()
queue.done()
queue.done()

print(queue.most_popular_request())
print(stack.history)

sorted_by_isbn = bookstore.sort(bookstore.items, 'isbn')
printer.create_table(sorted_by_isbn, "sort by isbn")

sorted_by_title = bookstore.sort(bookstore.items, 'title')
printer.create_table(sorted_by_title, "sort by title")

sorted_by_author = bookstore.sort(bookstore.items, 'author')
printer.create_table(sorted_by_author, "sort by author")

sorted_by_stock = bookstore.sort(bookstore.items, 'stock')
printer.create_table(sorted_by_stock, "sort by stock")

sorted_by_price = bookstore.sort(bookstore.items, 'price')
printer.create_table(sorted_by_price, "sort by price")

print("\nsearch for item with author:")
print(bookstore.search("author", "author1"))

print("\nsearch for item with price:")
print(bookstore.search("price", 1000))

printer.root.mainloop()
