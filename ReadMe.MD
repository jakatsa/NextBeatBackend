# NextBeat

## Overview

NextBeat is a beat-selling application designed for music creators and enthusiasts. The platform provides a seamless way for vendors to manage and sell beats, while offering users an intuitive interface to browse, filter, and purchase beats.

## Features

### Current Features

- **Beat Management**:
  - List and retrieve beats.
  - Add new beats (producer-only).
  - Enhanced user experience with dynamic filtering.
  - Playing beats online
- **Cart Functionality**:
  - Add beats to a shopping cart for streamlined purchases.
  - **User Authentication**:
  - User registration and login capabilities using JWT.

### Planned Features

- **Payment System Integration**:
  - Support for payment gateways like Mpesa and PayPal.
- **Order Management**:
  - checkout process.
- **Messaging Features**:
  - Implementaion of a messaging dashboaord allowing clients to interact.

**User Relationshhip Features**:

- users are able to follow each other.

## Dependencies

The project relies on the following Python packages:

- `asgiref==3.8.1`
- `Django==5.1.2`
- `django-cors-headers==4.5.0`
- `django-filter==24.3`
- `djangorestframework==3.15.2`
- `pillow==11.0.0`
- `sqlparse==0.5.1`
- `typing_extensions==4.12.2`

## File Structure

```
NextBeat
├── Nextbeat             # Django project directory
├── beats                # Beat-related models, views, and templates
├── db.sqlite3           # SQLite database
├── frontend             # Frontend assets and configurations
├── manage.py            # Django management script
├── orders               # Order management app
├── requirements.txt     # Dependencies file
├── settings             # Project settings and configurations
├── user_relationships   # User relationship models and logic
├── users                # User management app
```

## Getting Started

### Prerequisites

- Python 3.x
- Django 5.1.2
- Virtual environment setup

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd NextBeat
   ```
2. Activate the virtual environment:
   ```bash
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate   # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the application at `http://127.0.0.1:8000/`.

## Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or support, please contact jakatsa5@gmail.com
