from icrawler.builtin import BingImageCrawler
import os

classes = ["fish", "airplane"]
num_images = 100

for c in classes:
    
    folder = f"dataset/{c}"
    os.makedirs(folder, exist_ok=True)

    print(f"Downloading {c} images...")

    crawler = BingImageCrawler(storage={'root_dir': folder})
    crawler.crawl(keyword=c, max_num=num_images)

print("Download complete!")