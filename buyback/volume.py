import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

from .constants import MOTNH

def simple_moving_average(data, period=MOTNH):
    """
    Simple moving average

    Parameters:
    - data: A pandas Series of data.
    - period: The number of periods to consider in the moving average.

    Returns:
    - A pandas Series of the moving average.
    """
    return data.rolling(window=period).mean()

def exponential_moving_average(data, period=MOTNH, adjust=False):
    """
    Exponential moving average

    Parameters:
    - data: A pandas Series of data.
    - period: The number of periods to consider in the moving average.
    - adjust: Whether to adjust the weights for the first period.

    Returns:
    - A pandas Series of the moving average.
    """
    return data.ewm(span=period, adjust=adjust).mean()

def keras_predictor(volume, model_path, verbosity="auto"):
    """
    Predict the daily trade volume using a Keras model.

    Parameters:
    - volume: A pandas Series of trade volumes.
    - model_path: The path to the Keras model.
    - verbosity: The verbosity level of the Keras model. 0 = silent, 1 = progress bar, 2 = single line.

    Returns:
    - A pandas Series of the predicted trade volumes.
    """
    try:
        from keras.models import load_model
    except ImportError:
        raise ImportError("Keras is not installed. Please install Keras to use this function.")

    look_back = MOTNH # DEBUG: hardcoded because the model is trained with this

    # Load the Keras model
    model = load_model(model_path)

    # Prepare the latest data for prediction
    scaler = MinMaxScaler(feature_range=(0, 1))
    volume_data = scaler.fit_transform(volume.values.reshape(-1, 1))

    # Create X for lookback window directly 
    X = np.array([volume_data[i:(i + look_back), 0] for i in range(len(volume_data) - look_back)])

    # Vectorized prediction
    predictions = model.predict(X, verbose=verbosity)

    # Inverse transform and adjustments
    predictions = scaler.inverse_transform(predictions)[:, 0]  # Get the relevant column
    predictions[predictions < 0] = 0  # Ensure non-negative values
    predictions = np.rint(predictions)  # Round to nearest integer

    # Create predictions DataFrame with shifted index
    predictions_df = pd.Series(predictions, index=volume.index[look_back:]).shift(-1) 

    return predictions_df 