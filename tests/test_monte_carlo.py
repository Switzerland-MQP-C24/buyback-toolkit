import unittest
import numpy as np
from buyback.monte_carlo import simulate_gbm

class TestMonteCarloSimulation(unittest.TestCase):
    def test_simulate_gbm_initial_price_and_shape(self):
        start_price = 100  # Starting asset price
        drift = 0.05  # Expected annual return
        volatility = 0.2  # Annual volatility
        days = 252  # Number of trading days
        num_simulations = 1000  # Number of simulations
        
        price_paths = simulate_gbm(start_price, drift, volatility, days, num_simulations)
        
        # Check that the first row of price_paths is equal to start_price
        self.assertTrue(np.all(price_paths[0] == start_price), "First row should be initialized with start_price")
        
        # Check the shape of price_paths
        self.assertEqual(price_paths.shape, (days, num_simulations), "Shape of price_paths should match (days, num_simulations)")

if __name__ == '__main__':
    unittest.main()