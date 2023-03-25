import json
import pandas as pd
df=pd.read_csv("line_details.csv")
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
    label['box']=[row['word_x1'],row['word_y1'],row['word_x2']+row['word_y2']]
    # add the label to the output
    output['form'].append(label)
    # increment the label id
    ids+=1

with open("./conversion/mlData.json",'w') as f:
    json.dump(output, f, indent=2)