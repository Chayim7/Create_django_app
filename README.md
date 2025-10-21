# LitreView

📚 LITReview

LITReview is a Django-based social web app for book lovers and literature enthusiasts.
It allows users to discover, review, and follow others’ reading activity — a clean and minimal MVP built with the Django template system.

🚀 Features

🔐 User authentication (signup, login, logout)

🧑‍🤝‍🧑 Follow/unfollow other users

🏠 Personalized feed with reviews from followed users

📚 Book search and creation

✍️ Write, edit, and delete reviews (one per book per user)

📖 Public book pages showing all reviews

🧩 Example users and posts via fixtures

🏗️ Project Structure
litreview/
├── manage.py
├── README.md
├── requirements.txt
│
├── litreview_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/accounts/
│
├── books/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/books/
│
├── templates/
│   └── base.html
│
└── fixtures/
    └── seed.json

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone <your_repository_url>
cd litreview

2️⃣ Create a virtual environment
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt


If you don’t have requirements.txt yet, create it with:

pip freeze > requirements.txt

4️⃣ Apply migrations and load initial data
python manage.py migrate
python manage.py loaddata fixtures/seed.json

5️⃣ Run the development server
python manage.py runserver


Then open your browser and go to:
👉 http://127.0.0.1:8000

👤 Test Accounts
Username	Password	Role
alice	alicepass	Regular User
bob	bobpass	Regular User

Use these accounts to explore the app after loading fixtures.

🖥️ Core Pages Overview
Page	URL	Description
Login	/login/	User login page
Signup	/signup/	Create a new account
Home Feed	/	Shows all reviews (if not logged in)
Following Feed	/feed/	Reviews from followed users
Profile	/profile/	View your profile and reviews
User Profile	/u/<username>/	View another user’s profile and follow/unfollow them
Book Search	/books/	Search for books
Book Detail	/books/<id>/	View book details and reviews
New Review	/books/<id>/review/new/	Add a review for a book
🧩 Technologies Used

Python 3

Django (template-based rendering)

SQLite (default dev database)

Pillow (image uploads)

Bootstrap (optional — for simple styling)

🧰 Development Tips

Use python manage.py createsuperuser to create an admin account if needed.

Static and media files are automatically served in development.

Keep your app structure modular: accounts handles users, books handles content.

🧪 Testing the App Locally

After running the server, test these actions:

Create a new user via Signup

Log in and edit your Profile

Follow another user

Add a Book and write a Review

Check that reviews appear in your Feed

Log out and confirm public views work properly
