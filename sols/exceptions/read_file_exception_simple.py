#!/usr/bin/env python3

while True:
    filename = input('Enter the file name: ')
    try:
        f = open(filename, 'r')
        print('...reading: ', filename)
        contentlines = f.readlines()
        print('The file has: ', len(contentlines))
    except OSError:
        print("...File does not exist...:", filename, "...")

    resp = input("Continue (Y/n)?")
    if resp.lower() == 'n':
        break