import os


file_names = set()

# iterate through file system
for root, dirs, files in os.walk('/home', topdown=True):
    # itereate through directories with name str
    for name in dirs:
        # While there is a space in the name, run this iteration.
        while ' ' in name:
            file_names.add(name)
            new_name = f"{root}/{name.replace(' ', '_')}"
            if os.path.isdir(f"{root}/{name}"):
                try:
                    os.rename(f"{root}/{name}", new_name)
                except:
                    print('error')

file_names_changed = len(file_names)
print(f"Renamed {file_names_changed} directories")