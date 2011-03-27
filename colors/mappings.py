
import os

def get_mapping_color(color, path):
    #FIXME: singleton or borg pattern
    mappings = eval(open(path).read()) 
    if (color in mappings):
        return mappings[color]
    else:
        return None

def get_mapping_dbpedia_color(color):
    path = os.path.join(os.path.dirname(__file__), "..", "data", "mappings_dbpedia_colors.txt")
    return get_mapping_color(color, path)

def get_mapping_css_color(color):
    path = os.path.join(os.path.dirname(__file__), "..", "data", "mappings_css_colors.txt")
    return get_mapping_color(color, path)

