from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to VASMAX School Checker SaaS</h1><p>Go to /VAZY/check/ to test</p>")