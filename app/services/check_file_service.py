from multiprocessing.managers import BaseManager
from django.core.files.uploadedfile import UploadedFile
import urllib.request
from typing import List, Set

from app.models import FileSignatures



def validate_url(url):
    # Send a HEAD request to the URL
    response = urllib.request.urlopen(url, method="HEAD")

    # Check the response status code
    if response.getcode() == 200:
        # URL is valid and file exists
        return True
    else:
        # URL is invalid or file does not exist
        return False

#TODO refactor extract_header_upload + extract_header_url, create maybe oop service?
def extract_header_upload(uploaded_file: UploadedFile) -> str:
    hex_header = ""
    header = uploaded_file.read(30)
    for b in header:
        hex_header = hex_header + b.to_bytes(1, "big").hex() + " "
    uploaded_file.seek(0)
    return hex_header.upper()

#TODO check for directory from URL 
def extract_header_url(url: str) -> str:

    hex_header = ""
    response = urllib.request.urlopen(url)
    file_contents = response.read()
    header = file_contents.read(30)
    for b in header:
        hex_header = hex_header + b.to_bytes(1, "big").hex() + " "
    return hex_header.upper()

#TODO implement edgecases example: 46 4F 52 4D ?? ?? ?? ?? 49 4C 42 4D, see models TODO
def find_matches(string_list: Set[FileSignatures], target_string: str) -> List[str]:
    matches = []
    for s in string_list:
        if target_string.startswith(s.header):
            matches.append(s)
    return matches

if __name__ == "__main__":
    pass
