#!/usr/bin/python
# -*- coding: utf-8 -

import os
import csv

#Original source: http://www.w3schools.com/css/css_colornames.asp

def retrieve_mappings():
    mappings = {}
    path = path = os.path.join(os.path.dirname(__file__), "..", "data", "mappings_css_colors.csv")
    reader = csv.reader(open(path, "r"), delimiter=",", quotechar="\"")
    for row in reader:
        css = row[0][:-2]
        rgb = row[1][1:]
        mappings[css] = rgb

    return mappings


if __name__ == "__main__":
    mappings = retrieve_mappings()
    print mappings
