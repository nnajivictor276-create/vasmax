from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to Vintech application!")

def card_detail(request, slug, plan):
    return HttpResponse(f"Card {slug} - {plan}")

def register_view(request):
    return HttpResponse("Register page")

def login_view(request):
    return HttpResponse("Login page")

def logout_view(request):
    return HttpResponse("Logout")

def dashboard_view(request):
    return HttpResponse("Dashboard")

def success_page(request):
    return HttpResponse("Success")

def activate_membership_api(request):
    return HttpResponse("Activate API")