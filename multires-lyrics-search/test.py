import os
import json

path = "./data"

files = os.listdir(path)
print(files)
for file in files:
    try:
        with open(os.path.join(path, file)) as f:
            scanJson = json.load(f)

            text = ""
            for page in scanJson:

                try:
                    text += page["X-TIKA:content"]
                except Exception as ex:
                    print(ex)
                    pass
                print(text)
    except Exception as ex1:
        print(ex1)
        pass