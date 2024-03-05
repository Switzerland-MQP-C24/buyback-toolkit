import pandas as pd

# class Strategy:
#     def __init__(self, strategy):
#         raise NotImplementedError("You should implement this!")

#     def execute(self, data):
#         raise NotImplementedError("You should implement this!")


def buy_shares(desired_shares, price, remaining_budget=-1, remaining_shares=-1):
    """
    Calculate the number of shares to purchase.
    
    Parameters:
    - desired_shares: The number of shares to purchase.
    - price: The price of the shares.
    - remaining_budget: The remaining budget to purchase shares. If -1, the budget is not considered.
    - remaining_shares: The remaining shares to purchase. If -1, the remaining shares is not considered.
    
    Returns:
    - shares: The number of shares to purchase.
    - cost: The cost of purchasing the shares.
    - remaining_budget: The remaining budget after purchasing shares.
    - remaining_shares: The remaining shares after purchasing shares.
    """
    # Calculate the number of shares to purchase
    shares = desired_shares
    if remaining_budget != -1:
        shares = min(shares, remaining_budget / price)
    if remaining_shares != -1:
        shares = min(shares, remaining_shares)
    shares = int(shares)

    # Calculate the cost of purchasing the shares
    cost = shares * price

    # Calculate the remaining budget and shares
    if remaining_budget != -1:
        remaining_budget -= cost
    if remaining_shares != -1:
        remaining_shares -= shares

    return shares, cost, remaining_budget, remaining_shares


def percent_strategy(volumes, participation_rate, target_shares=-1): # TODO: add budget and target shares
    """
    Calculate the number of shares to purchase based on the participation rate.
    
    Parameters:
    - volumes: A pandas Series of traded volumes.
    - participation_rate: The percentage of the volume to participate in.
    - target_shares: The number of shares to purchase. If -1,
    
    Returns:
    - shares: The number of shares to purchase.
    """
    # Make sure the volumes are a pandas Series
    if not isinstance(volumes, pd.Series):
        volumes = pd.Series(volumes)

    # Calculate the number of shares to purchase
    shares = volumes * participation_rate

    # Round to the nearest whole number
    shares = shares.round().astype(int)
    
    return shares