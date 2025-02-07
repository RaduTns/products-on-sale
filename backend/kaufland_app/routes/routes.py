from backend.kaufland_app.services.text_extractor import group_text_by_font_size_and_position, extract_product, extract_initial_price, extract_on_sale_price


def get_products(pdf_path):
    return extract_product(pdf_path)

def get_original_price(pdf_path):
    extract_initial_price(pdf_path)

def get_on_sale_price(pdf_path):
    extract_on_sale_price(pdf_path)