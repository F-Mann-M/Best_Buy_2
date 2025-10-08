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
            self._promotion = None

        except (ValueError, TypeError) as e:
            print(f"Initialisation error: {e} ")
            self._activ = False # deactivate product if somthing went wrong

    def set_promotion(self, promotion): # add promotion object
        self._promotion = promotion


    def remove_promotion(self):
        self._promotion = None


    def get_promotion(self):
        if self._promotion:
            return self._promotion.name
        return None



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
        parts = [f"{self._name}", f"Price: {self._price}", f"Quantity: {self.get_quantity()}"]

        if self._promotion:
            parts.append(f"Promotion: {self.get_promotion()}")

        return ", ".join(parts)


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
                raise ValueError("Quantity must be greater than zero")
            if not self._activ:
                raise RuntimeError("Product is not activ")
            if quantity > self._quantity:
                raise ValueError(f"Not enough products are available.")

            #reduce stock
            self._quantity -= quantity

            # deactivate product
            if quantity == 0:
                self.deactivate()

            if self._promotion:
                print(f"Promotion: {self._promotion.name}")
                return self._promotion.apply_promotion(self, quantity)

            return self._price * quantity

        except (ValueError, RuntimeError) as e:
            print(f"Error: {e}")
            return 0


class NonStockedProduct(Product):

    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity = 0)
        self._quantity = 0
        self._is_active = True

    def get_quantity(self) -> str:
        return "Unlimited"

    def set_quantity(self, quantity):
        raise AttributeError("This product has no quantity")

    def buy(self, quantity=1) -> float:
        if not self._is_active:
            raise RuntimeError("Product is not active")
        return self._price * quantity


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        try:
            if not isinstance(maximum, int):
                raise TypeError("Maximum must be a number")
            if maximum < 0:
                raise ValueError("Maximum can't be negative")
            self._maximum = maximum
        except (ValueError, RuntimeError) as e:
            print(f"Error: {e}")

    def get_quantity(self):
        return f"limited to {self._maximum}"

    def get_maximum(self):
        return self._maximum

    def buy(self, quantity) -> float:
        if quantity > self._maximum:
            raise ValueError(f"Maximum oder is {self._maximum}")
        return super().buy(quantity)
