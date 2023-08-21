import os
import tsc_to_tap
import toc_to_tap
import get_lon_lat


def remove_tabs(file):
    with open(file, 'r') as file1:
        a = file1.readlines()
        file1.close()
    
    with open(file, 'w') as file2:
        b = [item.replace('	', '    ') for item in a]
        file2.writelines(b)
        file2.close()


output_folder_path = ('../output/')
input_folder_path = ('../input/')
input_folder_path_list = os.listdir(input_folder_path)

for file in input_folder_path_list:
    if len(file) == 4 or len(file) == 6:
        output_file_name = file
    
        try:
            x = ('.DS_Store')
            y = os.path.join(input_folder_path, x)

            os.remove(y)
        except Exception as e:
            print(e)

        input_tsc_path = input_folder_path + output_file_name + '/' + output_file_name + '.tsc'



        input_toc_path = input_folder_path + output_file_name + '/' + output_file_name + '.toc'

        lon = float(get_lon_lat.get_lon(input_tsc_path))
        lat = float(get_lon_lat.get_lat(input_tsc_path))


        with open('../files/tap-file_template.tap','r') as tap_file_template:          #get template
            tap_template = tap_file_template.read()
            tap_file_template.close()

        with open(output_folder_path + output_file_name + '.tap', 'w+') as output_file:      #create .tap-file
            
            output_file.write(tap_template)
            output_file.close()

            tsc_to_tap.cp_general_information(input_tsc_path, output_folder_path + output_file_name + '.tap')
            toc_to_tap.convert_xref(input_toc_path,output_folder_path + output_file_name + '.tap')
            tsc_to_tap.convert_boundaries(lon,lat,output_folder_path + output_file_name + '.tap')
            tsc_to_tap.convert_helipads(input_tsc_path,output_folder_path + output_file_name + '.tap')
            tsc_to_tap.convert_runway_pairs(input_tsc_path,output_folder_path + output_file_name + '.tap')
            tsc_to_tap.convert_parking_positions(input_tsc_path,output_folder_path + output_file_name + '.tap')
            
            remove_tabs(output_folder_path + output_file_name + '.tap')
