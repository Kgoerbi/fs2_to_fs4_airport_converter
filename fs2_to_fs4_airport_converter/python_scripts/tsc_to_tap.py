import re

#copy/paste  general information from .tsc to .tap
def cp_general_information(file_input, file_output):
    
    example = r"\[.*?\]\s*\[.*?\]\s*\[(.*?)\]"
    
    #tab_batch_code =    '        <[string8]          [batch_code]        []>'
    #tab_tags =          '        <[uint32]           [tags]              []>'
    #tab_priority =      '        <[uint32]           [priority]          []>'
    #tab_connections =   '        <[uint16]           [connections]       []>'
    #tab_time_zone =     '        <[int8]             [time_zone]         []>'
    #tab_iata =          '        <[stringt8c]        [iata]              []>'
    #tab_tower_heading = '        <[float64]          [tower_heading]     []>'
    tab_view_height =   '        <[float64][tower_view_height][]>'
    tab_elevation =     '        <[float64][elevation][]>'
    tab_icao =          '        <[stringt8c][icao][]>'
    tab_name =          '        <[string8][name][]>'
    tab_name_short =    '        <[string8][name_short][]>'
    tab_country =       '        <[stringt8c][country][]>'
    tab_model_center =  '        <[vector2_float64][model_center][]>'
    tab_tower_position ='        <[vector2_float64][tower_position][]>'
    tab_tower_height =  '        <[float64][tower_height][]>'
    
        
    with open(file_input, 'r') as input_file:
        
        tp_line_object = input_file.readlines()
        
                #tab_icao
        tp_line  = ''.join(tp_line_object[10])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_icao)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_icao,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
       
                #tab_name
        tp_line  = ''.join(tp_line_object[9])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_name)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_name,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
        
                #tab_name_short
        tp_line  = ''.join(tp_line_object[8])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_name_short)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_name_short,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
        
                #tab_country
        tp_line  = ''.join(tp_line_object[11])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_country)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_country,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
            
                #tab_elevation
        tp_line  = ''.join(tp_line_object[13])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_elevation)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_elevation,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
            
                #tab_model_center
        tp_line  = ''.join(tp_line_object[12])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_model_center)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_model_center,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
            
                #tab_tower_position
        tp_line  = ''.join(tp_line_object[15])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_tower_position)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_tower_position,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
            
                #tab_tower_height
        tp_line  = ''.join(tp_line_object[16])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_tower_height)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_tower_height,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
            
                #tab_view_height
        tp_line  = ''.join(tp_line_object[16])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_view_height)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_view_height,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
        
            
        output_file.close()
        input_file.close()


def convert_xref(xref_file, tap_file):
    with open(xref_file, 'r') as source:
        xref_content = source.readlines()
    
    line = 0
    while line < 361:
        
        with open('files/fs2_xref_flow32_direction.txt', 'r') as file2:
            search_files = file2.readlines()
    
        with open('files/fs4_xref_flow64_direction.txt', 'r') as file3:
            replace_files = file3.readlines()
            
        x = search_files[line]
        y = replace_files[line]

        xref_content = [item.replace(x,y) for item in xref_content]

        line = line + 1
    
        
    extracted_xref = ''.join(xref_content[14:-3])
    
    new_xref = extracted_xref.replace('[vector3_float64]','[vector2_float64]').lower()
        
    with open(tap_file, 'r') as output_file:
        tap_content = output_file.readlines()
        
    tap_content.insert(56, new_xref)
    
    with open(tap_file, 'w') as output_file:
        output_file.writelines(tap_content)


def convert_boundaries(lon, lat, tap_file):
    second_line = '                <[list_vector2_float64][points][(' +  str(lon + 0.04) + ' ' + str(lat + 0.02)  +  ') (' +  str(lon + 0.04) + ' ' + str(lat - 0.02)  +  ') (' +  str(lon - 0.04) + ' ' + str(lat - 0.02)  +  ') (' +  str(lon - 0.04) + ' ' + str(lat + 0.02)  +  ') (' +  str(lon + 0.04) + ' ' + str(lat + 0.02)  +  ')  ]>'
    
    with open(tap_file, 'r') as file:
        old_content = file.readlines()
        
    old_content.insert(51, second_line)
    
    with open(tap_file, 'w') as file:
        file.writelines(old_content)
    
