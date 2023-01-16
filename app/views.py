from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app.services.check_file_service import extract_header_upload, extract_header_url, find_matches, validate_url
from django.db.models.functions import Length
from app.services.rss_service import get_feed
from .models import Signatures

# Create your views here.


def app(request: HttpRequest) -> HttpResponse:

    file_type = ""
    header = ""
    signatures = (
        Signatures.objects.all().order_by(Length("hex_signature").desc())
    ) 
    if request.method == "POST":
        if request.POST["input_type"] == "file" and request.FILES.get("file"):
            # A file was uploaded
            header = extract_header_upload(request.FILES.get("file"))
        elif request.POST["input_type"] == "url" and request.POST["url"]:
            # A URL was provided
            if validate_url():
                header = extract_header_url(request.POST["url"])
            else:
                header = "Url not valid!"
        file_type = find_matches(string_list=signatures, target_string=header)

    
    return render(
        request,
        "index.html",
        {"file_type": file_type, "feed": get_feed()},
    )
