from sys import argv
from os.path import exists

script, from_file, to_file = argv

infile = open(from_file)
indata = infile.read()

print(f"Copying from {from_file} to {to_file}")
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")




