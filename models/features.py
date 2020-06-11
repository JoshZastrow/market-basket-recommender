import pandas as pd
import numpy as np

class UserProduct:
    '''Defines transformation functions for users and products'''
    
    @staticmethod
    def purchase_frequency(df):
    '''Calculate expanding frequency of a product purchase over user lifetime. First order frequency set to zero'''
        return (
            pd.crosstab(
                index=[df.order_number, df.order_id], 
                columns=df.product_id, 
                values=df.days_since_prior_order, 
                aggfunc=lambda x: x.sum(),
            )
            .expanding()
            .agg(lambda x: x.count() / x.shape[0])
            .reset_index()
            .melt(id_vars=['order_id', 'order_number'], value_name='frequency')
            .assign(frequency=lambda x: np.where(x.order_number > 1, x.frequency, 0))
            .drop('order_number', axis=1)
            .set_index(['product_id', 'order_id'])
        )