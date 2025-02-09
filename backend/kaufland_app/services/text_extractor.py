from collections import defaultdict

import fitz  # PyMuPDF
from typing import List, Dict, Any
from backend.utils.pdf_processing import process_text_block


def extract_text_blocks(page) -> List[Dict[str, Any]]:
    try:
        return page.get_text("dict")["blocks"]
    except KeyError:
        return []


def group_text_by_font_size_and_position(pdf_path: str) -> List[Dict[str, Any]]:
    try:
        with fitz.open(pdf_path) as doc:
            groups = []

            for page_number in range(len(doc)):
                page = doc.load_page(page_number)
                text_blocks = extract_text_blocks(page)

                current_group = []
                previous_font_size = None
                group_positions = []

                for block in text_blocks:
                    if block.get('type') == 0:  # Process text blocks only
                        previous_font_size, current_group, group_positions = process_text_block(
                            block, previous_font_size, current_group, group_positions, groups, page_number + 1
                        )
            return groups

    except Exception as e:
        raise RuntimeError(f"Failed to process PDF: {e}")

def extract_product(pdf_path):
    results = []
    try:
        text_groups = group_text_by_font_size_and_position(pdf_path)
        for group in text_groups:
          if (group["font_size"] ==10):
            results.append(group)
    except FileNotFoundError:
        print(f"File not found: {pdf_path}")
    except RuntimeError as e:
        print(e)
    return results

def extract_initial_price(pdf_path):
    try:
        text_groups = group_text_by_font_size_and_position(pdf_path)
        for group in text_groups:
          if (group["font_size"] >=15.5 and group["font_size"]<=16.5):
            print(group)
    except FileNotFoundError:
        print(f"File not found: {pdf_path}")
    except RuntimeError as e:
        print(e)

def extract_on_sale_price(pdf_path):
    try:
        text_groups = group_text_by_font_size_and_position(pdf_path)
        for group in text_groups:
          if (group["font_size"] >=26 and group["font_size"]<=27.5):
            print(group)
    except FileNotFoundError:
        print(f"File not found: {pdf_path}")
    except RuntimeError as e:
        print(e)

def split_products_per_page(list_of_products):
    products_per_page = defaultdict(list)
    for product in list_of_products:
        products_per_page[product["page_number"]].append(product["group_text"])
    return products_per_page


