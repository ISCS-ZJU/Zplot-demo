#! /usr/bin/env python

from zplot import *

xlabelTextSize = 7
ylabelTextSize = 8
xtitleTextSize = 9
ytitleTextSize = 9

bartypes = [('hline', 1, 1),
            ('hvline', 1, 0.7),
            ('solid', 1, 1),
            ('dline1', 1, 2),
            # ('dline2', 1, 2),
            ('solid', 0.5, 2),
            ('circle', 1, 2),
            ('square', 1, 1),
            ('triangle', 2, 2),
            ('utriangle', 2, 2)]

# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='Vgg16-sparsity', dimensions=['3.4in', '1.9in'])

t = table(file='Vgg16-sparsity.data')

d = drawable(canvas=c, xrange=[-0.8, t.getmax('rownumber')+0.8],
             yrange=[0, 100])


axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=False, doymajortics=True,
         dominortics =True,  doxminortics =False,
         xminorticcnt=0, yminorticcnt=1,
         xtitle='', ytitle='Sparsity ratio (%)', doylabels=True,
         linewidth=0.7,
         xtitleshift  = [0,-3],
         xaxisposition=0, yauto=['','',20], xlabelrotate=30, xlabelshift=[-1, -1],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['ReLU1', 0], ['MAX1', 1], ['ReLU2', 2], ['MAX2', 3], ['ReLU3', 4],
                  ['ReLU4', 5], ['MAX3', 6], ['ReLU5', 7], ['ReLU6', 8], ['MAX4', 9], ['ReLU7', 10],
                  ['ReLU8', 11]])


p = plotter()
L = legend()

grid(drawable=d, x=False, y=True, ystep=20,  yrange=[20, 80],
    linedash=[1,1], linewidth=0.3, linecolor='black')

series_list = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']
bgcolors    = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
fillcolors  = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']

for i in range(len(series_list)):
    p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield=series_list[i],
               barwidth=0.8, yloval=0,
               linewidth=0.35, cluster =[i,len(series_list)], legend="", legendtext="",
               labelrotate=0, labelsize=1,
               fill=True, fillcolor=fillcolors[i], bgcolor=bgcolors[i],
               fillsize=0.15)



#### legend
L.draw(canvas=c, coord=[d.left()+100, d.top()-10], skipnext=2, skipspace=55,
     hspace=4, fontsize=7,  width=6, height=12 )

c.render()
