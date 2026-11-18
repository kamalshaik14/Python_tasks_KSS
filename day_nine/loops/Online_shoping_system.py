#9. Online Shopping System (Multilevel Inheritance)
#An e-commerce company organizes products using multiple levels. Create classes
#Product → ElectronicProduct → MobilePhone using multilevel inheritance and display product details.







class Product:
    def display(self):
        print("Product:", self.name)


class ElectronicProduct(Product):
    pass


class MobilePhone(ElectronicProduct):
    pass


phone1 = MobilePhone()
phone1.name = "Samsung"

phone2 = MobilePhone()
phone2.name = "iPhone"

phone1.display()
phone2.display()
