"""Train model and save checkpoint"""

import argparse
import logging
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from joblib import dump

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='log/train_model.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')

TRAIN_DATA = 'data/proc/train.csv'
MODEL_SAVE_PATH = 'models/ridge_regression_v01.joblib'


def main(args):
    df_train = pd.read_csv(TRAIN_DATA)
    x_train = df_train[['total_meters']]
    y_train = df_train['price']

    ridge_model = Ridge()
    ridge_model.fit(x_train, y_train)
    dump(ridge_model, args.model)
    logger.info(f'Saved to {args.model}')

    r2 = ridge_model.score(x_train, y_train)

    c = int(ridge_model.coef_[0])
    inter = int(ridge_model.intercept_)

    logger.info(f'R2 = {r2:.3f}  Price = {c} * area + {inter}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model', 
                        help='Model save path',
                        default=MODEL_SAVE_PATH)
    args = parser.parse_args()
    main(args)
