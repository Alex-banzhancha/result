import json
from tqdm import tqdm

'''
JsonFile = open('final.json', 'r')
js = json.load(JsonFile)
f = open("datasetsBase.json", 'r')
ds = json.load(f)
for i in tqdm(range(len(js['dataset']['theorems']))):
    ds['dataset'].append({})
    ds['dataset'][i]['title'] = js['dataset']['theorems'][i]['title']

    contents = []
    for j in js['dataset']['theorems'][i]['proofs']:
        if j['contents'] != []:
            contents.append(j['contents'])
    if contents == []:
        contents = None
    ds['dataset'][i]['proofs'] = contents
result = open("datasets.json", "w")
result.write(json.dumps(ds, indent=2))
JsonFile.close
result.close


'''
JsonFile = open('final.json', 'r')
js = json.load(JsonFile)
f = open("datasetsBase.json", 'r')
ds = json.load(f)
a = 0
b = 0
c = 0
d = 0
for i in tqdm(range(len(js['dataset']['theorems']))):
    b += 1
    if js['dataset']['theorems'][i]['proofs'] == []:
            c += 1
    else:
        d += 1
        for j in js['dataset']['theorems'][i]['proofs']:
            a += 1
            if j['contents'] == []:
                contents = None
            elif "ProofWanted" in j['contents']:
                contents = None
            else:
                contents = j['contents']
            ds['dataset'].append({'title': js['dataset']['theorems'][i]['title'], 'proof':contents})

print(a)
print(b)
print(c)
print(d)
result = open("data.json", "w")
result.write(json.dumps(ds, indent=2))
JsonFile.close
result.close
