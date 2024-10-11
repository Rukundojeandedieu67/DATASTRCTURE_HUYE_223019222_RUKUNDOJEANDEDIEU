class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class BookstoreInventory:
    def __init__(self):
        self.available_books = []  # List for available books
        self.order_queue = []      # Queue for orders
        self.sales_stack = []      # Stack for undoing sales

    def add_book(self, book):
        self.available_books.append(book)
        print(f"Book '{book.title}' added to inventory.")

    def place_order(self, book):
        self.order_queue.append(book)
        print(f"Order placed for '{book.title}'.")

    def process_sale(self, book_title):
        for book in self.available_books:
            if book.title == book_title:
                self.available_books.remove(book)
                self.sales_stack.append(book)
                print(f"'{book.title}' sold.")
                return True
        print(f"Book '{book_title}' not found in inventory.")
        return False

    def undo_sale(self):
        if self.sales_stack:
            book = self.sales_stack.pop()
            self.available_books.append(book)
            print(f"Sale of '{book.title}' undone.")
        else:
            print("No sales to undo.")

    def process_next_order(self):
        if self.order_queue:
            next_order = self.order_queue.pop(0)
            self.add_book(next_order)
            print(f"Processed order for '{next_order.title}'.")
        else:
            print("No orders to process.")

    def display_inventory(self):
        if not self.available_books:
            print("No books available.")
        else:
            print("Available Books:")
            for book in self.available_books:
                print(f"- {book.title} by {book.author} (${book.price})")

# Main program to handle user input
def main():
    inventory = BookstoreInventory()

    while True:
        print("\nOptions:")
        print("1. Add a book to inventory")
        print("2. Place an order")
        print("3. Process a sale")
        print("4. Undo last sale")
        print("5. Process next order")
        print("6. Display inventory")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price:$ "))
            inventory.add_book(Book(title, author, price))

        elif choice == "2":
            title = input("Enter ordered book title: ")
            author = input("Enter ordered book author: ")
            price = float(input("Enter ordered book price: "))
            inventory.place_order(Book(title, author, price))

        elif choice == "3":
            book_title = input("Enter the title of the book to sell: ")
            inventory.process_sale(book_title)

        elif choice == "4":
            inventory.undo_sale()

        elif choice == "5":
            inventory.process_next_order()

        elif choice == "6":
            inventory.display_inventory()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
