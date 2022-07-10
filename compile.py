# !/usr/bin/python

import os

for subdir, dirs, files in os.walk(".\learning"):
    for file in files:
        if os.path.splitext(file)[1] == '.ipynb':
            exe_command = 'jupyter nbconvert "{}" --to html --output-dir learning-html'.format(''.join(os.path.join(subdir, file)))
            # print(exe_command)
            os.system(exe_command)
        else:
            continue