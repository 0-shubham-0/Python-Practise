import json
class Convs:
    def mlToLabel(self,jsonPath:str,imgPath:str,height,width):
        import copy
        with open(jsonPath) as f:
            data = json.load(f)
        data=data['form']
        filePath = imgPath
        imgHeight = height
        imgWidth = width
        output = {
            "data": {
                "ocr": filePath
            },
            "predictions": [{
                "result": []
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
            t['value']['x'] = (label['box'][0] / width) * 100
            t['value']['y'] = (label['box'][1] / height) * 100
            t['value']['width'] = ((label['box'][2]-label['box'][0])/width)*100
            t['value']['height'] = ((label['box'][3]-label['box'][1])/height) * 100.0
            t['id'] = str(id)
            return t


        i = 11
        for label in data:
            filledLabel1 = copy.deepcopy(getLabel(label,i))
            filledLabel2 = copy.deepcopy(getLabel(label,i))
            i+=1
            filledLabel2['value']['text'] = [label['text']]
            filledLabel2['from_name']="transcription"
            filledLabel2['type']="textarea"
            output["predictions"][0]["result"].append(filledLabel1)
            output["predictions"][0]["result"].append(filledLabel2)
            if 'words' in label:
                for word in label['words']:
                    filledLabel3 = copy.deepcopy(getLabel(word, i))
                    filledLabel4 = copy.deepcopy(getLabel(word, i))
                    i += 1
                    filledLabel4['value']['text'] = [word['text']]
                    filledLabel4['from_name']="transcription"
                    filledLabel4['type']="textarea"
                    output["predictions"][0]["result"].append(filledLabel3)
                    output["predictions"][0]["result"].append(filledLabel4)
                    filledLabel3.clear
                    filledLabel4.clear
            filledLabel1.clear
            filledLabel2.clear
        with open("./conversion2/forLabel.json",'w') as f:
            json.dump(output, f, indent=2)
    def labelToMl(self,path:str):
        def getBox(l:dict):
            box=[]
            box.append(l['value']['x'])
            box.append(l['value']['y'])
            box.append(l['value']['x']+l['value']['width'])
            box.append(l['value']['y']+l['value']['height'])
            return box


        # loading the input json file
        with open(path) as f:
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
        # label_name=[]
        # for label in data:
        #     if label.get('value',0) and label['value'].get('labels',0):
        #         label_name.append(label['value']['labels'])
        #         data.remove(label)
        # remove redundant keys
        i=0
        for label in data:
            if label.get('original_width',0): del label['original_width']
            if label.get('original_height',0): del label['original_height']
            if label.get('image_rotation',"no")!="no": del label['image_rotation']
            if label.get('from_name',0): del label['from_name']
            if label.get('to_name',0): del label['to_name']
            if label.get('type',0): del label['type']
            if label.get('origin',0): del label['origin']
            # if label.get('value',0) and label['value'].get('text',0):
            #     label['value']['labels']=label_name[i]
            #     i+=1

        i=0

        # convertion
        # creting list of children word or sub-words
        children=[]
        for label in data:
            if label.get('parentID',0):
                children.append({'parentID':label['parentID']})
                children[i]['text']=label['value']['text']
                children[i]['box']=getBox(label)
                i+=1

        # creating the output
        i=0
        output=[]
        for label in data:
            if not label.get('parentID',0):
                if label.get('id',0):output.append({'id':label['id']})
                # print(output,i)
                if label.get('value',0):
                    output[i]['text']=label['value']['text']
                    output[i]['box']=getBox(label)
                    output[i]['linking']=[]
                    # output[i]['label']=label['value']['labels']
                    output[i]['words']=[]
                i+=1

        # adding the sub-words
        for child in children:
            parentID=child['parentID']
            for label in output:
                if label['id']==parentID:
                    label['words'].append(child)
                    break

        # getting the links between labels
        links=[]
        for label in data:
            if label.get('from_id',0):
                links.append([label['from_id'],label['to_id']])

        # adding the links to output
        for link in links:
            for label in output:
                if link[0]==label['id'] or link[1]==label['id']:
                    label['linking'].append(link)

        # creating output json file
        with open("./conversion2/changedMl.json",'w') as f:
            json.dump(output, f, indent=2)
    def csvToMl(self,path:str):
        
        import pandas as pd
        df=pd.read_csv(path)
        # delete the second and third column
        df.drop(df.columns[[5,6,7,8,9,10,11,12]], axis=1, inplace=True)
        ids=10
        template = {
            "id": 0,
            "text": [],
            "box": []
        }
        output={
            "form": []
        }
        # iterate over the dataframe
        for index, row in df.iterrows():
            # create a new label
            label=template.copy()
            # set the label id
            label['id']=str(ids)
            # set the label text
            label['text']=row['word']
            # set the label box
            label['box']=[row['word_x1'],row['word_y1'],row['word_x2'],row['word_y2']]
            # add the label to the output
            output['form'].append(label)
            # increment the label id
            ids+=1
        outputPath="./conversion2/mlData.json"
        with open(outputPath,'w') as f:
            json.dump(output, f, indent=2)

csv_path="./conversion2/line_details.csv"
obj=Convs()
# obj.csvToMl(csv_path)
# obj.mlToLabel("D:\Python\Practise\conversion2\mlData.json","/data/upload/17/35cccf03-laxmi-may_0001-1_deskew_corrected.jpg",5000,3538)
obj.labelToMl("D:/Python/Practise/conversion2/fromlabel.json")