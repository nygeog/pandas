df_trim['hn_rnd2'] = df_trim.MATCH_ADDR.str.split(' ',1).str[0]
df_trim['street_rnd2'] = (df_trim.MATCH_ADDR.str.split(',',1).str[0]).str.split(' ',1).str[1]


df['latitude'] = df.return_address_str.str.split('*',2).str[1]
df['longitude'] = df.return_address_str.str.split('*',2).str[2]