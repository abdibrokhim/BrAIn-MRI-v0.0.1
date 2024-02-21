import csv
import json


def csv_to_jsonl(csv_file, jsonl_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        with open(jsonl_file, 'w') as jsonl:
            for row in reader:
                template = {
                    "prompt": row['Observation'],
                    "completion": row['Conclusion']
                }
                jsonl.write(json.dumps(template) + '\n')


def csv_to_jsonl_2(csv_file, jsonl_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        with open(jsonl_file, 'w') as jsonl:
            for row in reader:
                template = {
                    "text": f"###prompt: {row['Observation']}, ###completion: {row['Conclusion']}"
                }
                jsonl.write(json.dumps(template) + '\n')



def make_csv(file_path, new_file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        with open(new_file_path, 'w', newline='') as new_file:
            writer = csv.DictWriter(new_file, fieldnames=['text'])
            writer.writeheader()
            for row in reader:
                text = f"###prompt: {row['Observation']}, ###completion: {row['Conclusion']}"
                writer.writerow({'text': text})



path_to_csv = 'BrAIn MRI Data 2023 Full.csv'
path_to_jsonl = 'training_v1.jsonl'

# csv_to_jsonl(path_to_csv, path_to_jsonl)
# csv_to_jsonl_2(path_to_csv, path_to_jsonl)


# make_csv(path_to_csv, 'new.csv')
