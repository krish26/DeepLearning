import os
import requests
from duckduckgo_search import DDGS
from PIL import Image
from io import BytesIO

dataset = {
    "red_cup":[
        "red coffee cup on table",
        "red mug different angles",
        "red ceramic mug kitchen",
        "red cup top view",
        "red mug on desk"
    ],

    "blue_bottle":[
        "blue water bottle on table",
        "blue bottle different angles",
        "blue plastic bottle photography",
        "blue bottle studio photo"
    ],

    "phone":[
        "smartphone on table",
        "mobile phone different angles",
        "phone on desk with objects",
        "smartphone front and back"
    ]
}

base_folder = "dataset"

for label,queries in dataset.items():

    folder = os.path.join(base_folder,label)
    os.makedirs(folder,exist_ok=True)

    count = 0

    for query in queries:

        print("Searching:",query)

        with DDGS() as ddgs:
            results = ddgs.images(query,max_results=100)

            for r in results:

                try:
                    url = r["image"]

                    response = requests.get(url,timeout=5)

                    img = Image.open(BytesIO(response.content))

                    # skip very small images
                    if img.size[0] < 300 or img.size[1] < 300:
                        continue

                    path = os.path.join(folder,f"{label}_{count}.jpg")

                    img.convert("RGB").save(path)

                    count += 1

                except:
                    pass

    print(label,"downloaded:",count)