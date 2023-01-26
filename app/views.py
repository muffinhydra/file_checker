from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app.models import FileSignatures
import os
from urllib.parse import urlparse
from app.services.check_file_service import (
    extract_header_upload,
    extract_header_url,
    find_matches,
    validate_url,
)
from django.db.models.functions import Length
from app.services.rss_service import get_feed


def app(request: HttpRequest) -> HttpResponse:
    is_legitimate = True
    file_type = ""
    header = ""
    given_type = ""
    path = ""
    error_message = ""
    signatures = FileSignatures.objects.all().order_by(Length("header").desc())
    if request.method == "POST":

        if request.POST["input_type"] == "file" and request.FILES.get("file"):
            # A file was uploaded
            header = extract_header_upload(request.FILES.get("file"))
            path: str = request.FILES.get("file").name

        elif request.POST["input_type"] == "url" and request.POST["url"]:
            # A URL was provided
            if validate_url(request.POST["url"]):
                header = extract_header_url(request.POST["url"])
                path: str = urlparse(request.POST["url"]).path
            else:
                error_message = "Url not valid!"

        if error_message == "":
            file_type = find_matches(string_list=signatures, target_string=header)
            given_type = os.path.splitext(path)[1][1:].upper()

            if any(given_type in file.extension for file in file_type):
                is_legitimate = True
            else:
                is_legitimate = False

    return render(
        request,
        "index.html",
        {
            "error_message": error_message,
            "file_type": file_type,
            "feed": get_feed(),
            "given_type": given_type,
            "is_legitimate": is_legitimate,
        },
    )
