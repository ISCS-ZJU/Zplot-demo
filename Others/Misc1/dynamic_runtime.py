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

c = canvas(ctype, title='dynamic_runtime', dimensions=['3.4in', '2.1in'])

t = table(file='dynamic_runtime.data')
t_without = table(file="dynamic_runtime_without.data")
d = drawable(canvas=c, xrange=[-0.5, 8.4],
             yrange=[0, 6.8])

# Vgg16 runtime compression situation
axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=True, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='Epoch', ytitle='Layers', doylabels=True, ytitleshift=[0,-2],
         linewidth=0.5,
         xaxisposition=0, yauto=['','',0.4], xlabelrotate=0, xlabelshift=[0,-0.3],
         xlabelfontsize=8,
         ylabelfontsize=6.5,
         xtitlesize=9,
         ytitlesize=9,
         ymanual=[['ReLU1', 0.5], ['MAX1', 1], ['ReLU2', 1.5], ['MAX2', 2], ['ReLU3', 2.5], ['ReLU4', 3], ['MAX3', 3.5], ['ReLU5', 4], ['ReLU6', 4.5], ['MAX4', 5], ['ReLU7', 5.5], ['ReLU8', 6]],
         xmanual=[['0', 0],['3', 0.5], ['6', 1], ['9', 1.5], ['12', 2], ['15', 2.5], ['18', 3], ['21', 3.5], ['24', 4], ['27', 4.5], ['30', 5], ['33', 5.5], ['36', 6], ['39', 6.5], ['42', 7], ['45', 7.5], ['48', 8]]


     )


p = plotter()
L = legend()

# compression
p.points(drawable=d, table=t, xfield='Serie', yfield="compression", linecolor='black',
                 linewidth=0.3, style="circle", fill=True, fillcolor='black', size=3.2,
                legend=L, legendtext="With compression")



# non_compression
p.points(drawable=d, table=t_without, xfield='Serie', yfield="compression", linecolor='gray',
                 linewidth=0.3, style="circle", fill=True, fillcolor='white', size=3.2,
                legend=L, legendtext="Without compression")
# #### legend
L.draw(canvas=c, coord=[d.left()+23, d.top()-3], skipnext=1, skipspace=74,
     hspace=4, fontsize=7,  width=6, height=6 )

c.render()
