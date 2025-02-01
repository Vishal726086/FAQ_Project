# Create your models here.
'''from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def translate(self, lang='en'):
        cache_key = f'faq_{self.id}_{lang}'
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation
        
        translator = Translator()
        translation = translator.translate(self.question, dest=lang).text
        cache.set(cache_key, translation, timeout=86400)
        return translation

    def __str__(self):
        return self.question'''


from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator
from asgiref.sync import async_to_sync  # For using async method in sync code

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    async def translate_async(self, lang='en'):
        cache_key = f'faq_{self.id}_{lang}'
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation
        
        translator = Translator()
        translation = await translator.translate(self.question, dest=lang)  # Await the async translation
        cache.set(cache_key, translation.text, timeout=86400)
        return translation.text

    def translate(self, lang='en'):
        # If you need to keep this method synchronous
        return async_to_sync(self.translate_async)(lang)

    def __str__(self):
        return self.question

