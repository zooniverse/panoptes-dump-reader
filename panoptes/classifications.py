import pandas
import json

def load_csv(filename):
    with open(filename) as f:
        df = load_from(f)
    return df

def load_from(f):
    df = pandas.read_csv(f)

    subject_data = df['subject_data'].apply(lambda cell: json.loads(cell).values()[0])
    add_columns(df, subject_data, prefix="subject_data")

    metadata = df['metadata'].apply(lambda cell: json.loads(cell))
    add_columns(df, metadata, prefix="metadata")

    annotations = df['annotations'].apply(lambda cell: json.loads(cell))
    task_names = set([i["task"] for annotation in annotations for i in annotation])
    for name in task_names:
        tasks = [next((task for task in tasks if task['task'] == name), None) for tasks in annotations]
        add_columns(df, tasks, 'annotations_' + name)

    return df

def add_columns(df, data, prefix=None):
    if prefix:
        prefix = prefix + "_"

    column_names = set()
    for item in data:
        if item:
            for key in item.keys():
                column_names.add(key)

    for key in column_names:
        if key != '':
            df[prefix + key] = pandas.Series([item.get(key, None) if item else dict() for item in data])

    return df
