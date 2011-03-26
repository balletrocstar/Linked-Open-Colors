
import os

def get_mapping_dbpedia_color(color):
    path = os.path.join(os.path.dirname(__file__), "..", "data", "mappings_dbpedia_colors.txt")
    mappings = eval(open(path).read()) #FIXME: singleton or borg pattern
    if (color in mappings):
        return mappings[color]
    else:
        return None

