import numpy as np

def calculate_vwap(price, volume):
    """
    Calculate the Volume Weighted Average Price (VWAP)

    Parameters:
        price (array): The price of the asset
        volume (array): The volume of the asset

    Returns:
        final_vwap (float): The vwap of the entire period
        vwap_values (array): The vwap values at each point in time
    """
    vwap_values = np.cumsum(price * volume) / np.cumsum(volume)
    final_vwap = vwap_values[-1]
    return final_vwap, vwap_values