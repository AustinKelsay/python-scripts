import os


file_names = set()

# iterate through file system
for root, dirs, files in os.walk('/home', topdown=True):
    # itereate through directories with name str
    for name in dirs:
        # While there is a space in the name, run this iteration.
        while ' ' in name:
            file_names.add(name)
            print('This is where we need renaming permission')

file_names_changed = len(file_names)
print(f"Renamed {file_names_changed} directories")