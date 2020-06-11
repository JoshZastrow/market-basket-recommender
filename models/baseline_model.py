from metaflow import Metaflow, FlowSpec, step, Parameter, Flow, current
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import joblib
import numpy as np
from sspipe import p

from utils import download_data
from dotenv import load_dotenv, find_dotenv

find_dotenv() | p(load_dotenv)

if not os.getenv('APP_DIRECTORY'):
    raise EnvironmentError('.env file not created. Please read Getting Started.')
    
APP_DIRECTORY = os.getenv('APP_DIRECTORY')

from features import UserProduct

class BaselineModel(FlowSpec):
    datasets = [
        'aisles', 
        'orders', 
        'departments', 
        'products', 
        'order-products-train', 
        'order-products-prior', 
        'sample-submission'
    ]
    
    @step
    def start(self):
        """Loads data from Kaggle"""
        dataframes = download_data(APP_DIRECTORY)
        
        self.aisles = pd.read_csv(dataframes['aisles'])
#         self.orders = pd.read_csv(dataframes['orders'])
#         self.departments = pd.read_csv(dataframes['departments'])
#         self.products = pd.read_csv(dataframes['products'])
        self.order_products_train = pd.read_csv(dataframes['order-products-train'])
        self.order_products_prior = pd.read_csv(dataframes['order-products-prior'])
        self.sample = pd.read_csv(dataframes['sample-submission'])
        
        self.next(self.create_features)
        
    @step
    def create_features(self):
        self.df = pd.merge(
                self.orders,
                self.order_products_prior, 
                left_on='order_id', 
                right_on='order_id',
            )
            
        self.features = (
            self.df
            .groupby('user_id')
            .apply(UserProduct.purchase_frequency)
        )
        
        self.target = (
            self.df
            .set_index(['user_id', 'order_id', 'product_id'])
            .loc[:, 'reordered']
        )
        
        self.next(self.end)
        
    @step
    def end(self):
        """Completion message"""
        print('Feature Created!')
        
if __name__ == '__main__':
    BaselineModel()
    