from products import Product

class Store:

    def __init__(self, products=None):
        try:
            # Type validation
            if not isinstance(products, list):
                raise TypeError("Product list must be a list.")

            # Value validation
            if products is None or len(products) == 0:
                raise ValueError("List of products is empty or items in list are not valid.")

            for product in products:
                if not isinstance(product, Product):
                    raise TypeError(f"All items in products list must be objects of the class Product.")

            self._products = products

        except Exception as e:
            print(f"Initialisation error: {e} ")
            self._products = []



    def add_product(self, product):
        """ Add product to products list"""
        self._products.append(product)


    def remove_product(self, product):
        """ Removes product form products list """
        if product in self._products:
            self._products.remove(product)


    def get_total_quantity(self) -> int:
        """ Returns how many products are in products list"""
        return sum(product.get_quantity() for product in self._products if isinstance(product.get_quantity(), int))


    def get_all_products(self) -> list:
        """ Returns all products in the store that are active."""
        activ_products = []
        for product in self._products:
            if product.is_active():
                activ_products.append(product)
        return activ_products

    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


