import os
import re

def check_files(pathname, old, new):
    for root, dirs, files in os.walk(pathname):
        if len(files) > 0:
            for file in files:
                if not 'pyc' in file:
                    with open(root + "/" + file, 'w') as f:
                        content = f.read()
                    if old in content:
                        print(f'{old} found in {file} with {content.count(old)} occurances.')
                        content.replace(old, new)
            


check_files(".", "vitruvius", "nimbus")