def convert_xref(xref_file, tap_file):
    with open(xref_file, 'r') as source:
        xref_content = source.readlines()
    
    line = 0
    while line < 361:
        
        with open('../files/fs2_xref_flow32_direction.txt', 'r') as file2:
            search_files = file2.readlines()
    
        with open('../files/fs4_xref_flow64_direction.txt', 'r') as file3:
            replace_files = file3.readlines()
            
        x = search_files[line]
        y = replace_files[line]

        xref_content = [item.replace(x,y) for item in xref_content]

        line = line + 1
    
        
    extracted_xref = '        '.join(xref_content[14:-3])
    
    new_xref = extracted_xref.replace('[vector3_float64]','[vector2_float64]').lower()
        
    with open(tap_file, 'r') as output_file:
        tap_content = output_file.readlines()
        
    tap_content.insert(52, new_xref)
    
    with open(tap_file, 'w') as output_file:
        output_file.writelines(tap_content)
