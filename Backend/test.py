import os
if os.path.exists('credentials.json'):
    print("File exists!")
else:
    print("File does not exist!")