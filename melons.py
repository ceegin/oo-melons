"""Classes for melon orders."""

from random import randint

class AbstractMelonOrder(object):
    """Base melon order class"""
    def __init__(self, species, qty, country_code=None, order_type=None, tax=None):
            """Initialize melon order attributes."""
            self.species = species
            self.qty = qty
            self.country_code = country_code
            self.shipped = False
            self.order_type = order_type
            self.tax = tax

    def get_base_price(self):
        """Return a random integer"""
        return randint(5, 9)

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        if self.species == "Christmas":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        return round(total, 2)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

   

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initializes new domestic melon order"""

        super(DomesticMelonOrder, self).__init__(species, qty, "USA", "domestic", 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initializes new domestic melon order"""

        super(InternationalMelonOrder, self).__init__(species, qty, country_code, "international", 0.17)


    def get_total(self):
        """Calculate price, including tax."""

        result = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            result += 3

        return round(result, 2)

class GovernmentMelonOrder(DomesticMelonOrder):
    """A governmental melon order"""

    passed_inspection = False
    def mark_inspection(self, passed):
        self.passed_inspection = passed


test = DomesticMelonOrder("watermelon", 6)
test11 = DomesticMelonOrder("watermelon", 6)
test12 = DomesticMelonOrder("watermelon", 6)
test13 = DomesticMelonOrder("watermelon", 6)
test14 = DomesticMelonOrder("watermelon", 6)
test15 = DomesticMelonOrder("watermelon", 6)
test2 = DomesticMelonOrder('watermelon', 6)
test3 = InternationalMelonOrder("watermelon", 6, "AUS")
test4 = InternationalMelonOrder("watermelon", 6, "AUS")
test5 = GovernmentMelonOrder("watermelon", 6)