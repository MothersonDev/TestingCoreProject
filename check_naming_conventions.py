import os
import re

def check_naming_conventions():
    pattern = r'^[A-Z][a-zA-Z0-9]*$'  # Customize this regex pattern for your naming conventions

    for root, dirs, files in os.walk("."):
        for file in files: 
            if file.endswith(".cs"):
               from pathlib import Path    
               nm= Path(file).name
               if nm.length <10:
                print("File name of c# file should be greater than 10 chars")
                raise Exception("File name of c# file should be greater than 10 chars")
                      
                      
                      
    if (__name__ == "__main__"): 
       check_naming_conventions() 
    #             with open(os.path.join(root, file), "r") as f:
    #                 for line_number, line in enumerate(f, 1):
    #                     variables = re.findall(r'\b[A-Za-z_]\w*\b', line)
    #                     for variable in variables:
    #                         if not re.match(pattern, variable):
    #                             print(f"Error in {file}: Line {line_number}: Invalid variable name '{variable}'")

