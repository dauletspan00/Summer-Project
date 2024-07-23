class Item:
    def __init__(self, isbn, title, author, stock, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.stock = stock
        self.price = price

    def __repr__(self):
        return f"\nItem(isbn: {self.isbn}, title: {self.title}, author: {self.author}, price: {self.price})\n"
        

class Bookstore:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def add_items(self, items):
        self.items = self.items + items

    def merge(self, left, right, key):
        items_sorted = []
        while left and right:
            if (getattr(left[0], key) <= getattr(right[0], key)):
                items_sorted.append(left.pop(0))
            else:
                items_sorted.append(right.pop(0))
        items_sorted.extend(left if left else right)
        return items_sorted

    def sort(self, items, key):
        if len(items) == 1:
            return items
    
        mid = len(items) // 2
        items_left = self.sort(items[:mid], key)
        items_right = self.sort(items[mid:], key)

        return self.merge(items_left, items_right, key)
    
    def get_left(self, items, key, value):
        l = 0
        r = len(items) - 1
        result = -1;
        while l <= r:
            m = (l + r) // 2
            if getattr(items[m], key) == value:
                result = m
                r = m - 1
            elif getattr(items[m], key) < value:
                l = m + 1
            else:
                r = m - 1
        return result

    def get_right(self, items, key, value):
        l = 0
        r = len(items) - 1
        result = -1;
        while l <= r:
            m = (l + r) // 2
            if getattr(items[m], key) == value:
                result = m
                l = m + 1
            elif getattr(items[m], key) < value:
                l = m + 1
            else:
                r = m - 1
        return result

    def search(self, key, value):
        items = self.sort(self.items, key)
        if len(items) == 0:
            return None
        left = self.get_left(items, key, value)
        right = self.get_right(items, key, value)
        if left == -1:
            return []
        return items[left:right + 1]
        