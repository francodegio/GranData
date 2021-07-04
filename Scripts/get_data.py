import os


path = os.getcwd()
path = os.path.split(path)
path = os.path.join(path[0], 'Data')
os.chdir(path)

with open('links.txt', 'r') as f:
    data = f.read()

for _id in data.split('\n'):
    os.system(f"gdown --id {_id}")