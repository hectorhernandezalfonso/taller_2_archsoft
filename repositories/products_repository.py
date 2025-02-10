from models.products import Products, db


class ProductRepository:

    @staticmethod
    def create_product(name, description):
        product = Products(name = name, description = description)
        db.session.add(product)

        db.session.commit()
        return product
    

    @staticmethod
    def update_product(name, description):
        product = Products.query.filter_by(name=name).first()  # ✅ Corrected query
    
        if not product:
            return None  
        if description:
            product.description = description  
    
        db.session.commit()  
        return product

