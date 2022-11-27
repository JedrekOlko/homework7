import csv
def load_data(file):
    with open(file, encoding='utf-8') as fp:
        csvreader = csv.reader(fp)
        rows = []
        for row in csvreader:
            rows.append(row)
        return rows