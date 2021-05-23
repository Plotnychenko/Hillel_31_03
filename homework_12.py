# Homework 12
# E. Plotnychenko

import csv
import requests

url = "http://api.forismatic.com/api/1.0/"

def create_quote_list(quantity):
    quote_list = []
    count = 0
    while count < quantity:
        params = {
            "method": "getQuote",
            "format": "json",
            "key": count
        }
        random_quote = requests.get(url, params=params).json()
        if len(random_quote["quoteAuthor"]) > 0:
            quote_format = {"Author": random_quote["quoteAuthor"],
                            "Quote": random_quote["quoteText"],
                            "URL": random_quote["quoteLink"]}
            quote_list.append(quote_format)
            count += 1
    return quote_list


def quote_sort_by_author(quote_list):
    author = quote_list.get("Author")
    return author


def quote_list_to_csv(quote_list, filename="Quote_List.csv"):
    with open(filename, 'w', encoding="utf-8") as csv_file:
        fieldnames = ["Author", "Quote", "URL"]
        sort_quotes = sorted(quote_list, key=quote_sort_by_author)
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for value in sort_quotes:
            writer.writerow(value)

quote_list = create_quote_list(5)
quote_list_to_csv(quote_list)