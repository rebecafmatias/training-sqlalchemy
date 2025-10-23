def seed_suppliers():
    from core.database import session
    from core.models import Supplier

    suppliers_to_insert = [
        Supplier(name='Supplier A',contact_info='suplier_a@test.com'),
        Supplier(name='Supplier B',contact_info='suplier_b@test.com'),
        Supplier(name='Supplier C',contact_info='suplier_c@test.com')
    ]

    with session as s:
        s.add_all(suppliers_to_insert)
        s.commit()