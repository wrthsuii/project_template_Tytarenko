import pandas as pd

def input_from_console():
    """
    Prompts the user for input and returns the entered text.
    :return(str): The user input
    """
    user_input = input('Enter sth here: ')
    return user_input

def read_file(file_path):
    """
    Reads the content of a text file.
    :param file_path(str): The path to the file.
    :return(str): The file content if successful, or an error message if the file is not found.
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return 'File not found'

def read_file_pandas(file_path):
    """
    Reads a CSV file into a Pandas DataFrame.
    :param file_path(str): The path to the CSV file.
    :return(pd.DataFrame | str): The DataFrame if successful, or an error message in case of failure.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        return 'File not found'
    except pd.errors.EmptyDataError:
        return 'File is empty'
    except Exception as e:
        return f'Error: {e}'
