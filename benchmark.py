import numpy as np

def calculate_vwap(price, volume): # DEBUG: insitutional is a misnomer
    """
    Calculate the Volume Weighted Average Price (VWAP)

    Parameters:
        price (array): The price of the asset
        volume (array): The volume of the asset

    Returns:
        vwap_values (array): The vwap values at each point in time
    """
    vwap_values = np.cumsum(price * volume) / np.cumsum(volume)
    return vwap_values

def calculate_bogus_benchmark(price, volume):
    """
    Calculate the bogus Volume Weighted Average Price (VWAP)

    Parameters:
        price (array): The price of the asset
        volume (array): The volume of the asset

    Returns:
        vwap_values (array): The vwap values at each point in time
    """
    #vwap_values = (price * volume) / (volume)
    vwap_values = price.expanding().mean() # assuming price is the day's vwap
    return vwap_values