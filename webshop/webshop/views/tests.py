from __future__ import absolute_import


from pyramid import testing
from ..tests import BaseTest, dummy_request


class ProductViewTests(BaseTest):
    def setUp(self):
        super(ProductViewTests, self).setUp()
        self.config = testing.setUp()
        self.init_database()

    def tearDown(self):
        testing.tearDown()

    def test_get_all_products(self):
        from .products import ProductViews

        inst = ProductViews(dummy_request(self.session))
        response = inst.get_all_products()
        self.assertEqual(response.status_int, 500)
