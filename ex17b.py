from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()   # open source file, read the contents and assign to object file

print(f'''Copying from {from_file} to {to_file}
The input file is {len(indata)} bytes long  
Copying..........
''')

out_file = open(to_file, 'w').write(indata)  # open dst file and copy contents of source file
  
print("Alright, all done")
