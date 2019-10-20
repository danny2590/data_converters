import pandas as pd
import xlrd
import os
import json

# load data
data = pd.read_excel("FINAL Legal_Bot_Questions+intent+entities.xls")

# fill nan with blank
data.fillna(' ',inplace=True)

# extract columns as variables
intent = data['intent']
tasks = data['Task Name'].astype(str)
entity = data['entity'].astype(str)
entity_type = data['entity type'].astype(str)

# format variables for markdown
tasks = "- " + tasks
entity = "(" + entity + ")"
entity_type = "[" + entity_type + "]"

# add new column for concatenating tasks, entities, and entity types
data['tasks_entities'] = tasks + ", " + entity + ", " + entity_type

# copy intents and tasks/entities to new dataframe
df = data[['intent', 'tasks_entities']].copy()

# add formatting to intents
df['intent'] = '## ' + df['intent'].astype(str)

# groupby intents and convert into json string
json_data = df.groupby('intent', sort=False)['tasks_entities'].apply(lambda x: x.tolist()).to_json()

# print(json_data)
j = json.loads(json_data)

# print(j['## int7'])
# with open(os.path.abspath('results.txt'), "a+") as outfile:
#     outfile.write(str(json_data))
# with open(os.path.abspath('results.txt'), "a+") as outfile:
#     outfile.write(str(j))

def json_to_md():
    file = open(os.path.abspath('results.txt'), "a+")
    for key, val in j.items():
        # print(key)
        k = key + '\r\n'
        file.write(k)
        for element in val:
            # print(element.replace(',', ''))
            el = element.replace(',', '')
            # print(el)
            file.write(el + '\r\n')
        # print('\n')
        file.write('\r\n')
    
    file.close()
    return

# with open(os.path.abspath('results.txt'), "a+") as outfile:
#     outfile.write(str(json_to_md()))

json_to_md()
