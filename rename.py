import os
import datetime

# os.rename(r'file path\OLD file name.file type',r'file path\NEW file name.file type')

current_date = datetime.datetime.today().strftime ('%Y%m%dZ')
title = input("File title:   ")
correspondent = input("Correspondent:   ")
build_title = ("{} - {} - {}.txt".format(current_date,title,correspondent))
confirm = input("Are you sure you want to rename the file to {}?(y/n)  ".format(build_title))

if confirm.lower() == "y":
    os.rename(r'renamed.txt',build_title)
    print("File successfully renamed to {}".format(build_title))
else:
    print("Okay, bye now!")
