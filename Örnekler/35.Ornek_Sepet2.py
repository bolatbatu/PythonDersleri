class ProductCatalog:
    def __init__(self):
        self.products = {
            "laptop": 12500.00,
            "mouse": 750.50,
            "headphone": 1250.50,
            "klavye": 2450.00,
            "mousepad": 250.00,
            "144hz": 3500.00,
            "240hz": 9500.00,
            "kulaklık": 350.00,
            "hoparlör": 905.00,
            "rgbklavye": 3250.00
        }

    def show_products(self):
        print("--------- SHOPPING CART ---------")
        for key, value in self.products.items():
            print(f"{key:10}: {value:.2f} TL")
        print("------------------------")


class OrderManager:
    def __init__(self):
        self.order = []

    def add_to_order(self, item):
        self.order.append(item)

    def remove_from_order(self, item):
        if item in self.order:
            self.order.remove(item)
        else:
            print("\nÖZÜR DİLERİZ, SİLMEK İSTEDİĞİNİZ ÜRÜN SEPETİNİZDE BULUNAMADI!")

    def show_order(self):
        print("------ Siparişiniz ------")
        for item in self.order:
            print("Siparişleriniz>>>", item, end="\n\n")


class ShoppingCart:
    def __init__(self, product_catalog, order_manager):
        self.product_catalog = product_catalog
        self.order_manager = order_manager
        self.total = 0

    def start_shopping(self):
        self.product_catalog.show_products()

        while True:
            choice = input(
                "\nİstediğiniz cihazı seçiniz (sipariş bittiyse 'd'ye basınız. Silmek istediğiniz ürün için 'sil' yazınız.): \n"
            ).lower()

            if choice == "d":
                break
            elif choice == "sil":
                item_to_remove = input("Silinecek siparişinizi seçiniz:")
                self.order_manager.remove_from_order(item_to_remove)
            else:
                self.order_manager.add_to_order(choice)

        self.order_manager.show_order()
        self.calculate_total()

    def calculate_total(self):
        for item in self.order_manager.order:
            price = self.product_catalog.products.get(item, 0)
            self.total += price

        print(f"Toplam ücretiniz: {self.total:.2f} TL\n\n")


product_catalog = ProductCatalog()
order_manager = OrderManager()
shopping_cart = ShoppingCart(product_catalog, order_manager)
shopping_cart.start_shopping()
