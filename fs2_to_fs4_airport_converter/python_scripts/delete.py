import os

def delete_DS_store(input_path):

    contains = os.listdir(input_path)

    for filename in contains:
        print(filename)
        x = filename.split('.')
        if len(x) >  1:
            y = x[1].strip()
            if y.lower() == 'ds_store':
                file_to_delete = os.path.join(input_path, filename)
                os.remove(file_to_delete)
