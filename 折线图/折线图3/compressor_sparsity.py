#! /usr/bin/env python


from zplot import *


styles = [
    ['black',         'triangle',False],
    ['black',         'circle',False],
    ['black',         'triangle',False],
    ['black',         'square',False],
    ['blue',         'square',True],
    ['blue',         'square',False],
    ['red',         'xline',True],
    ['red',         'circle',False],
]

xlabelTextSize = 8.5
ylabelTextSize = 10
xtitleTextSize = 10
ytitleTextSize = 10
legendTextSize = 10
NormalizedTextSize = 4

ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, 'compressor_sparsity', dimensions=['3.2in', '2.2in'])

t_others = table(file='compressor_sparsity_Others.data')
t_zvc_lz4 = table(file='compressor_sparsity_ZVC.data')
# print(min_value)

d = drawable(canvas=c, xrange=[25, 95],
             yrange=[0, 100])


axis(drawable=d, style='xy', ticstyle='out', dominortics=False,
     xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     xtitle='Tensor sparsity', ytitle='Compression ratio (%)',
     xlabelshift=[0,-3],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     xlabelrotate=0,
     ytitlesize=ytitleTextSize,
     linewidth=0.2, yauto=['', '', 20],
     xmanual=[['30%', 30],['40%', 40], ['50%', 50],['60%', 60],['70%', 70],['80%', 80],['90%', 90]]
     )

p = plotter()

L = legend()
L_line = legend()

series_list = ['RLE','CSR']
series_name = ['RLE','CSR']

# print 32 line


# print 64 line

p.line(drawable=d, table=t_zvc_lz4, xfield='sparsity', yfield='ZVC', linecolor='black',
               linewidth=0.8,legend=L_line)

p.points(drawable=d, table=t_zvc_lz4, xfield='sparsity', yfield='ZVC', linecolor='black',
                 linewidth=0.8, style='xline', fill=False, fillcolor='black', size=2.5,
                legend=L, legendtext='ZVC')


p.line(drawable=d, table=t_zvc_lz4, xfield='sparsity', yfield='LZ4', linecolor='black',
               linewidth=0.8,legend=L_line)

p.points(drawable=d, table=t_zvc_lz4, xfield='sparsity', yfield='LZ4', linecolor='black',
                 linewidth=0.8, style='square', fill=False, fillcolor='black', size=2.5,
                legend=L, legendtext='LZ4')

for idx in range(len(series_list)):
    style = styles[idx][1]
    p.line(drawable=d, table=t_others, xfield='sparsity', yfield=series_list[idx], linecolor='black',
               linewidth=0.8,legend=L_line)

    p.points(drawable=d, table=t_others, xfield='sparsity', yfield=series_list[idx], linecolor='black',
                 linewidth=0.8, style=style, fill=False, fillcolor='black', size=2.5,
                legend=L, legendtext=series_name[idx])






L.draw(canvas=c, coord=[d.left()+17, d.top()+10], width=5, height=5, fontsize=9, skipnext=1, skipspace=43,order=[2,3,1,0])
L_line.draw(canvas=c, coord=[d.left()+14, d.top()+10], width=10, height=15, fontsize=9, skipnext=1, skipspace=43,order=[2,3,1,0])


# ----- drawing circle


c.render()
