import csv

 # TODO: implement searching function 
 
def extractColumns(file_path, indicies):
    with open(file_path, "r", encoding="utf-8") as titles:
        for line in titles:
            fields = line.strip().split("\t")
            selectedData = [fields[i] for i in indicies if i < len(fields)]
            return selectedData

extractColumns("test.tsv", [1, 2, 8])
