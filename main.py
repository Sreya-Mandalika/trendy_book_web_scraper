import requests
from bs4 import BeautifulSoup
import random
import time

def fetch_trending_books(url):
    books = []
    page = 1
    while True:
        print(f"Fetching all pages...")
        response = requests.get(f"{url}?page={page}")
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
            break
        
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all book containers, and find all books in those containers
        book_containers = soup.find_all('div', class_='sri__main') 
        
        if not book_containers:
            print("No more books found or no valid page.")
            break
        
        for book in book_containers:
            title_tag = book.find('a', class_='results') 
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = 'https://openlibrary.org' + title_tag.get('href')
                books.append((title, link))
        
        # Check if there is a "next" button and move to the next page
        next_button = soup.find('a', string='Next')
        if not next_button:
            break
        
        page += 1
        time.sleep(1) #to avoid bothering the server too much
    
    return books

def get_random_book(books):
    if not books:
        return None
    return random.choice(books)


def display_book(book):
    if book:
        title, link = book
        print(f"Random Book:\nTitle: {title}\nLink: {link}")
    else:
        print("No book found.")


def main():
    url = 'https://openlibrary.org/trending/now'
    books = fetch_trending_books(url)
    random_book = get_random_book(books)
    display_book(random_book)


if __name__ == "__main__":
    main()
