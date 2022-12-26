import os

file_path = "/Users/nike/Downloads"

for filename in os.listdir(file_path):
    file = os.path.join(file_path, filename)
    
    if os.path.isfile(file):
        print(file)
