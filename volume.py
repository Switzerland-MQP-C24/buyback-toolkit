import pandas as pd
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# TODO: move constants to a different file and explain
WEEK = 5
MOTNH = 21
QUARTER = 63
HALF_YEAR = 126
YEAR = 252

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

def keras_predictor(volume, model_path):
    """
    Predict the daily trade volume using a Keras model.

    Parameters:
    - volume: A pandas Series of trade volumes.
    - model_path: The path to the Keras model.

    Returns:
    - A pandas Series of the predicted trade volumes.
    """
    look_back = 21 # DEBUG: hardcoded because the model is trained with this

    # Load the Keras model
    model = load_model(model_path)

    # Prepare the latest data for prediction
    scaler = MinMaxScaler(feature_range=(0, 1))
    volume_data = scaler.fit_transform(volume.values.reshape(-1, 1))

    X = []
    for i in range(len(volume_data) - look_back):
        X.append(volume_data[i:(i + look_back), 0])
    X = np.array(X) # DEBUG: convert to numpy array. Is this necessary?

    # Predict the trade volumes
    predictions = []
    for i in range(len(X)):
        prediction = model.predict(X[i].reshape(1, -1))
        prediction = scaler.inverse_transform(prediction)[0, 0]
        prediction = max(prediction, 0) # make sure the prediction is not negative
        prediction = np.rint(prediction) # round the prediction to the nearest integer
        predictions.append(prediction)

    predictions_df = pd.Series(predictions, index=volume.index[look_back:]).shift(-1) # DEBUG: shift the predictions by 1 day
    return predictions_df