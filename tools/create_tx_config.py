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
        if not entered: break
        return entered

# Ask for values for common variables.
default = "https://www.transifex.com"
host = ask("What Transifex URL do you use? (https://www.transifex.com) :", default)
print("Thanks, Let's use " + host + " for the host.")

default = "en"
lang = raw_input("What is the source language? (en) : ")
if not lang:
	lang = default
print ("OK! Source language:" + lang)

while 
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

f = open(".tx/config",'w')
f.writelines("[main]\nhost = " + host +"\n\n")

if os.path.isdir(strings_path):
	for dirpath, dirname, filenames in os.walk(strings_path):
		for f in filenames:
			if f.endswith(".strings"):
				source_strings = os.path.join(dirpath,f)
				filename = f
				lang_path = dirpath.replace("en.lproj","<lang>.lproj")
				lang_strings = os.path.join(lang_path,f)
                resource_slug = filename.replace(".strings","strings")
			
			form = """\n[%s.%s]\nfile_filter = %s\nsource_file = %s\nsource_lang = %s\ntype = PO\n""" % (project_slug, resource_slug, f, pot, lang)

			f.writelines(form)
	
print ("Transifex config file written.  Please verify output in .tx/config.")
exit()
