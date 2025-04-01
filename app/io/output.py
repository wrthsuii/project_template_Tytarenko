import pandas as pd

def output_from_console(text):
    """
    Prints the given text to the console.
    :param text(str): The text to be displayed.
    :return: None
    """
    print(text)

def write_file(file_path, content):
    """
    Writes the provided text content to a file.
    :param file_path(str): The path to the file.
    :param content(str): The text content to be written to the file.
    :return: None
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def write_file_pandas(file_path, data):
    """
    Writes data to a CSV file using the Pandas library.
    :param file_path(str): The path to the CSV file.
    :param data(list[dict] | pd.DataFrame): The data to be converted into a DataFrame and saved.
    :return: None
    """
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding='utf-8')