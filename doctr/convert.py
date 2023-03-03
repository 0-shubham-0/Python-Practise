import json

# loading the input json file
with open("doctr\input.json") as f:
    data=json.load(f)


data=data[0]
data=data['annotations']
data=data[0]
data=data['result']

# cleaning the json file
# remove the redundant label
for label in data:
    if label.get('value',0):
        if label['value'].get('labels',0)==0 and label['value'].get('text',0)==0:
            data.remove(label)
# even after removing redundant label we still have 2 labels for each label so combining the 2 labels
label_name=[]
for label in data:
    if label.get('value',0) and label['value'].get('labels',0):
        label_name.append(label['value']['labels'])
        data.remove(label)
i=0
for label in data:
    if label.get('original_width',0): del label['original_width']
    if label.get('original_height',0): del label['original_height']
    if label.get('image_rotation',"no")!="no": del label['image_rotation']
    if label.get('from_name',0): del label['from_name']
    if label.get('to_name',0): del label['to_name']
    if label.get('type',0): del label['type']
    if label.get('origin',0): del label['origin']
    if label.get('value',0) and label['value'].get('text',0):
        label['value']['labels']=label_name[i]
        i+=1

i=0
# convertion

children=[]
for label in data:
    if label.get('parentID',0):
        children.append({'parentID':label['parentID']})
        children[i]['text']=label['value']['text']
        box=[]
        box.append(label['value']['x'])
        box.append(label['value']['y'])
        box.append(label['value']['width'])
        box.append(label['value']['height'])
        children[i]['box']=box
        i+=1


i=0
output=[]
for label in data:
    if not label.get('parentID',0):
        if label.get('id',0):output.append({'id':label['id']})
        if label.get('value',0):
            output[i]['text']=label['value']['text']
            box=[]
            box.append(label['value']['x'])
            box.append(label['value']['y'])
            box.append(label['value']['width'])
            box.append(label['value']['height'])
            output[i]['box']=box
            output[i]['linking']=[]
            output[i]['label']=label['value']['labels']
            output[i]['words']=[]
    i+=1

for child in children:
    parentID=child['parentID']
    for label in output:
        if label['id']==parentID:
            label['words'].append(child)
            break
links=[]
for label in data:
    if label.get('from_id',0):
        links.append([label['from_id'],label['to_id']])

for link in links:
    for label in output:
        if link[0]==label['id'] or link[1]==label['id']:
            label['linking'].append(link)


with open("doctr/new.json",'w') as f:
    json.dump(output, f, indent=2)
