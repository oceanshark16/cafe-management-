"""
Unit tests for Cafe Management System business logic
"""
import unittest
from cafe_logic import CafeManager

class TestCafeManager(unittest.TestCase):
    def setUp(self):
        # Create a fresh CafeManager instance for each test
        self.cafe = CafeManager()
    
    def test_initial_state(self):
        """Test that the initial state of the order is empty"""
        # Check initial order values
        for item, quantity in self.cafe.order.items():
            self.assertEqual(quantity, 0, f"Initial quantity for {item} should be 0")
        
        # Check initial costs
        self.assertEqual(self.cafe.costs['drinks_cost'], 0)
        self.assertEqual(self.cafe.costs['cakes_cost'], 0)
        self.assertEqual(self.cafe.costs['service_charge'], 100)
        self.assertEqual(self.cafe.costs['tax'], 0)
        self.assertEqual(self.cafe.costs['subtotal'], 0)
        self.assertEqual(self.cafe.costs['total'], 0)
    
    def test_update_item_quantity(self):
        """Test updating item quantities"""
        # Update quantity of latte
        result = self.cafe.update_item_quantity('latte', 3)
        self.assertTrue(result)
        self.assertEqual(self.cafe.order['latte'], 3)
        
        # Try updating non-existent item
        result = self.cafe.update_item_quantity('not_an_item', 5)
        self.assertFalse(result)
    
    def test_get_item_price(self):
        """Test retrieving item prices"""
        self.assertEqual(self.cafe.get_item_price('latte'), 50)
        self.assertEqual(self.cafe.get_item_price('chocolate_cake'), 100)
        self.assertEqual(self.cafe.get_item_price('not_an_item'), 0)
    
    def test_calculate_costs_empty_order(self):
        """Test cost calculation for empty order"""
        costs = self.cafe.calculate_costs()
        
        self.assertEqual(costs['drinks_cost'], 0)
        self.assertEqual(costs['cakes_cost'], 0)
        self.assertEqual(costs['service_charge'], 100)
        self.assertEqual(costs['subtotal'], 100)
        self.assertEqual(costs['tax'], 15)  # 15% of 100
        self.assertEqual(costs['total'], 115)
    
    def test_calculate_costs_with_items(self):
        """Test cost calculation with items in the order"""
        # Add some items to the order
        self.cafe.update_item_quantity('latte', 2)  # 2 × 50 = 100
        self.cafe.update_item_quantity('chocolate_cake', 1)  # 1 × 100 = 100
        self.cafe.update_item_quantity('fruit_juice', 3)  # 3 × 300 = 900
        
        costs = self.cafe.calculate_costs()
        
        # Expected costs:
        # Drinks: 2 lattes (100) + 3 fruit juices (900) = 1000
        # Cakes: 1 chocolate cake (100) = 100
        # Service charge: 100
        # Subtotal: 1000 + 100 + 100 = 1200
        # Tax: 15% of 1200 = 180
        # Total: 1200 + 180 = 1380
        
        self.assertEqual(costs['drinks_cost'], 1000)
        self.assertEqual(costs['cakes_cost'], 100)
        self.assertEqual(costs['service_charge'], 100)
        self.assertEqual(costs['subtotal'], 1200)
        self.assertEqual(costs['tax'], 180)
        self.assertEqual(costs['total'], 1380)
    
    def test_reset_order(self):
        """Test resetting the order"""
        # Add some items to the order
        self.cafe.update_item_quantity('latte', 2)
        self.cafe.update_item_quantity('chocolate_cake', 1)
        
        # Calculate costs
        self.cafe.calculate_costs()
        
        # Reset order
        self.cafe.reset_order()
        
        # Check that everything is reset
        for item, quantity in self.cafe.order.items():
            self.assertEqual(quantity, 0, f"Quantity for {item} should be 0 after reset")
        
        self.assertEqual(self.cafe.costs['drinks_cost'], 0)
        self.assertEqual(self.cafe.costs['cakes_cost'], 0)
        self.assertEqual(self.cafe.costs['service_charge'], 100)
        self.assertEqual(self.cafe.costs['tax'], 0)
        self.assertEqual(self.cafe.costs['subtotal'], 0)
        self.assertEqual(self.cafe.costs['total'], 0)
    
    def test_generate_receipt(self):
        """Test receipt generation"""
        # Add some items to the order
        self.cafe.update_item_quantity('latte', 2)
        self.cafe.update_item_quantity('chocolate_cake', 1)
        
        # Generate receipt
        receipt = self.cafe.generate_receipt()
        
        # Check that the receipt contains expected elements
        self.assertIn("Cafe Management System - Receipt", receipt)
        self.assertIn("Latte", receipt)
        self.assertIn("2", receipt)
        self.assertIn("Rs. 100", receipt)
        self.assertIn("Chocolate Cake", receipt)
        self.assertIn("1", receipt)
        self.assertIn("Rs. 100", receipt)
        self.assertIn("Cost of Drinks:", receipt)
        self.assertIn("Cost of Cakes:", receipt)
        self.assertIn("Service Charge:", receipt)
        self.assertIn("Subtotal:", receipt)
        self.assertIn("Tax (15%):", receipt)
        self.assertIn("Total:", receipt)
        self.assertIn("Thank you for visiting our cafe!", receipt)

if __name__ == "__main__":
    unittest.main()
