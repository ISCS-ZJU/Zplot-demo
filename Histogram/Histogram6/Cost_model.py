#! /usr/bin/env python

from zplot import *

xlabelTextSize = 8
ylabelTextSize = 8
xtitleTextSize = 9
ytitleTextSize = 9
legendTextSize = 8
NormalizedTextSize = 4

bartypes = [('solid', 1, 1),
            ('solid', 4, 5),
            ('dline1', 4, 5),
            ('dline2', 4, 5),
            ('dline1', 6, 3),
            # ('hline', 1, 2),
            ('hvline', 0.5, 2),
            ('circle', 1, 2),
            ('square', 1, 1),
            ('triangle', 2, 2),
            ('utriangle', 2, 2)]


# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='Cost_model', dimensions=['3.2in', '1.5in'])

t = table(file='Cost_model.data')

d = drawable(canvas=c, xrange=[-0.6, t.getmax('rownumber')+0.6],
             yrange=[0, 0.8])


axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='', ytitle='RAE', doylabels=True, ytitleshift=[0,-4],
         linewidth=0.5,
         xaxisposition=0, yauto=['','',0.2], xlabelrotate=0, xlabelshift=[0,0],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['Compression', 0], ['Decompression', 1]])


p = plotter()
L = legend()

# grid(drawable=d, x=False, y=True, ystep=0.15,  yrange=[0, 0.8],
#     linedash=[1,1], linewidth=0.5, linecolor='black')

series_list = ['Liner',  'Bayesian',  'Svm','Decision']
series_name = ['LR(CSwap)',  'BR',  'SVM', 'DT']
bgcolors    = ['white', 'white', 'white', 'darkgray', 'white', 'white', 'white']
fillcolors  = ['white', 'darkgray', 'black', 'black', 'black', 'black', 'black']


for i in range(len(series_list)):
    p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield=series_list[i],
               barwidth=0.75, yloval=0,
               linewidth=0.5, cluster =[i,len(series_list)], legend=L, legendtext=series_name[i],
               labelformat='%s samples/ms',labelrotate=0,labelsize=5,
               fill=True, 
               fillcolor=fillcolors[i], 
               # bgcolor=bgcolors[i],
               fillstyle=bartypes[i][0], fillsize=0.55, fillskip=bartypes[i][2])
#### legend
L.draw(canvas=c, coord=[d.left()+30, d.top()], skipnext=2, skipspace=85,
     hspace=4, fontsize=6,  width=6, height=6 )

c.render()
