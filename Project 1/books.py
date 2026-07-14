from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/test")
async def first_api():
    return {'message': 'Hello Dan!'}

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/favorite")
async def read_book():
    return { 'book_title': 'favorite book'}

# return by path param
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

#return category by query
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category') == category:
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold() and \
                book.get('author').casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if(BOOKS[i].get('title').casefold() == update_book.get('title').casefold()):
            BOOKS[i] = update_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)

#get all books from a specific author
@app.get("/books/byauthor/{author}")
async def get_books_by_author(author: str):
    books_by_author = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_by_author.append(book)
    return books_by_author

#to run debugger
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("books:app", host="0.0.0.0", port=8000, reload=True)
