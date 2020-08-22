from django.template.response import TemplateResponse
from django.shortcuts import render


def hello(request):

    message = "Hello, world!"

    return TemplateResponse(
        request, "hello.html", {
            "message": message
        }
    )
