import os

def delete_DS_store(input_path):
    #input_folder_path = ('input/')
    #input_folder_path_list = os.listdir(input_folder_path)
    #output_file_name = input_folder_path_list[0]

    #test = input_folder_path + output_file_name + '/'

    contains = os.listdir(input_path)

    for filename in contains:
        print(filename)
        x = filename.split('.')
        if len(x) >  1:
            y = x[1].strip()
            print(y)
            if y.lower() == 'ds_store':
                print(filename)
                file_to_delete = os.path.join(input_path, filename)
                os.remove(file_to_delete)