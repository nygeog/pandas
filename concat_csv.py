import pandas as pd
import glob
import csv

all_csvs = glob.glob(pt+exp)
df_list = []

for j in all_csvs:
	df = pd.read_csv(j)
	df_list.append(df)

df = pd.concat(df_list)