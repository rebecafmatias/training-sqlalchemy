from core.database import initialize_database
from seeds.suppliers import seed_suppliers
from seeds.products import seed_products

def main():
    # Initialize the database connection
    print("Initializing database...")
    
    db = initialize_database()
    
    # Your main application logic here
    print("Database initialized:", db)

    # Seed suppliers
    print("Seeding suppliers...")
    seed_suppliers()
    print("Suppliers seeded.")
    # Seed products
    print("Seeding products...")
    seed_products()
    print("Products seeded.")
    

if __name__ == "__main__":
    main()