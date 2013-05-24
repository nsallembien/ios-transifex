#!/bin/bash

ibtool Demo/Demo/Base.lproj/MainStoryboard.storyboard --generate-strings-file Demo/Demo/en.lproj/MainStoryboard.strings
tx push -s
