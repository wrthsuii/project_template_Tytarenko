import os
from app.io.input import input_from_console, read_file, read_file_pandas
from app.io.output import write_file

def main():
    file_path1 = os.path.join('app', 'data', 'ValentinesDay.txt')
    file_path2 = os.path.join('app', 'data', 'example.csv')
    output_file_path = os.path.join("app", "data", "output.txt")
    user_input = input_from_console()
    content_file = read_file(file_path1)
    content_file_pandas = read_file_pandas(file_path2)

    output_text = f"User input: {user_input}\n\n"
    output_text += f"Content of {file_path1}:\n{content_file}\n\n"
    output_text += f"Content of {file_path2}:\n{content_file_pandas}\n"

    print(output_text)

    write_file(output_file_path, output_text)

if __name__ == '__main__':
    main()
