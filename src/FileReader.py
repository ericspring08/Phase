def open_file(filename):
    file_contents = ""
    with open(filename) as f:
        line = f.readline()
        if len(line) > 0 and line[0] != "#":
            file_contents += line
    
    return file_contents