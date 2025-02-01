from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse
from django.shortcuts import redirect
from faqs.views import home # import the new view

# Define a simple view for the root path
# def home(request):
    # return HttpResponse("Welcome to the FAQs API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('faqs.urls')),

    # path('', home, name='home'),  # Add this line for the root URL
    path('', lambda request: redirect('/api/')), #Redirect root to /api/
    path('', home), # Add this line to handle the root url
]
