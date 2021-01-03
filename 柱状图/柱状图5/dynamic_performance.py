#! /usr/bin/env python

from zplot import *


bartypes = [('dline2', 1, 2),
            ('solid', 1, 0.7),
            ('dline1', 1, 1),
            ('solid', 7, 0.7),
            ('dline1', 6, 3),
            # ('hline', 1, 2),
            ('hvline', 0.5, 2),
            ('circle', 1, 2),
            ('square', 1, 1),
            ('triangle', 2, 2),
            ('utriangle', 2, 2)]


# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='dynamic_performance', dimensions=['3.4in', '1.8in'])

t = table(file='dynamic_performance.data')

d = drawable(canvas=c, xrange=[-0.6, t.getmax('rownumber')+0.6],
             yrange=[0, 13])


axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='', ytitle='Performance improvement (%)', doylabels=True, ytitleshift=[0,-5],
         linewidth=0.5,
         xaxisposition=0, yauto=['','',2], xlabelrotate=18, xlabelshift=[0,-3.5],
         xlabelfontsize=9,
         ylabelfontsize=9,
         xtitlesize=9,
         ytitlesize=8.5,
         xmanual=[['AlexNet', 0], ['Vgg16', 1], ['Vgg19', 2],['Plain20', 3],['MobileNet', 4], ['ResNet', 5], ['SqueezeNet', 6]])


p = plotter()
L = legend()

# grid(drawable=d, x=False, y=True, ystep=0.15,  yrange=[0, 0.8],
#     linedash=[1,1], linewidth=0.5, linecolor='black')

series_list = ['CIFAR10_V100','CIFAR10_2080Ti']
series_name = ['V100','2080Ti']
bgcolors    = ['white', 'white', 'white', 'white', 'white', 'white', 'white']
fillcolors  = ['darkgray', 'darkgray', 'darkgray', 'gray', 'black', 'black', 'black']


for i in range(len(series_list)):
    p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield=series_list[i],
               barwidth=0.58, yloval=0,
               linewidth=0.5, cluster =[i,len(series_list)], legend=L, legendtext=series_name[i],
               labelformat='%s samples/ms',labelrotate=0,labelsize=5,
               fill=True, fillcolor=fillcolors[i], bgcolor=bgcolors[i],
               fillstyle=bartypes[i][0], fillsize=0.55, fillskip=bartypes[i][2])
#### legend
L.draw(canvas=c, coord=[d.left()+45, d.top()-1], skipnext=1, skipspace=80,
     hspace=4, fontsize=9,  width=6, height=6 )

c.render()
