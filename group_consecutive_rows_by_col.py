df['block'] = (df.in_rdp.shift(1) != df.in_rdp).astype(int).cumsum()


#http://stackoverflow.com/questions/14358567/finding-consecutive-segments-in-a-pandas-data-frame