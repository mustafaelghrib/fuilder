"""A module that contains the index view of the api url."""

from django.http import HttpResponse, HttpRequest


def index_view(request: HttpRequest) -> HttpResponse:
    """Show index view for the root url of the api.

    Args:
        request: the http request

    Returns:
        A welcome message in http response

    """
    return HttpResponse(f"<h1>Welcome Users Service</h1>")
