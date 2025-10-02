class Product:

    def __init__(self, name: str, price: float, quantity: int):

        try:
            # Type validation
            if not isinstance(name, str):
                raise TypeError("Product name must be a string.")
            if not isinstance(price, (int, float)):
                raise TypeError("Price must be an int or a float.")
            if not isinstance(quantity, int):
                raise TypeError("Quantity must be an int.")

            # Value validation
            if float(price) < 0:
                raise ValueError("Price cannot be negative")
            if int(quantity) < 0:
                raise ValueError("Quantity cannot be negative.")

            # Initialize instance variable
            self._name = str(name)
            self._price = float(price)
            self._quantity = int(quantity)
            self._activ = True

        except (ValueError, TypeError) as e:
            print(f"Initialisation error: {e} ")
            self._activ = False # deactivate product if somthing went wrong

    def get_quantity(self) -> int:
        """ Getter function for quantity. Returns the quantity (int)"""
        return self._quantity


    def set_quantity(self, quantity):
        """ Setter function for quantity. If quantity reaches 0, deactivates the product"""
        if quantity >= 0:
            self._quantity = quantity
        else:
            print("Quantity must be a positive number")


    def is_active(self) -> bool:
        """ Getter function for active. Returns True if the product is active, otherwise False."""
        return self._activ


    def get_price(self):
        return self._price

    def activate(self):
        """ Activates the product """
        self._activ = True


    def deactivate(self):
        """ Deactivates the product """
        self._activ = False


    def show(self):
        """ prints a string that represents the product """
        return self._name


    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        """
        try:
            quantity = int(quantity)
            if quantity <= 0:
                print("Quantity must be greater than zero")
            if not self._activ:
                raise Exception("Product is not activ")
            if quantity > self._quantity:
                raise Exception(f"Not enough products are available.")
            if quantity == 0:
                self._activ = False # Products empty
            self._quantity -= quantity
            return self._price * quantity
        except (ValueError, Exception) as e:
            print(f"Error: {e}")
            return 0