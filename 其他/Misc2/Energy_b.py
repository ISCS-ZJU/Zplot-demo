#! /usr/bin/env python

from zplot import *


bartypes = [('dline1', 10, 8),
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

styles = [
    ['black',         'circle',True],
    ['black',         'square',False],
    ['black',         'xline',False],
    ['black',         'plusline',False],
    ['blue',         'square',True],
    ['blue',         'square',False],
    ['red',         'circle',True],
    ['red',         'circle',False],
]

# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='Energy_b', dimensions=['3in', '1.8in'])

t = table(file='Energy_b.data')
t2 = table(file='Energy_b_line.data')

d = drawable(canvas=c, xrange=[-0.5, 3.5],
             yrange=[0, 14],coord=[30,25],dimensions=['2.1in', '1.2in'])

d2 = drawable(canvas=c, xrange=[-0.5, 3.5],
             yrange=[0, 0.5],coord=[181,25],dimensions=[])

d3 = drawable(canvas=c, xrange=[-0.5, 3.5],
             yrange=[0, 0.5],coord=[30,25],dimensions=['2.1in', '1.2in'])

axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='', ytitle='Comparison Rate', doylabels=True, ytitleshift=[2,0],
         linewidth=0.5,
         xaxisposition=0, yauto=['','',2], xlabelrotate=18, xlabelshift=[0,0],
         xlabelfontsize=9,
         ylabelfontsize=9,
         xtitlesize=9,
         ytitlesize=9,
         xmanual=[['32x32', 0], ['64x64', 1], ['128x128', 2],['256x256', 3]])

axis(drawable=d2, style='y', ticstyle='in',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='', ytitle='Accuracy', doylabels=True, ytitleshift=[30,0],ylabelshift=[22,0],
         linewidth=0.5,
         xaxisposition=0, yauto=['','',0.1], xlabelrotate=18, xlabelshift=[0,0],
         xlabelfontsize=9,
         ylabelfontsize=9,
         xtitlesize=9,
         ytitlesize=9,
         xmanual=[['32x32', 0], ['64x64', 1], ['128x128', 2],['256x256', 3]])

axis(drawable=d3, style='y', ticstyle='out',
         doxmajortics=False, doymajortics=False,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='', ytitle='', doylabels=False, ytitleshift=[2,0],
         linewidth=0.5,
         xaxisposition=0, yauto=['','',0.1], xlabelrotate=18, xlabelshift=[0,0],
         xlabelfontsize=9,
         ylabelfontsize=9,
         xtitlesize=9,
         ytitlesize=9,
         xmanual=[['32x32', 0], ['64x64', 1], ['128x128', 2],['256x256', 3]])

p = plotter()
L = legend()
L_line = legend()
L_line_point = legend()
# grid(drawable=d, x=False, y=True, ystep=0.15,  yrange=[0, 0.8],
#     linedash=[1,1], linewidth=0.5, linecolor='black')

series_list = ['energy']
# series_name = ['']
bgcolors    = ['white', 'white', 'white', 'white', 'white', 'white', 'white']
fillcolors  = ['black', 'darkgSerieray', 'darkgray', 'gray', 'black', 'black', 'black']


for i in range(len(series_list)):
    p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield=series_list[i],
               barwidth=0.4, yloval=0,
               linewidth=0.5, cluster =[i,len(series_list)], legend=L, legendtext='',
               labelformat='%s samples/ms',labelrotate=0,labelsize=5,
               fill=True, fillcolor=fillcolors[i], bgcolor=bgcolors[i],
               fillstyle=bartypes[i][0], fillsize=0.55, fillskip=bartypes[i][1])


series_list_line = ['acc']
for idx in range(len(series_list_line)):
    style = styles[idx][1]
    p.line(drawable=d3, table=t2, xfield='Serie', yfield=series_list_line[idx], linecolor='black',
               linewidth=0.8,legend=L_line)

    p.points(drawable=d3, table=t2, xfield='Serie', yfield=series_list_line[idx], linecolor='black',
                 linewidth=0.8, style=style, fill=False, fillcolor='black', size=2.5,
                legend=L_line_point, legendtext='acc loss')

# L_line.draw(canvas=c, coord=[d.left()+27, d.top()], width=10, height=15, fontsize=8, skipnext=1, skipspace=55)
# L_line_point.draw(canvas=c, coord=[d.left()+29, d.top()], width=5.5, height=15, fontsize=8, skipnext=1, skipspace=55)
c.render()
