# Final Python Project Word editor
# Sparsh Gosalia
# Date: 2024-04-11
# File Picker

import os
'''
def isTextFile(filePath):
    
    # Check if a file is a text file based on its extension.
    textExtensions = ['.txt', '.csv', '.py', '.html', '.xml']  # Add more text file extensions if needed
    _, fileExtension = os.path.splitext(filePath)
    return fileExtension.lower() in textExtensions
'''

def listTextFiles(directory):
    
    # List all text files in a given directory.
    textFiles = []
    for filename in os.listdir(directory):
        filePath = os.path.join(directory, filename)
        if os.path.isfile(filePath):
            textFiles.append(filePath)
            print(textFiles)
    return textFiles

def selectOperationalFile(directory):
    
    # Select a text file from a given directory.
    textFiles = listTextFiles(directory)
    if textFiles:
        return textFiles[0]  # Return the first text file found
    else:
        return None

username = "jack" #used for testing
listTextFiles(f"user-Docs\\{username}") #used for testing 
############
# How this code can be used with the complete code 
############
    
# directory = input("Enter the directory path: ")
# operationalFile = selectOperationalFile(directory)
# if operationalFile:
#     print(f"Operational file selected: {operationalFile}")
# else:
#     print("No text file found in the directory.")
