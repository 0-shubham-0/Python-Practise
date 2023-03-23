import copy
import json
with open("conversion/reference.json") as f:
    data = json.load(f)


filePath = "path"
imgHeight = 100
imgWidth = 100
output = {
    "data": {
        "ocr": filePath
    },
    "predictions": [{
        "results": [

        ]
    }
    ]
}
template = {
    "original_width": imgWidth,
    "original_height": imgHeight,
    "image_rotation": 0,
    "value": {
        "x": 0,
        "y": 0,
        "width": 0,
        "height": 0,
        "rotation": 0
    },
    "id": "",
    "from_name": "bbox",
    "to_name": "image",
    "type": "rectangle",
    "origin": "manual"
}


def getLabel(label, id=None):
    t = template.copy()
    t['value']['x'] = label['box'][0]
    t['value']['y'] = label['box'][1]
    t['value']['width'] = label['box'][2]-label['box'][0]
    t['value']['height'] = label['box'][3]-label['box'][1]
    if 'id' in label:
        t['id'] = label['id']
    else:
        t['id'] = id
    return t


i = 0
for label in data:
    filledLabel1 = copy.deepcopy(getLabel(label))
    filledLabel2 = copy.deepcopy(getLabel(label))
    filledLabel2['value']['text'] = label['text'][0]
    output["predictions"][0]["results"].append(filledLabel1)
    output["predictions"][0]["results"].append(filledLabel2)
    if 'words' in label:
        for word in label['words']:
            filledLabel3 = copy.deepcopy(getLabel(word, i))
            i += 1
            filledLabel4 = copy.deepcopy(getLabel(word, i))
            i += 1
            filledLabel4['value']['text'] = word['text'][0]
            output["predictions"][0]["results"].append(filledLabel3)
            output["predictions"][0]["results"].append(filledLabel4)
    filledLabel1.clear
    filledLabel2.clear
    filledLabel3.clear
    filledLabel4.clear
    break
with open("newoutput.json",'w') as f:
    json.dump(output, f, indent=2)