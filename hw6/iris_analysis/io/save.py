import csv
def save_data(file_name, results, results_labels, labels):
    with open(file_name, "w") as fp:
        writer = csv.writer(fp)
        labels.insert(0, '')
        writer.writerow(labels)
        for count, lst in enumerate(results):
            lst.insert(0, results_labels[count])
            writer.writerow(lst)
