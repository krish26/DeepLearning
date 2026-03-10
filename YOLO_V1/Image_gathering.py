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




# Importing the module
from google_images_download import google_images_download
import os
import time

# Create object
response = google_images_download.googleimagesdownload()

# Search queries
search_queries = [
    "blue bottle on table with objects",
    "blue bottle next to laptop",
    "smart phone in different angles",
    "phone on desk with objects",
]

# Function to download images
def download_images(query, limit=100):
    # Arguments for downloading
    arguments = {
        "keywords": query,
        "format": "jpg",
        "limit": limit,
        "print_urls": True,
        "size": "medium",
        "aspect_ratio": "square",
        "output_directory": "downloaded_images",  # All images saved here
    }

    try:
        print(f"Downloading images for query: '{query}' ...")
        response.download(arguments)
        print(f"✅ Completed: {query}\n")
    except FileNotFoundError:
        print(f"Folder not found for query: {query}, retrying without aspect_ratio...")
        arguments.pop("aspect_ratio", None)
        try:
            response.download(arguments)
            print(f"✅ Completed (without aspect_ratio): {query}\n")
        except Exception as e:
            print(f"❌ Failed to download images for '{query}': {e}\n")
    except Exception as e:
        print(f"❌ Unexpected error for '{query}': {e}\n")

# Driver code
for query in search_queries:
    download_images(query)
    time.sleep(2)  # Wait 2 seconds between queries to reduce request load