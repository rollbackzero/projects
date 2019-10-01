import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()  

    if line:
        print_line(line, encoding, errors)  
        return main(language_file, encoding, errors)  

def print_line(line, encoding, errors):    
    next_lang = line.strip()  # strip trailing \n on the line string  
    raw_bytes = next_lang.encode(encoding, errors=errors)  # encode strings to bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)  # decode bytes to string

    print(raw_bytes, "<===>", cooked_string)  

languages = open("languages.txt", encoding="utf-8")   

main(languages, input_encoding, error)  
