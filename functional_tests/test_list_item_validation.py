from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
           # Sara goes to the home page and accidentally tries to submit
           # an empty list item
           self.browser.get(self.server_url)
           self.get_item_input_box().send_keys('\n')

           # The home page refreshes and there is an error message saying that
           # list items cannot be blank.
           error = self.browser.find_element_by_css_selector('.has-error')
           self.assertEqual(error.text, "You can't have an empty list item")

           # She tries again with characters and it works.
           self.get_item_input_box().send_keys('Buy milk\n')
           self.check_for_row_in_list_table('1: Buy milk')
           
           # To mess with me, she tries to submit a blank item again.
           self.get_item_input_box().send_keys('\n')

           # She receives a similar warning.
           self.check_for_row_in_list_table('1: Buy milk')
           error = self.browser.find_element_by_css_selector('.has-error')
           self.assertEqual(error.text, "You can't have an empty list item")

           # And she can correct by filling in some text
           self.get_item_input_box().send_keys('Make tea\n')
           self.check_for_row_in_list_table('1: Buy milk')
           self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # Sara goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # she accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')

        # she sees a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You've already got this in your list")

