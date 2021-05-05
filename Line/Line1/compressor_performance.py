#! /usr/bin/env python


from zplot import *


styles = [
    ['black',         'circle',False],
    ['black',         'square',False],
    ['black',         'xline',False],
    ['black',         'plusline',False],
    ['blue',         'square',True],
    ['blue',         'square',False],
    ['red',         'circle',True],
    ['red',         'circle',False],
]

xlabelTextSize = 8.5
ylabelTextSize = 10
xtitleTextSize = 10
ytitleTextSize = 10
legendTextSize = 10
NormalizedTextSize = 4

ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, 'compressor_performance', dimensions=['3.2in', '2.2in'])

t = table(file='compressor_performance.data')

# print(min_value)

d = drawable(canvas=c, xrange=[25, 350+25],
             yrange=[0, 20])


axis(drawable=d, style='xy', ticstyle='out', dominortics=False,
     xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     xtitle='Tensor size (MB)', ytitle='Computation time (ms)',
     xlabelshift=[0,-3],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     xlabelrotate=15,
     ytitlesize=ytitleTextSize,
     linewidth=0.2, xauto=[0, 300, 0], yauto=['', '', 4],
     xmanual=[['50MB', 50],['100MB', 100], ['150MB', 150],['200MB', 200],['250MB', 250],['300MB', 300],['350MB', 350]]
     )

p = plotter()

L = legend()
L_line = legend()

series_list = ['CSR','ZVC','RLE']
series_name = ['CSR','ZVC','RLE']

# print 32 line


# print 64 line
for idx in range(len(series_list)):
    style = styles[idx][1]
    p.line(drawable=d, table=t, xfield='size', yfield=series_list[idx], linecolor='black',
               linewidth=0.8,legend=L_line)

    p.points(drawable=d, table=t, xfield='size', yfield=series_list[idx], linecolor='black',
                 linewidth=0.8, style=style, fill=False, fillcolor='black', size=2.5,
                legend=L, legendtext=series_name[idx])


L.draw(canvas=c, coord=[d.left()+17, d.top()-3], width=5, height=5, fontsize=9, skipnext=1, skipspace=55, order=[0,2,1])
L_line.draw(canvas=c, coord=[d.left()+14, d.top()-3], width=10, height=15, fontsize=9, skipnext=1, skipspace=55, order=[0,2,1])


# ----- drawing circle


c.render()
