from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
           # Sara goes to the home page and accidentally tries to submit
           # an empty list item
           # The home page refreshes and there is an error message saying that
           # list items cannot be blank.
           # She tries again with characters and it works.
           # To mess with me, she tries to submit a blank item again.
           # She receives a similar warning.
           self.fail('Write me!')


