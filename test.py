import os, re

#path = re.match(r'images/\D/')

for filename in os.listdir(re.match(r'images/\D/')):
        with open(os.path.join(re.match(r'images/\D/'), filename), 'r') as f:
            print(f.name)