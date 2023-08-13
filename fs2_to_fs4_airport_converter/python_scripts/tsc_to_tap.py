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

def convert_boundaries(lon, lat, tap_file):
    second_line = '                <[list_vector2_float64][points][(' +  str(lon + 0.04) + ' ' + str(lat + 0.02)  +  ') (' +  str(lon + 0.04) + ' ' + str(lat - 0.02)  +  ') (' +  str(lon - 0.04) + ' ' + str(lat - 0.02)  +  ') (' +  str(lon - 0.04) + ' ' + str(lat + 0.02)  +  ') (' +  str(lon + 0.04) + ' ' + str(lat + 0.02)  +  ')  ]>'
    
    with open(tap_file, 'r') as file:
        old_content = file.readlines()
        
    old_content.insert(51, second_line)
    
    with open(tap_file, 'w') as file:
        file.writelines(old_content)

def convert_helipads(file_input,  file_output):
    
    helipad_line = []
    
    with open(file_input, 'r') as file:
        source = file.readlines()
        
        #get line numbers of helipads
        line_number = 0
        for line in source:
            number = 0
            while number < 50:
                if line.strip() == '<[tmsimulator_helipad][element][' + str(number) + ']':
                    helipad_line.append(line_number)
                if line.strip() == '><[tmsimulator_helipad][element][' + str(number) + ']':
                    helipad_line.append(line_number)
                number += 1
            line_number += 1
        file.close()
    
    print(helipad_line)
    
    helipad_position = []
    helipad_direction = []
    helipad_radius =[] 
    helipad_name = [] 
    
    #collecting general Data
    for line in helipad_line:
        a = source[line + 3]
        helipad_position.append(a[28:])
        b = source[line + 5]
        helipad_direction.append(b[19:])
        c = source[line + 4]
        helipad_radius.append(c[18:])
        d = source[line + 1]
        helipad_name.append(d[16:])
    
    with open(file_output, 'r') as file:
        target = file.readlines()
        file.close()
    
    x = 0
    while x < len(helipad_line):
        y = x * 6
        a = 46 + y
        target.insert(a,'')
        target.insert(a, '<[tm_airport_pd_helipad][element]['+str(x)+']\n')
        a += 1
        target.insert(a,'')
        target.insert(a, '<[vector2_float64][position]'+str(helipad_position[x]))
        a += 1
        print(a)
        target.insert(a,'')
        target.insert(a, '<[float64][direction]'+str(helipad_direction[x]))
        a += 1
        print(a)
        target.insert(a,'')
        target.insert(a, '<[float64][radius]'+str(helipad_radius[x]))
        a += 1
        target.insert(a,'')
        target.insert(a, '<[string8][name]['+ str(x + 1) + ']>\n')
        a += 1
        target.insert(a,'')
        target.insert(a, '>\n')

        x+=1
    
    with open(file_output, 'w') as file:
        file.writelines(target)
        file.close()
