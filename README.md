 CookPal Web Application

 Introduction

CookPal is a web application designed to discover and share recipes from around the world. This README provides an overview of the application's features, installation instructions, and usage guidelines.

 Features

- Extensive Recipe Repository: Access a wide variety of recipes from different cuisines and meal types.
- Advanced Search: Easily find recipes by name, type, or origin.
- User Accounts: Create an account to submit recipes, rate dishes, and leave comments.
- Favorites: Save your favorite recipes for easy access.
- Interactive Community: Engage with other users by sharing tips and tricks, and interacting through comments.

 Installation

 Prerequisites

- Python 3.x
- Django 3.x
- Bootstrap 4.x
- A web browser

 Steps

1. Clone the repository:
   ```bash
   git clone http://itgroup27.pythonanywhere.com
   ```

2. Navigate to the project directory:
   ```bash
   cd CookPal
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

7. Open your web browser and navigate to `http://127.0.0.1:8000` to start using CookPal.

Website
Visit https://itgroup27.pythonanywhere.com/ 

 Usage

 Browsing Recipes

- Homepage: View the latest recipes, sorted by upload time.
- Advanced Search: Use the search bar to filter recipes by name, type, or origin.
- Recipe Details: Click on a recipe card to view detailed information, including ingredients and instructions.

 User Accounts

- Sign Up: Create an account to unlock additional features.
- Log In: Access your profile, favorite recipes, and interact with other users.
- Profile Management: Edit your profile details, view your submitted recipes, and manage your favorites.

 Recipe Management

- Create Recipe: Submit your own recipes with images, ingredients, and instructions.
- Favorite Recipes: Save recipes to your favorites for easy access later.
- Share Recipes: Share recipe URLs with others.

 Community Interaction

- Comments: Leave comments on recipes and rate them.
- Moderation: Report offensive content for review by moderators.

 Development

 System Architecture

- Frontend: Built using HTML, CSS (Bootstrap), and JavaScript.
- Backend: Developed with Django, using a PostgreSQL database.
- API: Django's built-in email API for account-related notifications.

 ER Diagram

- UserAccount: Attributes include username, email, phone number, nickname, favorites, and image.
- SiteAdmin: Manages reported content and user support.

 Wireframes

- Detailed wireframes for the main page, login/signup page, profile page, and recipe creation page.

 Testing

- Unit Tests: Comprehensive test cases for all functionalities, including user account management, recipe creation, and advanced search.
- Automated Testing: Uses Django's TestCase class for automated testing of all components.


For any issues or support, please contact the development team via the provided email addresses or use the support form on the website.


CookPal - Discover and share the joy of cooking with recipes from around the world!
![image](https://github.com/Daniel-Nduka/CookPal/assets/118636486/d9fe2415-ff1b-4c73-a24f-473d7a769d4d)
