import os, re
from tqdm import tqdm


path = os.getcwd()
path = os.path.split(path)
path = os.path.join(path[0], 'Data')
os.chdir(path)

os.mkdir('raw')

pattern = re.compile(r'(\d{4}\-\d{2}\-\d{2})')

for file in tqdm(os.listdir()):
    if os.path.splitext(file)[1] in ('.gz', '.tar.gz'):
        name = re.findall(pattern, file)
        os.system(f"tar -xf {file} -C raw/")