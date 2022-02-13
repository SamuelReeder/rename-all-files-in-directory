import os
import sys
path = sys.argv[1]
files = os.listdir(path)

try:
        name = sys.argv[2] + "_"
except IndexError:
        name = ""

for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([name + str(index), (file[file.index("."):])])))