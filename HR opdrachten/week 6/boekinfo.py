# fucntie om een boek te kunnen zoeken
def search_book(books, term):
    # Hoogletters verlagen zodat het makkelijker is om een boek te vinden
    term = term.lower()
    # door de boeken heen loepen totdat je een boek kan vinden van wat je zoekt, als er geen boek is, return false
    for book in books:
        if term in book['title'].lower() or term in book['author'].lower() or term in book['publisher'].lower():
            return True
    return False


# main functie
def main():
    books = []  # boek info opslaan

    while True:
        # opties laten zien
        choice = input("[A] Add book\n[S] Search book\n[E] Exit (and print)\nYour choice: ").strip().upper()

        if choice == 'A':
            # nieuwe boek toevoegen
            book_details = input("Book details (title,author,publisher,publication date): ").strip()
            # input in commas splitsen
            title, author, publisher, pub_date = [item.strip() for item in book_details.split(",")]
            
            # kijk of boek titel al bestaat
            if any(book['title'].lower() == title.lower() for book in books):
                print("Book with this title already exists.")
            else:
                # Boek toevoegen in de lijst van dictionary
                books.append({'title': title, 'author': author, 'publisher': publisher, 'pub_date': pub_date})
                print("Book has been added")
        
        elif choice == 'S':
            # zoek voor de boek met termen
            search_term = input("Search term: ").strip()
            if search_book(books, search_term):
                print(f"Found a book for: {search_term}")
            else:
                print(f"No book found for: {search_term}")
        
        elif choice == 'E':
            # programma sluiten en de hele lijst uitprintten
            print("\nAll books:")
            for book in books:
                print(book)
            break
        
        else:
            print("Invalid choice. Please select A, S, or E.")

# programma runnen
if __name__ == "__main__":
    main()
