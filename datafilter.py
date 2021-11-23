import json
import re
from tqdm import tqdm


JsonFile = open('naturalproofs_proofwiki2.json', 'r')
js = json.load(JsonFile)

for i in tqdm(range(len(js['dataset']['theorems']))):
    if js['dataset']['theorems'][i]['contents'] == []:
        continue
    prev = js['dataset']['theorems'][i]['contents'][0]
    content = []
    for k in range(1, len(js['dataset']['theorems'][i]['contents'])):
        item = js['dataset']['theorems'][i]['contents'][k]
        x = item[0].isupper()
        y = item[0: 2]
        if x | (y == "{{"):
            content.append(prev)
            prev = item
        else:
            prev = prev + " \n " + item
    if len(content) == 0:
        content.append(prev)
    js['dataset']['theorems'][i]['contents'] = content
result = open("result.json", "w")
result.write(json.dumps(js, indent=2))
JsonFile.close
result.close