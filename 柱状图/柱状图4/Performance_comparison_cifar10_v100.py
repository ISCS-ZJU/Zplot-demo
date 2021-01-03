#! /usr/bin/env python

from zplot import *


bartypes = [('utriangle', 1, 1),
            ('dline1', 1, 4),
            ('solid', 1, 1.5),
            ('solid', 1, 1),
            ('hvline', 0.5, 2),
            ('circle', 1, 2),
            ('square', 1, 1),
            ('triangle', 2, 2),
            ('utriangle', 2, 2)]



# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='Performance_comparison_cifar10_v100', dimensions=['3.2in', '1.6in'])

t = table(file='Performance_comparison_cifar10_v100.data')

d = drawable(canvas=c, xrange=[-0.8, t.getmax('rownumber')+0.8],
             yrange=[0.2, 1.8])


axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='', ytitle='Normalized throughput', doylabels=True,ytitleshift=[0,0],
         linewidth=0.5,
         xaxisposition=0.2, yauto=['','',0.4], xlabelrotate=20,xlabelshift=[0,-4],
         xlabelfontsize=7,
         ylabelfontsize=7,
         xtitlesize=8,
         ytitlesize=8,
         xmanual=[['AlexNet', 0], ['Vgg16', 1],
                 ['Plain20', 2],['MobileNet', 3],
                   ['ResNet', 4],['SqueezeNet', 5]])


p = plotter()
L = legend()
L_line = legend()

# grid(drawable=d, x=False, y=True, ystep=0.4,  yrange=[0.2, 1.5],
#     linedash=[1,1], linewidth=0.3, linecolor='black')

series_list = ['vDNN','VDNN_plus','CSwap_average','Oracular']
series_name = ['vDNN','vDNN++','CSwap','Orac']
bgcolors    = ['white', 'white', 'gray', 'darkgray', 'white', 'white', 'white']
fillcolors  = ['white', 'black', 'gray', 'black', 'black', 'black', 'black']

for i in range(len(series_list)):
    p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield=series_list[i],
               barwidth=0.75, yloval=0.2,
               linewidth=0.5, cluster =[i,len(series_list)], legend=L, legendtext=series_name[i],
               labelformat='%s samples/ms',labelrotate=0,labelsize=5,
               fill=True, fillcolor=fillcolors[i], bgcolor=bgcolors[i],
               fillstyle=bartypes[i][0], fillsize=0.55, fillskip=bartypes[i][2])

# max line
# p.line(drawable=d, table=t, xfield='rownumber', yfield='CSwap_max', linecolor='black',
#                linewidth=0.6,legend=L_line)
#
# p.points(drawable=d, table=t, xfield='rownumber', yfield='CSwap_max', linecolor='black',
#                  linewidth=0.7, style='circle', fill=False, fillcolor='black', size=0.8,
#                 legend=L, legendtext='CSwap max')



#### text for each normalized throughput.
x_start = 11.5
x_step = 27.2
y_start = 34
real_throughput = [76.98788504, 4.428835874, 1.77819516, 2.223971283, 1.638805899, 3.837822036]

for i in range(len(real_throughput)):
   x_text = "%.2f S/ms" %  (real_throughput[i])
   c.text(coord=[d.left()+x_start+i*x_step, d.bottom()+y_start], rotate=90,
         text=x_text, size=5.5, anchor='l,h')


#### legend
L.draw(canvas=c, coord=[d.left()+5.5, d.top()+4], skipnext=1, skipspace=48,
     hspace=4, fontsize=7,  width=6, height=6 )
L_line.draw(canvas=c, coord=[d.left()+118, d.top()-9], width=10, height=15, fontsize=8, skipnext=1, skipspace=55)

c.render()
