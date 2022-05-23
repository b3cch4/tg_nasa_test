import os

for filename in os.listdir("images/apod"):
   with open(os.path.join("images/apod", filename), 'r') as f:
       print(f.name)