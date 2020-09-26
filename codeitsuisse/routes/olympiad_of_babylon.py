import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluateOly():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    books = data.get("books")
    days = data.get("days")
    best = solve(books,days)
    resultDict = {"optimalNumberOfBooks" : best}

    return json.dumps(resultDict)

def solve(books, days, books_read=0, max_books=0):
    # all books are read
    if books_read == len(books):
        return books_read
    if books_read > max_books:
        max_books = books_read
    for i, day in enumerate(days):
        for j, book in enumerate(books):
            if book > day:
                break
            if book > 0:
                days[i] -= book
                books[j] = 0
                max_books = solve(sorted(books), sorted(days), books_read + 1, max_books)
                if max_books == len(books):
                    return max_books
                days[i] += book
                books[j] = book
    return max_books





