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
        self.orders = pd.read_csv(dataframes['orders'])
        self.departments = pd.read_csv(dataframes['departments'])
        self.products = pd.read_csv(dataframes['products'])
        self.opt = pd.read_csv(dataframes['order-products-train'])
        self.opp = pd.read_csv(dataframes['order-products-prior'])
        self.sample = pd.read_csv(dataframes['sample-submission'])
        
        self.next(self.end)
        
    @step
    def end(self):
        """Completion message"""
        print('Data Downloaded!')
        
if __name__ == '__main__':
    BaselineModel()
    