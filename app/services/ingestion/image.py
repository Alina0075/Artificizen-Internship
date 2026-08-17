import os
import base64
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def extract_image(file_path: str):
    with open(file_path, "rb") as f:
        image_data = base64.b64encode(
            f.read()
        ).decode("utf-8")

    ext = file_path.split(".")[-1].lower()
    if ext in ["jpg", "jpeg"]:
        mime = "image/jpeg"
    elif ext == "png":
        mime = "image/png"
    else:
        raise ValueError(
            f"Unsupported image format: {ext}"
        )

    response = client.chat.completions.create(
        model="google/gemma-3-12b-it:free",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": (
                                f"data:{mime};base64,"
                                f"{image_data}"
                            )
                        }
                    },
                    {
                        "type": "text",
                        "text": (
                            "Describe this image in detail. "
                            "Extract all visible text, data, "
                            "labels, and any relevant "
                            "cybersecurity information."
                        )
                    }
                ]
            }
        ]
    )

    return [
        response.choices[0].message.content
    ]