def load_books_from_csv(file_path):
    """
    Load books from a CSV file.
    """
    books = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            books.append(row)
    return books


# Load the books from the CSV file
books = load_books_from_csv('books.csv')


def display_menu():
    """Display the menu of choices."""
    print("Library Management System")
    print("---------------------------")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Print sample books")
    print("5. Display a random sample of books")
    print("6. Quit")
    print("---------------------------")

