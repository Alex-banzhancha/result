import json
from tqdm import tqdm

'''
JsonFile = open('final.json', 'r')
js = json.load(JsonFile)
f = open("datasetsBase.json", 'r')
ds = json.load(f)
for i in tqdm(range(len(js['dataset']['theorems']))):
    ds['dataset']['theorems'].append({})
    ds['dataset']['theorems'][i]['id'] = i
    ds['dataset']['theorems'][i]['title'] = js['dataset']['theorems'][i]['title']

    contents = []
    for j in js['dataset']['theorems'][i]['proofs']:
        contents.append(j['contents'])
    ds['dataset']['theorems'][i]['proofs'] = contents
result = open("datasets.json", "w")
result.write(json.dumps(ds, indent=2))
JsonFile.close
result.close
'''

JsonFile = open('final.json', 'r')
js = json.load(JsonFile)
f = open("datasetsBase.json", 'r')
ds = json.load(f)
for i in tqdm(range(len(js['dataset']['theorems']))):
    for j in js['dataset']['theorems'][i]['proofs']:
        if j['contents'] == []:
            contents = None
        else:
            contents = j['contents']
        ds['dataset'].append({'title': js['dataset']['theorems'][i]['title'],
                                      'proof':contents})
result = open("data.json", "w")
result.write(json.dumps(ds, indent=2))
JsonFile.close
result.close

