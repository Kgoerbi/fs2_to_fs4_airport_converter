import os
import tsc_to_tap
import get_lon_lat
import delete

output_folder_path = ('../output/')
input_folder_path = ('../input/')
input_folder_path_list = os.listdir(input_folder_path)
output_file_name = input_folder_path_list[0]

delete.delete_DS_store(input_folder_path + output_file_name + '/')

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
tsc_to_tap.convert_xref(input_toc_path,output_folder_path + output_file_name + '.tap')
tsc_to_tap.convert_boundaries(lon,lat,output_folder_path + output_file_name + '.tap')
