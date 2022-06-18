#!/usr/bin/env python3

#import os
from os import remove

from_file = "sample.txt"
to_file = "new.txt"

source = open(from_file).read()
target = open(to_file, 'w')
target.write(source)

target = open(to_file)
contents = target.read()
print(contents)
target.close()

remove(to_file)
