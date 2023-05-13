import csv

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
    print("6. Recommend books to read")
    print("7. Quit")
    print("---------------------------")



# Define a main function
def main():

    # Display the menu
    display_menu()

    # Get the user's choice
    user_choice = input("Please enter your choice (1-7): ")

    # Process the user's choice
    if user_choice == "1":
        print("")
        add_new_books(books)
    elif user_choice == "2":
        remove_book(books)
    elif user_choice == "3":
        search_book(books)
    elif user_choice == "4":
        print_sample_books(books)
    elif user_choice == "5":
        display_random_samples(books)
    elif user_choice == "6":
        recommend_books(books)
    elif user_choice == "7":
        print("Goodbye!")
        global Start
        Start = False
    else:
        print("Invalid choice. Please try again.")


Start = True
while Start:
    main()
