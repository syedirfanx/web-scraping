import csv
import json

csvFilePath = "cnn_scraper.csv"
jsonFilePath = "cnn_scraper.json"
data = {}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        hmid = csvRow["Headline"]
        data[hmid] = csvRow

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data))
