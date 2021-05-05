#! /usr/bin/env python

from zplot import *

legendTextSize = 8
NormalizedTextSize = 4
PointSize = 3

bartypes = [('hline', 0.5, 1),
            ('hvline', 0.5, 1),
            ('solid', 1, 1),
            ('dline1', 0.5, 2),
            ('dline2', 0.5, 2),
            ('solid', 0.5, 2),
            ('circle', 1, 2),
            ('square', 1, 1),
            ('triangle', 2, 2),
            ('utriangle', 2, 2)]

# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='dynamic-motivation-breakdown', dimensions=['3.2in', '1.7in'])

t = table(file='dynamic-motivation-breakdown-1.data')
t2 = table(file='dynamic-motivation-breakdown-2.data')
t_zoom1 = table(file='dynamic-motivation-breakdown-zoom1.data')
t_zoom2 = table(file='dynamic-motivation-breakdown-zoom2.data')


d = drawable(canvas=c, xrange=[-1, 12],
             yrange=[0, 180])

axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=False, doymajortics=True,
         dominortics = True, doxminortics =False,
         xminorticcnt=0, yminorticcnt=1,
         xtitle='', ytitle='Time (ms)', doylabels=True,
         linewidth=0.7,
         xaxisposition=0, yauto=['','200',30], xlabelrotate=30,xlabelshift=[-1, -2],
         xlabelfontsize=7,
         ylabelfontsize=8,
         xtitlesize=9,
         ytitlesize=9,
         xmanual=[['ReLU1', 0], ['MAX1', 1], ['ReLU2', 2], ['MAX2', 3], ['ReLU3', 4],
                  ['ReLU4', 5], ['MAX3', 6], ['ReLU5', 7], ['ReLU6', 8], ['MAX4', 9],
                  ['ReLU7', 10], ['ReLU8', 11]])

p = plotter()
L = legend()
L2 = legend()

# draw the fist cluster - "No compression" bars
##########################################################
barargs = {'drawable': d, 'table': t, 'xfield': 'rownumber',
           'linewidth': 0.5, 'fill': True, 'barwidth': 0.7,
           'legend': L, 'stackfields': [], 'cluster':[0,2]}

# search node bar
barargs['yfield'] = 'No_compression_transfer'
barargs['legendtext'] = 'W/O compression'
barargs['fillcolor'] = 'black'
barargs['fill'] = 'True'
barargs['fillsize'] = '0.55'
barargs['fillstyle'] = 'dline1'
# barargs['fillstyle'] = bartypes[0][0]
p.verticalbars(**barargs)
barargs['stackfields'].append(barargs['yfield'])
##########################################################

# draw the second cluster - "No compression" bars
##########################################################
barargs = {'drawable': d, 'table': t2, 'xfield': 'rownumber',
           'linewidth': 0.5, 'fill': True, 'barwidth': 0.7,
           'legend': L2, 'stackfields': [], 'cluster':[1,2], 'labelsize':5}

# SC swapping time/computing time bar

barargs['yfield'] = 'Static_compression_compute_or_transfer'
barargs['legendtext'] = 'Data transfer'
barargs['fillcolor'] = 'gray'
barargs['fill'] = 'True'
barargs['fillsize'] = '0.55'
barargs['fillstyle'] = 'solid'
# barargs['fillstyle'] = bartypes[1][0]
p.verticalbars(**barargs)
barargs['stackfields'].append(barargs['yfield'])


# Operation time bar

barargs['yfield'] = 'Static_compression_operator'
barargs['legendtext'] = 'Data compression and decompression'
barargs['fillcolor'] = 'white'
barargs['fill'] = 'True'
barargs['fillsize'] = '0.55'
barargs['fillstyle'] = 'solid'

# barargs['fillstyle'] = bartypes[0][0]
p.verticalbars(**barargs)


##########################################################



#### added boxes for some bars
# c.box(coord=d.map([[0.5,38],[1.5,0]]), linecolor='red', linewidth=0.5)
c.box(coord=d.map([[2.5,41],[3.5,-4]]), linecolor='black', linewidth=0.5, linedash=[2,2],
         fill=False)
c.box(coord=d.map([[5.5,21],[6.5,-4]]), linecolor='black', linewidth=0.5, linedash=[2,2],
         fill=False)
c.box(coord=d.map([[8.5,23],[11.5,-4]]), linecolor='black', linewidth=0.5, linedash=[2,2],
         fill=False)



L.draw(canvas=c, coord=[d.left()+18, d.top()+11], skipnext=1, skipspace=46,
     hspace=4, fontsize=6,  width=4, height=4,order=[0,1,2])
L2.draw(canvas=c, coord=[d.left()+18, d.top()+4], skipnext=1, skipspace=115,
     hspace=4, fontsize=6,  width=4, height=4,order=[1,0,2])

# - - - - - - - - - - - - - - - - - - zoom
# - - - - - - - - - - - - - - - - - - zoom
# - - - - - - - - - - - - - - - - - - zoom
# - - - - - - - - - - - - - - - - - - zoom

zoom_d = drawable(canvas=c,
                    coord=[128, 61],
                    xrange=[-0.8, 5],
                    yrange=[0, 40],
                    dimensions=['1in','0.5in'])


axis(drawable=zoom_d, style='box', ticstyle='in',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         dominortics=True,
         xtitle='', ytitle='', doylabels=True,
         linewidth=0.5,
         xaxisposition=0, yauto=['','',8], xlabelrotate=0,xlabelshift=[0, 2],
         xlabelfontsize=4,
         ylabelfontsize=4,
         xtitlesize=4.6,
         ytitlesize=5,
         doxlabels=True,
         xmanual=[['MAX2', 0], ['MAX3', 1], ['MAX4', 2], ['ReLU7', 3], ['ReLU8', 4]])



p1 = plotter()


# draw the fist cluster - "No compression" bars
##########################################################
barargs1 = {'drawable': zoom_d, 'table': t_zoom1, 'xfield': 'rownumber',
           'linewidth': 0.5, 'fill': True, 'barwidth': 0.5,
           'legend': L, 'stackfields': [], 'cluster':[0,2]}

# search node bar
barargs1['yfield'] = 'No_compression_transfer'
barargs1['legendtext'] = 'NC swapping time'
barargs1['fillcolor'] = 'black'
barargs1['fill'] = 'True'
barargs1['fillsize'] = '0.55'
barargs1['fillstyle'] = 'dline1'
# barargs['fillstyle'] = bartypes[0][0]
p1.verticalbars(**barargs1)




barargs1['stackfields'].append(barargs1['yfield'])
##########################################################

# draw the second cluster - "No compression" bars
##########################################################
barargs1 = {'drawable': zoom_d, 'table': t_zoom2, 'xfield': 'rownumber',
           'linewidth': 0.5, 'fill': True, 'barwidth': 0.5,
           'legend': L, 'stackfields': [], 'cluster':[1,2], 'labelsize':5}

# SC swapping time/computing time bar

barargs1['yfield'] = 'Static_compression_compute_or_transfer'
barargs1['legendtext'] = 'Transfer time'
barargs1['fillcolor'] = 'gray'
barargs1['fill'] = 'True'
barargs1['fillsize'] = '0.55'
barargs1['fillstyle'] = 'solid'
# barargs['fillstyle'] = bartypes[1][0]
p1.verticalbars(**barargs1)
barargs1['stackfields'].append(barargs1['yfield'])


# Operation time bar

barargs1['yfield'] = 'Static_compression_operator'
barargs1['legendtext'] = 'Data compression and decompression'
barargs1['fillcolor'] = 'white'
barargs1['fill'] = 'True'
barargs1['fillsize'] = '0.55'
barargs1['fillstyle'] = 'solid'

p1.verticalbars(**barargs1)

# draw array
c.line(coord=d.map([[3,40.5],[5.7,58.5]]), linedash=[3,1],
            linewidth=0.6, linecolor='black', arrow=True,arrowheadwidth=2,arrowheadlength = 3)

c.line(coord=d.map([[6,19.5],[7,49]]), linedash=[3,1],
            linewidth=0.6, linecolor='black', arrow=True,arrowheadwidth=2,arrowheadlength = 3)

c.line(coord=d.map([[10,21.2],[9.5,48]]), linedash=[3,1],
            linewidth=0.6, linecolor='black', arrow=True,arrowheadwidth=2,arrowheadlength = 3)

c.render()
