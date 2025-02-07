from groq import Groq

groq = Groq()
q1 = "Extract the prices(both initial and on-sale if available) of the following list of products from the given image and return them in a JSON format of a similar type to {'name':'product_name','initial_price':'initial_price_of_product','sale_price':'sale_price_of_product'}:"

def get_products_and_prices(list, img):
    question = q1.concat(list)
    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img}",
                        },
                    },
                ],
            }
        ],
        model="llama-3.2-11b-vision-preview",
    )