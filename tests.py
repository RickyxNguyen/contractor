from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

sample_product_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_product = {
    'name': 'WiPro',
    'description': 'Chinese knockoff',
    'price': 2999.99
}
sample_cart_id = ObjectId('5d55cffc4a3d4031f42827a4')
sample_cart = {
    'name': 'WiBook Pro 15',
    'description': 'Chinese knockoff',
    'price': 999.99
}


@mock.patch('pymongo.collection.Collection.find_one')
class ContractorTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_show_products(self, prod_list):
        """Test the playlists homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        # self.assertIn(result.data)

    def test_show_cart(self, something):
        """Test submitting a new playlist."""
        result = self.client.get('/cart', data=sample_cart)

        # After submitting, should redirect to that playlist's page
        self.assertEqual(result.status, '200 OK')
        # self.assertIn(result.data)


if __name__ == '__main__':
    unittest_main()
