import json
import re
from tqdm import tqdm


JsonFile = open('naturalproofs_proofwiki1.json', 'r')
js = json.load(JsonFile)

for i in tqdm(range(len(js['dataset']['theorems']))):
    for j in range(len(js['dataset']['theorems'][i]['proofs'])):
        if js['dataset']['theorems'][i]['proofs'][j]['contents'] == []:
            continue
        prev = js['dataset']['theorems'][i]['proofs'][j]['contents'][0]
        content = []
        for k in range(1, len(js['dataset']['theorems'][i]['proofs'][j]['contents'])):
            item = js['dataset']['theorems'][i]['proofs'][j]['contents'][k]
            x = item[0].isupper()
            y = item[0: 2]
            if x | (y == "{{") & (item != "{{begin-eqn}}"):
                content.append(prev)
                prev = item
            else:
                prev = prev + " " + item
        js['dataset']['theorems'][i]['proofs'][j]['contents'] = content

        if js['dataset']['theorems'][i]['proofs'][j]['contents'] == []:
            continue
        prev = js['dataset']['theorems'][i]['proofs'][j]['contents'][0]
        for k in range(1, len(js['dataset']['theorems'][i]['proofs'][j]['contents'])):
            item = js['dataset']['theorems'][i]['proofs'][j]['contents'][k]
            prev = prev + " \\n " + item
        js['dataset']['theorems'][i]['proofs'][j]['contents'] = prev
result = open("result.json", "w")
result.write(json.dumps(js, indent=2))
JsonFile.close
result.close