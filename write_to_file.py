import json

# This script writes json data to a new file

"""
Args:
:data: 'dict or iterable data to save to file'
:filename: 'str' name of the file you will save
:option: 'str' 'send in either "w" for write or "a" for append to the file'
:multiline: 'bool' 'true if data needs to be iterated through with a new line'
"""
def write_to_file(data, filename, option="w", multiline=True)

OPTIONS = ["w", "a"]
# if an incorrect input is given
if option.lower() not in OPTIONS:
		print(f"Writing Method of {method} not valid. Defaulting to `{DEFAULT_METHOD}")
		method = DEFAULT_METHOD