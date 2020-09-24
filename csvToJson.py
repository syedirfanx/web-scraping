import csv
import json

csvFilePath = "BSoup_3.csv"
jsonFilePath = "BSoup_3.json"
data = {}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        hmid = csvRow["Headline"]
        data[hmid] = csvRow

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data))
