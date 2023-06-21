class ProductCatalog:
    def __init__(self, products):
        self.products = products

    def ürünlerilistele(self):
        print("--------- PRODUCT CATALOG ---------")
        for product in self.products:
            name, price = product
            print(f"{name:10}: {price:.2f} TL")
        print("-----------------------------------")


class OrderManager:
    def __init__(self):
        self.order = []

    def ürünekle(self, item):
        self.order.append(item)

    def ürünçıkart(self, item):
        if item in self.order:
            self.order.remove(item)
        else:
            print("\nÖZÜR DİLERİZ, SİLMEK İSTEDİĞİNİZ ÜRÜN SEPETİNİZDE BULUNAMADI!")

    def ürünlerigöster(self):
        print("------ Siparişiniz ------")
        for item in self.order:
            print("Siparişleriniz>>>", item, end="\n\n")


class ShoppingCart:
    def __init__(self, ürünkatalok, siparisyönet):
        self.ürünkatalok = ürünkatalok
        self.siparisyönet = siparisyönet
        self.total = 0

    def alışveriş(self):
        self.ürünkatalok.ürünlerilistele()

        while True:
            choice = input(
                "\nİstediğiniz cihazı seçiniz (sipariş bittiyse 'd'ye basınız. Silmek istediğiniz ürün için 'sil' yazınız.): \n"
            ).lower()

            if choice == "d":
                break
            elif choice == "sil":
                itemçıkart = input("Silinecek siparişinizi seçiniz:")
                self.siparisyönet.ürünçıkart(itemçıkart)
            else:
                self.siparisyönet.ürünekle(choice)

        self.siparisyönet.ürünlerigöster()
        self.fiyat()

    def fiyat(self):
        for item in self.siparisyönet.order:
            for product in self.ürünkatalok.products:
                name, price = product
                if item == name:
                    self.total += price

        print(f"Toplam ücretiniz: {self.total:.2f} TL\n\n")


liste = [
    ("ürün1", 100.00),
    ("ürün2", 200.00),
    ("ürün3", 300.00),
    ("ürün4", 400.00),
]

ürünkatalok = ProductCatalog(liste)
siparisyönet = OrderManager()
shopping_cart = ShoppingCart(ürünkatalok, siparisyönet)
shopping_cart.alışveriş()
