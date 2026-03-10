# from icrawler.builtin import BingImageCrawler
# import os

# dataset = {
#     "red_cup":[

#         "red cup on messy desk"
#     ],

#     "blue_bottle":[

#         "blue bottle on table with objects",
#         "blue bottle next to laptop"
#     ],

#     # "phone":[
#     #     "smartphone on table",
#     #     "mobile phone different angles",
#     #     "phone on desk with objects",
#     #     "smartphone front and back",
#     #     "phone on desk with laptop",
#     #     "cup and phone on table"
#     # ]
# }


# dataset_path = "dataset"

# for label,queries in dataset.items():

#     folder = os.path.join(dataset_path,label)
#     os.makedirs(folder,exist_ok=True)

#     for q in queries:

#         print("Downloading:",q)

#         crawler = BingImageCrawler(
#             feeder_threads=1,
#             parser_threads=2,
#             downloader_threads=4,
#             storage={'root_dir':folder}
#         )

#         crawler.crawl(
#             keyword=q,
#             max_num=10,
#             min_size=(300,300)   # avoid tiny images
#         )


# Install first if not installed:
# pip install duckduckgo-search requests tqdm
import os
import time
import random
import requests
from tqdm import tqdm
from ddgs import DDGS

# Queries to search
search_queries = [

    "people holding smartphone",
    "phone on desk with objects"
]

# Output folder
output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)


def download_images(query, limit=30, retries=3):

    print(f"\nSearching images for: {query}")

    for attempt in range(retries):

        try:
            with DDGS() as ddgs:
                results = list(ddgs.images(query, max_results=limit))

            if not results:
                print("No results found")
                return

            query_folder = os.path.join(
                output_folder, query.replace(" ", "_"))
            os.makedirs(query_folder, exist_ok=True)

            for i, img in enumerate(tqdm(results, desc="Downloading")):

                try:
                    url = img["image"]

                    response = requests.get(url, timeout=10)

                    ext = url.split(".")[-1].split("?")[0]

                    if ext.lower() not in ["jpg", "jpeg", "png"]:
                        ext = "jpg"

                    filepath = os.path.join(query_folder, f"{i+1}.{ext}")

                    with open(filepath, "wb") as f:
                        f.write(response.content)

                except Exception as e:
                    print(f"Failed image {i+1}: {e}")

            print(f"Finished downloading for '{query}'")

            return

        except Exception as e:

            print(f"Attempt {attempt+1} failed: {e}")

            wait = random.randint(5, 10)
            print(f"Waiting {wait} seconds before retry...")
            time.sleep(wait)

    print(f"Failed completely for {query}")


# Run downloader
for query in search_queries:

    download_images(query, limit=30)

    # delay between queries to avoid rate limit
    time.sleep(random.randint(5, 8))