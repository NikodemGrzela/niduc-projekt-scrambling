import csv

def write_data(data,name):
    with open(name + ".csv", mode="w") as csvfile:
        headers = ["DBE_probability","XOR_probability","V34_probability"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in data:
            csvfile.write(row + '\n')