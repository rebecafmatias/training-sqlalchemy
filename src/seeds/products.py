def seed_products():    
    from core.database import session
    from core.models import Product

    products_to_insert = [
        Product(name='Laptop', price=1200.00,supplier_id=1),
        Product(name='Smartphone', price=800.00,supplier_id=2),
        Product(name='Tablet', price=400.00,supplier_id=3),
        Product(name='Monitor', price=300.00,supplier_id=1),
        Product(name='Keyboard', price=50.00,supplier_id=2),
        Product(name='Mouse', price=30.00,supplier_id=3),
        Product(name='Printer', price=150.00,supplier_id=1),
        Product(name='Router', price=100.00,supplier_id=2)
    ]

    with session as s:
        s.add_all(products_to_insert)
        s.commit()