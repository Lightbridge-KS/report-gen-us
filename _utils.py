def read_markdown(path):
    """
    Read a markdown file from a given file path and return the content as a string.

    Args:
    path (str): The file path to the markdown file.

    Returns:
    str: The content of the markdown file as a string.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "The file could not be found."
    except Exception as e:
        return f"An error occurred: {e}"

# Usage example:
# content = read_markdown('path_to_markdown.md')
# print(content)
