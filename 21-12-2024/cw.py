txt_file = "lesson14.txt"

file = open(txt_file, "a", encoding="utf-8")

file.write("Hello world\n")

file.close()

def write_to_file(file_name: str, * str, mode: str = "a", encoding: str = "utf-8") -> None:
    with open(file_name, mode, encoding=encoding) as file:
        for line in txt_file:
        file.write(line + '\n'):  
