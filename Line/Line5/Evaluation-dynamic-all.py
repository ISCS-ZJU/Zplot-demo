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

xlabelTextSize = 17
ylabelTextSize = 20
xtitleTextSize = 19
ytitleTextSize = 26
legendTextSize = 15
titleTextSize = 19
# NormalizedTextSize = 5
dimensionSize_w = 105
dimensionSize_h = 150
interval = 35
begin_ = 50
titleshift = -220
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, 'Evaluation-dynamic-all', dimensions=[600, 300]) # 50 * 30 * 30 * 30 *  = 400 + 150


#################################### alexnet
t1 = table(file='AlexNet-Evaluation-dynamic.data')
d1 = drawable(canvas=c, xrange=[0, 40], yrange=[0, 5], coord=[begin_,80], dimensions=[dimensionSize_w,dimensionSize_h] )

axis(drawable=d1, style='xy', ticstyle='out', dominortics=False,
     xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     title='(a) AlexNet',
     titlesize = titleTextSize,
     titleshift= [0, titleshift],
     xtitle='epoch', ytitle='Number of layers',
     ytitleshift=[-7, 0],
     xlabelshift=[0,-3],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     xlabelrotate=25,
     ytitlesize=ytitleTextSize,
     linewidth=0.2, xauto=[0, 90, 0], yauto=['', '', 1],
    #  xmanual=[['0', 0],['10', 10],['20', 20],['30', 30],['40', 40]]
     xmanual=[['0', 0],['10', 10],['20', 20],['30', 30],['40', 40]]
     )

p = plotter()
L = legend()
L_line = legend()

series_list = ['num']
series_name = ['num']

for idx in range(len(series_list)):
    style = styles[idx][1]
    p.line(drawable=d1, table=t1, xfield='size', yfield=series_list[idx], linecolor='black',
               linewidth=1,legend=L_line,legendtext="the num of compressed layer")

grid(drawable=d1, x=False, y=True, ystep=0.4,  yrange=[5,5],
    linedash=[1,1], linewidth=1, linecolor='black')



#################################### vgg16

t2 = table(file='Vgg16-Evaluation-dynamic.data')
d2 = drawable(canvas=c, xrange=[0, 50], yrange=[3, 12], coord=[begin_+dimensionSize_w+interval, 80], dimensions=[dimensionSize_w,dimensionSize_h])

axis(drawable=d2, style='xy', ticstyle='out', dominortics=False,
     xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     title='(b) Vgg16',
     titlesize = titleTextSize,
     xtitle='epoch',
     titleshift= [0, titleshift],
     xlabelshift=[0,-3],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     xlabelrotate=25,
     ytitlesize=ytitleTextSize,
     linewidth=0.2, xauto=[0, 90, 0], yauto=[3, 12, 3],
     xmanual=[['0', 0],['10', 10],['20', 20],['30', 30],['40', 40],['50', 50]]
     )

p = plotter()

L = legend()
L_line = legend()

series_list = ['num']
series_name = ['num']

for idx in range(len(series_list)):
    style = styles[idx][1]
    p.line(drawable=d2, table=t2, xfield='size', yfield=series_list[idx], linecolor='black',
               linewidth=1,legend=L_line,legendtext="the num of compressed layer")

grid(drawable=d2, x=False, y=True, ystep=0.4,  yrange=[12,12],
    linedash=[1,1], linewidth=1.4, linecolor='black')


#################################### mobilenet
t3 = table(file='MobileNet-Evaluation-dynamic.data')
d3 = drawable(canvas=c, xrange=[0, 50], yrange=[5, 25], coord=[begin_+(dimensionSize_w+interval)*2,80], dimensions=[dimensionSize_w,dimensionSize_h])

axis(drawable=d3, style='xy', ticstyle='out', dominortics=False,
     xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     title='(c) MobileNet',
     titlesize = titleTextSize,
     xtitle='epoch',
     titleshift= [0, titleshift],
     xlabelshift=[0,-3],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     xlabelrotate=25,
     ytitlesize=ytitleTextSize,
     linewidth=0.2, xauto=[0, 90, 0], yauto=[5, 25, 5],
     xmanual=[['0', 0],['10', 10], ['20', 20],['30', 30],['40', 40],['50', 50]]
     )

p = plotter()

L = legend()
L_line = legend()

series_list = ['num']
series_name = ['num']

for idx in range(len(series_list)):
    style = styles[idx][1]
    p.line(drawable=d3, table=t3, xfield='size', yfield=series_list[idx], linecolor='black',
               linewidth=1,legend=L_line,legendtext="the num of compressed layer")


grid(drawable=d3, x=False, y=True, ystep=0.4,  yrange=[25,25],
    linedash=[1,1], linewidth=1, linecolor='black')


#################################### squeezenet
t4 = table(file='squeezenet-Evaluation-dynamic.data')
d4 = drawable(canvas=c, xrange=[0, 50], yrange=[4, 16], coord=[begin_+(dimensionSize_w+interval)*3,80], dimensions=[dimensionSize_w,dimensionSize_h])

axis(drawable=d4, style='xy', ticstyle='out', dominortics=False,
     xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     title='(d) SqueezeNet',
     titlesize = titleTextSize,
     xtitle='epoch',
     titleshift= [0, titleshift],
     xlabelshift=[0,-3],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     xlabelrotate=25,
     ytitlesize=ytitleTextSize,
     linewidth=0.2, xauto=[0, 90, 0], yauto=['', '', 4],
     xmanual=[['0', 0],['10', 10], ['20', 20],['30', 30],['40', 40],['50', 50]]
     )
p = plotter()

L = legend()
L_line = legend()

series_list = ['num']
series_name = ['num']

for idx in range(len(series_list)):
    style = styles[idx][1]
    p.line(drawable=d4, table=t4, xfield='size', yfield=series_list[idx], linecolor='black',
               linewidth=1,legend=L_line,legendtext="the num of compressed layer")

    # p.points(drawable=d, table=t, xfield='size', yfield=series_list[idx], linecolor='black',
    #              linewidth=0.6, style=style, fill=False, fillcolor='black', size=2.5,
    #             legend=L, legendtext=series_name[idx])

grid(drawable=d4, x=False, y=True, ystep=0.4,  yrange=[16,16],
    linedash=[1,1], linewidth=1, linecolor='black')




c.render()