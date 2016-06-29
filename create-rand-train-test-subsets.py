msk = np.random.rand(len(df)) < 0.8 
#http://stackoverflow.com/questions/24147278/how-do-i-create-test-and-train-samples-from-one-dataframe-with-pandas
train = df[msk]
test = df[~msk]

print len(test)

print len(train)