import unittest
import numpy as np
from helpers.volatility import calculate_historical_var, calculate_variance_covariance_var, calculate_monte_carlo_var

# Generated with ChatGPT
class TestVolatility(unittest.TestCase):
    def test_historical_var(self):
        returns = np.random.normal(0, 0.1, 1000)  # Simulate some returns
        confidence_level = 0.95
        var = calculate_historical_var(returns, confidence_level)
        self.assertTrue(0 <= var <= max(abs(returns)), "VaR should be within the range of absolute returns")

    def test_variance_covariance_var(self):
        P = 1000000  # Portfolio value
        sigma = 0.05  # Standard deviation of returns
        confidence_level = 0.95
        var = calculate_variance_covariance_var(P, sigma, confidence_level)
        self.assertTrue(var > 0, "VaR should be positive")
        self.assertTrue(var <= P, "VaR should not exceed the portfolio value")

    def test_monte_carlo_var(self):
        P = 1000000  # Portfolio value
        mu = 0.01  # Expected return
        sigma = 0.05  # Standard deviation of returns
        time_horizon = 1  # 1 year
        simulations = 10000
        confidence_level = 0.95
        var = calculate_monte_carlo_var(P, mu, sigma, time_horizon, simulations, confidence_level)
        self.assertTrue(var > 0, "VaR should be positive")
        self.assertTrue(var <= P, "VaR should not exceed the portfolio value")

if __name__ == '__main__':
    unittest.main()