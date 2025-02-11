import base64
from io import BytesIO

q1 = "Extract the prices(both initial and on-sale if available) of the following list of products from the given image and return them in a JSON format of the type to [{'name':'product_name','initial_price':'initial_price_of_product','sale_price':'sale_price_of_product'}]. Provide as an output ONLY the json formatted text, nothing else, absolutely nothing else extra please!"

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_products_and_prices(list: str, img, groq):
    base64_image = encode_image(img)
    question = q1 + list
    print(question)
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model="llama-3.2-11b-vision-preview",
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content