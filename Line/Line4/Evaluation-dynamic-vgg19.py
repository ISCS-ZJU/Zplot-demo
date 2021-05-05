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

xlabelTextSize = 7.5
ylabelTextSize = 7.5
xtitleTextSize = 9
ytitleTextSize = 9
legendTextSize = 8
NormalizedTextSize = 4

ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, 'Evaluation-dynamic-vgg19', dimensions=['4in', '2.3in'])

t = table(file='Vgg19-Evaluation-dynamic.data')

# print(min_value)

d = drawable(canvas=c, xrange=[0, 52],
             yrange=[4, 16])


axis(drawable=d, style='xy', ticstyle='in', dominortics=False,
     xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     xtitle='Epoch', ytitle='The number of compressed tensors',
     xlabelshift=[0,-3],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     xlabelrotate=25,
     ytitlesize=ytitleTextSize,
     linewidth=0.2, xauto=[0, 90, 0], yauto=['', '', 2],
     xmanual=[['0', 0],['5', 5],['10', 10], ['15', 15],['20', 20],['25', 25],['30', 30],['35', 35],['40', 40],['45', 45],['50', 50]]
     )

p = plotter()

L = legend()
L_line = legend()

series_list = ['num']
series_name = ['num']

# print 32 line


# print 64 line
for idx in range(len(series_list)):
    style = styles[idx][1]
    p.line(drawable=d, table=t, xfield='size', yfield=series_list[idx], linecolor='black',
               linewidth=0.6,legend=L_line,legendtext="the num of compressed layer")

    # p.points(drawable=d, table=t, xfield='size', yfield=series_list[idx], linecolor='black',
    #              linewidth=0.6, style=style, fill=False, fillcolor='black', size=2.5,
    #             legend=L, legendtext=series_name[idx])

grid(drawable=d, x=False, y=True, ystep=0.4,  yrange=[15,15],
    linedash=[1,1], linewidth=1, linecolor='black')
# L.draw(canvas=c, coord=[d.left()+30, d.top()-10], width=5, height=5, fontsize=8, skipnext=1, skipspace=55)
# L_line.draw(canvas=c, coord=[d.left()+27, d.top()-10], width=10, height=15, fontsize=8, skipnext=1, skipspace=55)


# ----- drawing circle


c.render()
