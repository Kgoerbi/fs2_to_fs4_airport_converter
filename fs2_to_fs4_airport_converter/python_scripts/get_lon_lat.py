import re

def get_lon(source_file):
    
    example = r"\[.*?\]\s*\[.*?\]\s*\[(.*?)\]"
    
    with open(source_file, 'r') as source:
        source_lines = source.readlines()
        
        line = source_lines[12]
    
    x = re.search(example, line)
    y = x.group(1)
    z = y.index(' ')
    
    lon = y[:z]
    return(lon)

def get_lat(source_file):
    
    example = r"\[.*?\]\s*\[.*?\]\s*\[(.*?)\]"
    
    with open(source_file, 'r') as source:
        source_lines = source.readlines()
        
        line = source_lines[12]
    
    x = re.search(example, line)
    y = x.group(1)
    z = y.index(' ')
    
    lat = y[z+1:]
    return(lat)