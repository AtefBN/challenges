import os, sys, datetime
from mutagen.mp3 import MP3

# Fetching the directory to compute duration
directory = sys.argv[-1]

# Testing said directory exists
if not os.path.isdir(directory):
    print('This directory {} does not seem to exist in the system.')
    sys.exit(1)

# Listing directory contents
contents = os.listdir(directory)

# Retrieving mp3 files
sum_duration = 0
for file in contents:
    if file.endswith('.MP3'):
        audio = MP3(os.path.join(directory, file))
        sum_duration += audio.info.length
        print file + ' ' + str(datetime.timedelta(0, audio.info.length))
print '___________________________________'
print('Total:                  '+str(datetime.timedelta(0, sum_duration)))



