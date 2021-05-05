#! /usr/bin/env python

from zplot import *


bartypes = [('dline1', 1, 6),
            ('solid', 1, 0.7),
            ('hvline', 1, 1),
            ('dline1', 1, 2),
            # ('hline', 1, 2),
            ('hvline', 0.5, 2),
            ('circle', 1, 2),
            ('square', 1, 1),
            ('triangle', 2, 2),
            ('utriangle', 2, 2)]


# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='Evaluation_BO', dimensions=['3.2in', '1.5in'])

t = table(file='Evaluation_BO.data')

d = drawable(canvas=c, xrange=[-0.6, t.getmax('rownumber')+0.2],
             yrange=[0, 1000])


axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='', ytitle='Time (ms)', doylabels=True, ytitleshift=[0,0],
         linewidth=0.5,
         xaxisposition=0.5, yauto=['','',200], xlabelrotate=0, xlabelshift=[-9,0],
         xlabelfontsize=8,
         ylabelfontsize=8,
         xtitlesize=9,
         ytitlesize=9,
         xmanual=[['RD', 0], ['EP', 1],
                  ['BO', 2],    ['GS', 3]])


p = plotter()
L = legend()

grid(drawable=d, x=False, y=True, ystep=0.5,  yrange=[1, 1.5],
    linedash=[1,1], linewidth=0.5, linecolor='black')

series_list = ['Time']
series_name = ['Time']
bgcolors    = ['white', 'white', 'white', 'white', 'white', 'white', 'white']
fillcolors  = ['gray', 'black', 'darkgray', 'black', 'black', 'black', 'black']


# p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield=series_list[0],
#                barwidth=0.5, yloval=0.5,
#                linewidth=0.5, cluster =[0,1], legend=L, legendtext=series_name[0],
#                labelformat='%s samples/ms',labelrotate=0,labelsize=5,
#                fill=True, fillcolor=fillcolors[0], bgcolor=bgcolors[0],
#                fillstyle=bartypes[0][0], fillsize=0.25, fillskip=bartypes[0][2])

barargs1 = {'drawable': d, 'table': t, 'xfield': 'rownumber',
           'linewidth': 0.5, 'fill': True, 'barwidth': 0.8,
           'legend': L, 'stackfields': [], 'cluster':[0,2]}


barargs1['yfield'] = 'others'
barargs1['legendtext'] = 'The remaining time'
barargs1['fillcolor'] = 'black'
barargs1['fill'] = 'True'
barargs1['fillsize'] = '0.7'
barargs1['fillskip'] = 7
barargs1['fillstyle'] = 'dline1'
p.verticalbars(**barargs1)

barargs1['stackfields'].append(barargs1['yfield'])

barargs1['yfield'] = 'compression'
barargs1['legendtext'] = 'Compression and decompression time'
barargs1['fillcolor'] = 'white'
barargs1['fill'] = 'True'
barargs1['fillsize'] = '0.55'
barargs1['fillstyle'] = 'solid'

p.verticalbars(**barargs1)

#### legend
L.draw(canvas=c, coord=[d.left()+55, d.top()-1], skipnext=3, skipspace=55,
     hspace=4, fontsize=6,  width=6, height=6 )

c.render()
