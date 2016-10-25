df['sequence']=df.groupby('patient').cumcount()
#http://stackoverflow.com/questions/29353096/add-a-sequence-number-to-each-element-in-a-group-using-python