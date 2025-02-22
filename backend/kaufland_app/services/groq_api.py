import base64
from io import BytesIO

q1 = "From the given image, please extract the initial price and discount price for the following products in a json format of tuples having name, initial_price and discounted_price:"
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_products_and_prices(list: str, img, groq):
    base64_image = encode_image(img)
    question = q1 + list
    print(question)
    try:
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
            temperature = 0.3,
            response_format={"type": "json_object"},


        )
        print(chat_completion.choices[0].message.content)
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(e)
        return None