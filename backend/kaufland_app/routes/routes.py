import os
from time import sleep
from os import walk
from collections import defaultdict
from backend.kaufland_app.services.groq_api import get_products_and_prices
from backend.kaufland_app.services.text_extractor import group_text_by_font_size_and_position, extract_product, \
    extract_initial_price, extract_on_sale_price, split_products_per_page
from backend.utils.pdf_processing import pdf_to_jpeg


def get_products(pdf_path, groq):
    result = {}
    products = split_products_per_page(extract_product(pdf_path))
    images = pdf_to_jpeg(pdf_path)
    i = 0
    filenames = next(walk(r"D:/GIT Repo/products-on-sale/backend/images/"), (None, None, []))[2]
    print(filenames)
    for page in products:
         text = r"D:/GIT Repo/products-on-sale/backend/images/"+filenames[i]
         result[page] = get_products_and_prices(str(products[page]), text, groq)
         sleep(10)
         i = i+1
    return result

def get_original_price(pdf_path):
    extract_initial_price(pdf_path)

def get_on_sale_price(pdf_path):
    extract_on_sale_price(pdf_path)