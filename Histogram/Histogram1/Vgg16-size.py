#! /usr/bin/env python

from zplot import *


bartypes = [('dline1', 1, 4),
            ('utriangle', 1, 1),
            ('solid', 1, 1.5),
            ('solid', 1, 1),
            ('hvline', 0.5, 2),
            ('circle', 1, 2),
            ('square', 1, 1),
            ('triangle', 2, 2),
            ('utriangle', 2, 2)]

# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='Vgg16-size', dimensions=['3.2in', '1.7in'])

t = table(file='Vgg16-size.data')

d = drawable(canvas=c, xrange=[-1, t.getmax('rownumber')+1],
             yrange=[0, 1600])


axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=False, doymajortics=True,
         dominortics =True,  doxminortics =False,
         xminorticcnt=0, yminorticcnt=1,
         xtitle='', ytitle='Tensor size (MB)', doylabels=True,
         linewidth=0.7,
         xtitleshift  = [0,-3],
         xaxisposition=0, yauto=['','',400], xlabelrotate=25, xlabelshift=[-1, -2],
         xlabelfontsize=7,
         ylabelfontsize=8,
         xtitlesize=9,
         ytitlesize=9,
         xmanual=[['ReLU1', 0], ['MAX1', 1], ['ReLU2', 2], ['MAX2', 3], ['ReLU3', 4],
                  ['ReLU4', 5], ['MAX3', 6], ['ReLU5', 7], ['ReLU6', 8], ['MAX4', 9], ['ReLU7', 10],
                  ['ReLU8', 11]])


p = plotter()
L = legend()

# grid(drawable=d, x=False, y=True, ystep=20,  yrange=[20, 80],
#     linedash=[1,1], linewidth=0.3, linecolor='black')

series_list = ['ImageNet_128_MB']
series_name = ['E1I1', 'E1I15', 'E40I1', 'E40I15']
bgcolors    = ['white', 'white', 'gray', 'darkgray', 'white', 'white', 'white']
fillcolors  = ['black', 'black', 'gray', 'black', 'black', 'black', 'black']

for i in range(len(series_list)):
    p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield=series_list[i],
               barwidth=0.6, yloval=0,
               linewidth=0.5, cluster =[i,len(series_list)], legend=L, legendtext=series_name[i],
               labelrotate=0, labelsize=1,
               fill=True,
               fillcolor=fillcolors[i],
#               bgcolor=bgcolors[i],
               fillstyle=bartypes[i][0],
               fillskip=5,
               fillsize=0.25)


#### legend
# L.draw(canvas=c, coord=[d.left()+70, d.top()-5], skipnext=2, skipspace=50,
#      hspace=2, fontsize=8,  width=5, height=8 )

c.render()
