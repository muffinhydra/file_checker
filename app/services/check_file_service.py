from multiprocessing.managers import BaseManager
from django.core.files.uploadedfile import UploadedFile
from typing import List, Set
import requests
from app.models import FileSignatures


def validate_url(url: str) -> bool:
    """
    Validate the given URL for download.

    This function takes in a single parameter, url, which is a string representing the URL to be validated.
    It sends a HEAD request to the URL and checks the value of the 'content-type' header in the response.
    If the header value contains the sub-string 'text' or 'html', the function returns False indicating the URL is not valid.
    Otherwise, it returns True indicating the URL is valid.

    Args:
    url: str: The URL to be validated.

    Returns:
    bool: True if the URL is valid, False otherwise.
    """
    h: requests.Response = requests.get(url, allow_redirects=True)
    content_type = h.headers.get("content-type")
    print(h)

    if "text" in content_type.lower():
        return False
    if "html" in content_type.lower():
        return False
    return True


def extract_header_upload(uploaded_file: UploadedFile) -> str:
    """
    Extracts and formats the header of the given uploaded file.

    This function takes in a single parameter, uploaded_file, which is an instance of the `UploadedFile` class.
    It seeks to the beginning of the file and reads the first 64 bytes of the file, which is considered as the file's header.
    Then it formats the header as a string of 2-digit hexadecimal values separated by a space and returns it in uppercase.

    Args:
    uploaded_file: UploadedFile: The uploaded file to extract the header from.

    Returns:
    str: The formatted header of the file in uppercase
    """
    uploaded_file.seek(0)
    header = uploaded_file.read(64)
    # The "{:02x}" is a format specifier that formats an integer as a 2-digit hexadecimal number with leading zero.
    formatted_hex_header = " ".join("{:02x}".format(b) for b in header)
    return formatted_hex_header.upper()


def extract_header_url(url: str) -> str:
    """
    Extracts and formats the header of a file located at the given URL.

    This function takes in a single parameter, url, which is a string representing the URL of the file to extract the header from.
    It sends a GET request to the URL using the `requests` library and reads the first 200 bytes of the response content,
    which is considered as the file's header. Then it formats the header as a string of 2-digit hexadecimal values separated by a space
    and returns it in uppercase.

    Args:
    url: str: The URL of the file to extract the header from.

    Returns:
    str: The formatted header of the file in uppercase
    """
    formatted_hex_header: str = ""
    response: requests.Response = requests.get(url, allow_redirects=True)
    header = response.content[:400]
    # The "{:02x}" is a format specifier that formats an integer as a 2-digit hexadecimal number with leading zero.
    formatted_hex_header: str = " ".join("{:02x}".format(b) for b in header)
    return formatted_hex_header.upper()


def find_matches(
    string_list: Set[FileSignatures], target_string: str
) -> List[FileSignatures]:
    """
    Finds matches in the given list of FileSignatures based on the target_string.

    Args:
        string_list (Set[FileSignatures]): a set of FileSignatures objects
        target_string (str): the target string to match against the headers of the FileSignatures objects

    Returns:
        List[FileSignatures]: a list of FileSignatures objects that matched the target_string
    """
    matches = []
    for s in string_list:
        if target_string.startswith(s.header):
            matches.append(s)

    return matches


if __name__ == "__main__":
    pass
