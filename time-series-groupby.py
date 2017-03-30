t = time_series.groupby([pd.TimeGrouper(freq='1w'), 'ZIPCODE']).count()
