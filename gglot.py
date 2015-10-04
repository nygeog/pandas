retPlot_YTD = ggplot(data, aes('Date','Returns',color='Stocks')) \
+ geom_line(size=2.) \
+ geom_hline(yintercept=0, color='black', size=1.7, linetype='-.') \
+ scale_y_continuous(labels='percent') \
+ scale_x_date(labels='%b %d %y',breaks=date_breaks('week') ) \
+ theme_seaborn(style='whitegrid') \
+ ggtitle(('%s Cumulative Daily Return vs Peers_YTD') % key_Stock) 

fig = retPlot_YTD.draw()
ax = fig.axes[0]
offbox = ax.artists[0]
offbox.set_bbox_to_anchor((1, 0.5), ax.transAxes)
fig.show()

#http://stackoverflow.com/questions/23541497/is-there-a-way-to-plot-a-pandas-series-in-ggplot

