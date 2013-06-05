#!/usr/bin/env python
#
# Copyright (C) 2013 Transifex
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
# associated documentation files (the "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the
# following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import os
import string

def ask(question, default=""):
    entered = default
    while True:
        entered = raw_input(question)
        if entered:
            break
        elif default:
            return default
    return entered

# Ask for values for common variables.
host = ask("What Transifex URL do you use? (https://www.transifex.com) :", "https://www.transifex.com")
print("Thanks, Let's use " + host + " for the host.")

source_lang = ask("What is the source language? (en) : ", "en")
print ("OK! Source language:" + source_lang)

 
project_slug = ask("Enter your project id on Transifex. This is the last path component in the project URL on Transifex: ")
print("Okay, using " + project_slug + " for this instance.")

# Search in path for files with a .strings suffix and provide a relative path and file name.
txconfig = ".tx/config"
if os.path.isfile(txconfig):
    print("Found an existing Transifex config file. Good to go.")
else:
    print("There is no Transifex config file. Please run tx init first to create one.")
    exit()


strings_path = "./"
resource_format = """
[%s.%s]
file_filter = %s
source_file = %s
source_lang = %s
"""

source_dir = "%s.lproj" % (source_lang)

config_file = open(".tx/config",'w')
config_file.writelines("[main]\nhost = " + host +"\n\n")

if os.path.isdir(strings_path):
    for dirpath, dirname, filenames in os.walk(strings_path):
        for filename in filenames:
            source_strings = ""
            lang_path = ""
            lang_strings = ""
            resource_slug = ""
            resource = ""
            if filename.endswith(".strings") and source_dir in dirpath :
                source_strings = os.path.join(dirpath, filename)
                lang_path = dirpath.replace(source_dir, "<lang>.lproj")
                lang_strings = os.path.join(lang_path, filename)
                resource_slug = filename.replace(".strings", "strings")		
                resource = resource_format % (project_slug, resource_slug, lang_strings, source_strings, source_lang)
                config_file.writelines(resource)

print ("Transifex config file written.  Please verify output in .tx/config.")
exit()
