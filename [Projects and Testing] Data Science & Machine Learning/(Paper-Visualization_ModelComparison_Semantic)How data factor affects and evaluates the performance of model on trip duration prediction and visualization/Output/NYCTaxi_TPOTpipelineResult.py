import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
try:
    from sklearn.impute import SimpleImputer as Imputer
except ImportError:
    from sklearn.preprocessing import Imputer

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=None)

imputer = Imputer(strategy="median")
imputer.fit(training_features)
training_features = imputer.transform(training_features)
testing_features = imputer.transform(testing_features)

# Average CV score on the training set was:-0.1470238507301496
exported_pipeline = XGBRegressor(learning_rate=0.1, max_depth=6, min_child_weight=3, n_estimators=100, nthread=1, objective="reg:squarederror", subsample=0.7000000000000001)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
