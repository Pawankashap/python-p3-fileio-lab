def write_file(file_name='lib/logfile', file_content='Log 1: 5 bananas added'):
    with open(f"{file_name}.txt", 'w', encoding="utf-8") as file:
        file.write(file_content)

def append_file(file_name='lib/logfile', append_content="Log 2: 3 bananas subtracted"):
    with open(f"{file_name}.txt", 'a', encoding="utf-8") as file:
        file.write(append_content)

def read_file(file_name='lib/logfile'):
    with open(f"{file_name}.txt", encoding='utf-8') as file:
        return file.read()