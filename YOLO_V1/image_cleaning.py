import os
import hashlib
from PIL import Image

folder = "dataset"

hashes = set()

for root, dirs, files in os.walk(folder):
    for file in files:

        path = os.path.join(root, file)

        try:
            with open(path, "rb") as f:
                filehash = hashlib.md5(f.read()).hexdigest()

            # duplicate check
            if filehash in hashes:
                print("Removing duplicate:", path)
                if os.path.exists(path):
                    os.remove(path)
                continue
            else:
                hashes.add(filehash)

            # check if image is valid
            img = Image.open(path)
            img.verify()

        except Exception as e:
            print("Removing corrupted:", path)

            if os.path.exists(path):
                os.remove(path)