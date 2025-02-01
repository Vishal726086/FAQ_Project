# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the FAQ Project")

class FAQViewSet(viewsets.ViewSet):
    def list(self, request):
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        data = [{
            'id': faq.id,
            'question': faq.translate(lang),
            'answer': faq.answer,
        } for faq in faqs]
        return Response(data)