from backend.kaufland_app.routes.routes import get_products

pdf_path = "Kaufland-23-12-2024-24-12-2024-04.pdf"  # Path to your PDF file

list = get_products(pdf_path)

for item in list:
    if(item["page_number"] == 2):
        print(item["group_text"])