# Multilingual FAQ API (Django)

This project is a Multilingual FAQ API built using Django and Django REST Framework. It allows users to create, manage, and retrieve FAQs in multiple languages with support for a WYSIWYG editor, caching with Redis, and automatic translations.


🚀 Features

✅ Multilingual Support: FAQs can be stored and retrieved in multiple languages.

✅ WYSIWYG Editor: Uses django-ckeditor for rich text formatting.

✅ Fast API Responses: Uses Django's caching framework with Redis.

✅ Google Translate Integration: Auto-translates FAQs to different languages.

✅ RESTful API: Allows CRUD operations with language selection via ?lang= query parameter.

✅ Admin Panel: Provides a user-friendly UI for managing FAQs.

✅ Docker Support: Easily run the project using Docker.

✅ PEP8 Compliant: Code follows best practices and conventions.




🛠️ Installation

1️⃣ Clone the Repository

 git clone https://github.com/YOUR_USERNAME/multilingual-faq-api.git
 cd multilingual-faq-api

2️⃣ Create a Virtual Environment

 python -m venv env
 source env/bin/activate  # For Windows: env\Scripts\activate

3️⃣ Install Dependencies

 pip install -r requirements.txt

4️⃣ Set Up the Database

 python manage.py makemigrations
 python manage.py migrate

5️⃣ Create a Superuser

 python manage.py createsuperuser

6️⃣ Start the Server
 python manage.py runserver



🌍 API Endpoints

Fetch All FAQs (Default: English)

 GET /api/faqs/

Fetch FAQs in a Specific Language

 GET /api/faqs/?lang=hi  # Hindi
 GET /api/faqs/?lang=bn  # Bengali

Create a New FAQ

POST /api/faqs/
Content-Type: application/json
{
    "question": "What is Django?",
    "answer": "Django is a high-level Python Web framework...",
    "language": "en"
}

Update an FAQ

PUT /api/faqs/{id}/

Delete an FAQ

DELETE /api/faqs/{id}/




🗄️ Caching with Redis

Install Redis:

sudo apt install redis

Run Redis Server:

redis-server

Update ********settings.py:

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}



🐳 Running with Docker (Optional)

Build the Docker Image:
 docker build -t multilingual-faq-api .

Run the Container:
 docker-compose up


 🧪 Running Tests
  pytest



📜 Contribution Guidelines

Fork the repository

Create a feature branch (feat/add-new-feature)

Commit using conventional messages:
 git commit -m "feat: add caching for FAQ translations"

Push and create a pull request



📄 License

This project is licensed under the MIT License.



📧 Contact

Author: Vishal Kumar

GitHub: https://github.com/Vishal726086