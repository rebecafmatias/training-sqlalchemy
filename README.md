# Data Journey - SQLAlchemy Example

This project demonstrates the use of SQLAlchemy for database management in Python. It includes core functionalities for database initialization, seeding data, and a main entry point to run the application.

## Project Structure

```
src/
├── core/
│   ├── database.py    # Database initialization and session management
│   └── models.py      # SQLAlchemy models
├── seeds/
│   ├── products.py    # Seed data for products
│   └── suppliers.py    # Seed data for suppliers
└── main.py            # Entry point to run the application
```

## Features

- **Database Initialization**: Set up and configure a SQLite database.
- **Data Seeding**: Populate the database with example data for products and suppliers.
- **Main Entry Point**: Run the application to initialize the database and seed data.

## Requirements

- Python 3.11
- SQLAlchemy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rebecafmatias/training-sqlalchemy.git
   cd data-journey-sqlalchemy
   ```

2. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install the required packages:
   ```bash
   poetry install
   ```

4. To run the application, use:
   ```bash
   poetry run python src/main.py
   ```

## Usage

To run the application and initialize the database with seed data, execute:

```bash
python src/main.py
```

## License

This project is licensed under the MIT License.