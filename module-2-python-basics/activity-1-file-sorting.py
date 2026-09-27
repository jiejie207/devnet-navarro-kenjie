"""
Module 2 — Activity: File Sorting with os and shutil
Student: Navarro, Kenjie Mariel A
Date: 9/27/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
The only thing i build is a script that checks if a kind of files exist in my current folder.
for example, if i have a .jpg file, it will print "the file exists!", and if i don't have a .jpg file,
it will print "the file does not exist.".


============================================
KEY VOCABULARY
============================================
- os module: tools for using files, creating directories, and listing files.
- shutil module: tools for copying and removing files.
- file path: location of the file in the computer.
- directory: another term for folder.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

Files_Types = [".jpg, .png, .pdf, .txt, .pptx, .mp4, .zip"]

for file in os.listdir():
    if file.endswith(tuple(Files_Types)):
        print("The file exists!")
        break
    else:
        print("The file does not exist.")



"""
A MISTAKE I MADE (or one I want to avoid)
============================================
At first, I thought that my code will work perfectly, because theres no red lines, 
but when I run it, the Terminal print "TypeError: endswith first arg must be str or a tuple of str, not list"
then i just out tuple on before the (Files_types) and it works.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
