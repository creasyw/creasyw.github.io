import os
import sys
import subprocess

keywords = {"<div class=\'post\'>": "",
            "<br/>": "\n",
            "<br />": "\n",
            "&nbsp;": "";
            "</div>": ""}


full_path = sys.argv[1]
if full_path is None:
    print("Error! The correct form is:\n$ python3 script path_of_the_folder")
# Transfer bytes into string and remove the first 2 characters, then split it into files
# only search the 1st level
files = str(subprocess.check_output(("ls", full_path)))[2:].split('\\n')

# Left only html files
for file in filter(lambda x: ".html" in x, files):
    print("Processing the file -- {}".format(file))
    with open(os.path.join(full_path, file), 'r') as file_handle:
        contents = file_handle.read()
    for keyword in keywords:
        contents = contents.replace(keyword, keywords[keyword])
    save_to_file = file.replace(".html", ".md")
    print("Save to the file --  {}".format(save_to_file)) 
    with open(os.path.join(full_path, save_to_file), 'w') as file_handle:
        file_handle.write(contents)
    # clean up
    os.remove(os.path.join(full_path, file))
