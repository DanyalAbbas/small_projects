import pandas
import json

names = pandas.read_csv("names.csv")
stripped = names.iloc[:,[1]].values.flatten().tolist()

# for i in stripped: print(i)
l = []
json_data = json.load(open("smt.json", "r"))
for i in json_data["QueryResponse"]["Customer"]:
    if i["DisplayName"] not in stripped:
        l.append(i)
        print(i["DisplayName"])

json.dump(l, open("missing_names.json", "w"), indent=4)