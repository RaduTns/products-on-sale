import base64
from io import BytesIO

q1 = "Extract the prices(both initial and on-sale if available) of the following list of products from the given image and return them in a JSON format of a similar type to {'name':'product_name','initial_price':'initial_price_of_product','sale_price':'sale_price_of_product'}:"

def get_products_and_prices(list: str, img, groq):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    question = q1 + list
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image}",
                        },
                    },
                ],
            }
        ],
        model="llama-3.2-11b-vision-preview",
    )
    return chat_completion.choices[0].message.content