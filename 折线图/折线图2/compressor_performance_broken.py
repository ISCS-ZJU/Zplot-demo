#! /usr/bin/env python


from zplot import *


styles = [
    ['black',         'circle',False],
    ['black',         'xline',False],
    ['black',         'triangle',False],
    ['black',         'square',False],
    ['blue',         'square',True],
    ['blue',         'square',False],
    ['red',         'circle',True],
    ['red',         'circle',False],
]

xlabelTextSize = 8.5
ylabelTextSize = 10
xtitleTextSize = 10
ytitleTextSize = 11
legendTextSize = 10
NormalizedTextSize = 4

ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, 'compressor_performance_broken', dimensions=['3.6in', '3in'])

t = table(file='compressor_performance_broken.data')

# print(min_value)

d = drawable(canvas=c, xrange=[25, 350+32],
             coord=[35, 60],
             yrange=[0, 19],
             dimensions=['3.2in', '0.6in'])

top_d = drawable(canvas=c,
                    coord=[35, 110],
                    xrange=[25, 350+32],
                    yrange=[20, 130],
                    dimensions=['3.2in', '0.7in'])

axis(drawable=d, style='xy', ticstyle='out', dominortics=False,
     xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     xtitle='Tensor size (MB)', ytitle='Computation time (ms)',
     xlabelshift=[0,-3],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     xlabelrotate=15,
     ytitleshift=[-5,28],
     ytitlesize=ytitleTextSize,
     linewidth=0.2, xauto=[0, 300, 0], yauto=['', '', 5],
     xmanual=[['50MB', 50],['100MB', 100], ['150MB', 150],['200MB', 200],['250MB', 250],['300MB', 300],['350MB', 350]]
     )

axis(drawable=top_d, style='y', ticstyle='out', dominortics=False,
     # xminorticcnt=0,
     doxminortics=False, yminorticcnt=0,
     # xtitle='Tensor size (MB)',
     # ytitle='Computation time (ms)',
     xlabelshift=[0,-3],
     # xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     # xlabelrotate=15,
     ytitlesize=ytitleTextSize,
     linewidth=0.2, yauto=[40, 130, 30],
     # xmanual=[['50MB', 50],['100MB', 100], ['150MB', 150],['200MB', 200],['250MB', 250],['300MB', 300],['350MB', 350]]
     )

c.text(coord= [35,102],text = '~',size = 9,)
c.text(coord= [35,107],text = '~',size = 9,)

p = plotter()
p1 = plotter()
L = legend()
L_line = legend()

series_list = ['CSR','ZVC','RLE']
series_name = ['CSR','ZVC','RLE']

# print 32 line

p.line(drawable=top_d, table=t, xfield='size', yfield='LZ4', linecolor='black',
               linewidth=0.8,legend=L_line)

p.points(drawable=top_d, table=t, xfield='size', yfield='LZ4', linecolor='black',
                 linewidth=0.8, style=styles[3][1], fill=False, fillcolor='black', size=2.5,
                legend=L, legendtext='LZ4')

# print 64 line
for idx in range(len(series_list)):
    style = styles[idx][1]
    p.line(drawable=d, table=t, xfield='size', yfield=series_list[idx], linecolor='black',
               linewidth=0.8,legend=L_line)

    p.points(drawable=d, table=t, xfield='size', yfield=series_list[idx], linecolor='black',
                 linewidth=0.8, style=style, fill=False, fillcolor='black', size=2.5,
                legend=L, legendtext=series_name[idx])


L.draw(canvas=c, coord=[d.left()+17, d.top()+66], width=5, height=5, fontsize=10, skipnext=1, skipspace=55, order=[3,1,0,2])
L_line.draw(canvas=c, coord=[d.left()+14, d.top()+66], width=10, height=15, fontsize=10, skipnext=1, skipspace=55, order=[3,1,0,2])


# ----- drawing circle


c.render()
