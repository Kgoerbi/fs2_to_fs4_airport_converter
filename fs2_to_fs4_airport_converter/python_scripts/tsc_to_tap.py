import re

def append_string_to_line(file_path, line_number, append_string):
    with open(file_path, 'r') as file:
        lines = file.readlines()


    lines[line_number - 1] = lines[line_number - 1].rstrip() + append_string

    with open(file_path, 'w') as file:
        file.writelines(lines)


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
        
                #tap_icao
        tp_line  = ''.join(tp_line_object[10])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_icao)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_icao,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
       
                #tap_name
        tp_line  = ''.join(tp_line_object[9])
        ergebnis = re.search(example, tp_line)
        new_content = re.sub(r"\[\s*\]", f"[{ergebnis.group(1)}]", tab_name)
        
        with open(file_output, 'r' ) as output_file:
            new_tab = output_file.read().replace(tab_name,new_content)

        with open(file_output, 'w') as file:
            file.write(new_tab)
            file.close()
        
                #tap_name_short
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
        target.insert(a, '            <[tm_airport_pd_helipad][element]['+str(x)+']\n')
        a += 1
        target.insert(a,'')
        target.insert(a, '                <[vector2_float64][position]'+str(helipad_position[x]))
        a += 1
        target.insert(a,'')
        target.insert(a, '                <[float64][direction]'+str(helipad_direction[x]))
        a += 1
        target.insert(a,'')
        target.insert(a, '                <[float64][radius]'+str(helipad_radius[x]))
        a += 1
        target.insert(a,'')
        target.insert(a, '                <[string8][name]['+ str(x + 1) + ']>\n            >\n')
        # a += 1
        # target.insert(a,'')
        # target.insert(a, '            >\n            >\n')

        x+=1
    
    with open(file_output, 'w') as file:
        file.writelines(target)
        file.close()

def  convert_runway_pairs(file_input, file_output):
    
    runway_line = []
    
    with open(file_input, 'r') as file:
        
        source = file.readlines()
        
        #get line numbers of runway_pairs
        line_number = 0
        for line in source:
            number = 0
            while number < 250:
                if line.strip() == '<[tmsimulator_runway][element][' + str(number) + ']':
                    runway_line.append(line_number)
                number += 1
            line_number += 1
        file.close()
        
        
    threshold_1 = []
    threshold_2 = []
    identifier_1 = []
    identifier_2 = []
    appltsys_1 = []
    appltsys_2 = []
    reil_1 = []
    reil_2 = []
    papi_1 = []
    papi_2 = []
    direction_1 = []
    direction_2 = []
    width = []
        
    for line in runway_line:
        a = source[line+3]
        threshold_1.append(a[31:])
        a = source[line+4]
        threshold_2.append(a[31:])
        a = source[line+6]
        #a2= a[]
        identifier_1.append(a[23:])
        a = source[line+7]
        identifier_2.append(a[23:])
        a = source[line+8]
        appltsys_1.append(a[28:])
        a = source[line+9]
        appltsys_2.append(a[28:])
        a = source[line+12]
        reil_1.append(a[24:])
        a = source[line+13]
        reil_2.append(a[24:])
        a = source[line+10]
        papi_1.append(a[24:])
        a = source[line+11]
        papi_2.append(a[24:])
        #a = source[line+]
        #direction_1.append(a[:])
        #a = source[line+]
        #direction_2.append(a[:])
        a = source[line+5]
        width.append(a[23:])
    
    
    with open(file_output, 'r') as file:
        target = file.readlines()
        file.close()
        
    with open('../files/runway_pairs-template.txt', 'r') as file:
        template = file.readlines()
        file.close()
    
    
    number = 0
    while number < len(runway_line):
        number2 = 44
        while number2 > 0:
            #target.insert(5,'\n')
            target.insert(42, template[number2])
            number2 -= 1
            
        #target.insert(5,'\n')
        number+=1
    
    with open(file_output, 'w') as file:
        file.writelines(target)
        file.close()
    
    number = 0
    while number < len(runway_line):
        x = 43 + number * 45
        append_string_to_line(file_output, x, str(number) + ']\n')
        y = x + 3
        append_string_to_line(file_output, y, threshold_1[number])
        y = x + 5
        append_string_to_line(file_output, y, identifier_1[number])
        y = x + 6
        append_string_to_line(file_output, y, appltsys_1[number])
        y = x + 7
        append_string_to_line(file_output, y, reil_1[number])
        y = x + 8
        append_string_to_line(file_output, y, papi_1[number])
        #y = x + 4
        #append_string_to_line(file_output, y, direction_1[number])

        y = x + 21
        append_string_to_line(file_output, y, threshold_2[number])
        y = x + 23
        append_string_to_line(file_output, y, identifier_2[number])
        y = x + 24
        append_string_to_line(file_output, y, appltsys_2[number])
        y = x + 25
        append_string_to_line(file_output, y, reil_2[number])
        y = x + 26
        append_string_to_line(file_output, y, papi_2[number])
        #y = x + 4
        #append_string_to_line(file_output, y, direction_1[number])
        
        y = x + 39
        append_string_to_line(file_output, y, width[number] + '\n>')

        
        number += 1
    



#convert_runway_pairs('../input/KNKX/KNKX.tsc', '../output/KNKX.tap')

def convert_parking_positions(file_input,  file_output):
    
    pp_line = []
    
    with open(file_input, 'r') as file:
        source = file.readlines()
        
        #get line numbers of parking_positions
        line_number = 0
        for line in source:
            number = 0
            while number < 250:
                if line.strip() == '<[tmsimulator_parking_position][element][' + str(number) + ']':
                    pp_line.append(line_number)
                number += 1
            line_number += 1
        file.close()
    
    
    pp_position = []
    pp_direction = []
    pp_name = [] 
    
    #collecting general Data
    for line in pp_line:
        a = source[line + 1]
        pp_position.append(a[28:])
        b = source[line + 2]
        pp_direction.append(b[24:])
        d = source[line + 3]
        pp_name.append(d[21:])
    
    with open(file_output, 'r') as file:
        target = file.readlines()
        file.close()
    
    
    x = 0
    while x < len(pp_line):
        y = x * 6
        a = 39 + y
        target.insert(a,'')
        target.insert(a, '            <[tm_airport_pd_parking_position][element]['+str(x)+']\n')
        a += 1
        target.insert(a,'')
        target.insert(a, '                <[vector2_float64][position]'+str(pp_position[x]))
        a += 1
        target.insert(a,'')
        target.insert(a, '                <[float64][direction]'+str(pp_direction[x]))
        a += 1
        target.insert(a,'')
        target.insert(a, '                <[float64][radius][40]>\n')
        a += 1
        target.insert(a,'')
        target.insert(a, '                <[string8][name]'+ str(pp_name[x]))
        a += 1
        target.insert(a,'')
        target.insert(a, '                <[float64][type][parked_jet]>\n            >\n')

        x+=1
    
    with open(file_output, 'w') as file:
        file.writelines(target)
        file.close()
