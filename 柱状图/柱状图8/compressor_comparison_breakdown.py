#! /usr/bin/env python

from zplot import *

xlabelTextSize = 8.5
ylabelTextSize = 10
xtitleTextSize = 10
ytitleTextSize = 10
legendTextSize = 10
NormalizedTextSize = 4

PointSize = 3

bartypes = [('solid', 1, 1),
            ('hline', 1, 1),
            ('dline1', 1, 1),
            ('dline2', 1, 2),
            ('dline2', 0.5, 2),
            ('solid', 0.5, 2),
            ('circle', 1, 2),
            ('square', 1, 1),
            ('triangle', 2, 2),
            ('utriangle', 2, 2)]

# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='compressor_comparison_breakdown', dimensions=['3.2in', '2.2in'])

t1 = table(file='ZVC_breakdown-1.data')
t2 = table(file='RLE_comparison_breakdown-2.data')
t3 = table(file='CSR_comparison_breakdown-3.data')
t4 = table(file='LZ4_comparison_breakdown-4.data')

d = drawable(canvas=c, xrange=[-0.7, 6.7],
             yrange=[0, 160])

axis(drawable=d, style='xy', ticstyle='out',
         doxmajortics=False, doymajortics=True,
         dominortics = True, doxminortics =False,
         xminorticcnt=0, yminorticcnt=1,
         ytitle='Time (ms)', doylabels=True,xtitle='Tensor size (MB)',
         linewidth=0.8,
         xaxisposition=0, yauto=['','200',40], xlabelrotate=20,xlabelshift=[0, -3],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['50MB', 0], ['100MB', 1], ['150MB', 2], ['200MB', 3], ['250MB', 4],
                  ['300MB', 5], ['350MB', 6]])

p = plotter()
L = legend()



##########################################################

# draw the second cluster - "RLE" bars
##########################################################
barargs = {'drawable': d, 'table': t2, 'xfield': 'rownumber','legend':L,
           'linewidth': 0.5, 'fill': True, 'barwidth': 0.85,'stackfields': [], 'cluster':[0,4], 'labelsize':5, 'fillskip':1}

# transfer_time
barargs['yfield'] = 'op_time'
barargs['legendtext'] = 'RLE_CT'
barargs['fillcolor'] = 'black'
barargs['bgcolor'] = 'darkgray'
barargs['fill'] = 'True'
barargs['fillsize'] = '0.4'
barargs['fillskip'] = 2
barargs['fillstyle'] = bartypes[1][0]
# barargs['fillstyle'] = 'dline1'
p.verticalbars(**barargs)
barargs['stackfields'].append(barargs['yfield'])
# op_time
barargs['yfield'] = 'transfer_time'
barargs['legendtext'] = 'RLE_ST'
barargs['fillcolor'] = 'gray'
barargs['bgcolor'] = 'white'
barargs['fill'] = 'True'
barargs['fillsize'] = '0.5'
barargs['fillskip'] = 2.5
barargs['fillstyle'] = bartypes[3][0]
p.verticalbars(**barargs)

# draw the third cluster - "CSR" bars
##########################################################
barargs = {'drawable': d, 'table': t3, 'xfield': 'rownumber','legend':L,
           'linewidth': 0.5, 'fill': True, 'barwidth': 0.85,'stackfields': [], 'cluster':[1,4], 'labelsize':5}

# transfer_time
barargs['yfield'] = 'op_time'
barargs['legendtext'] = 'CSR_CT'
barargs['fillcolor'] = 'black'
barargs['bgcolor'] = 'darkgray'
barargs['fill'] = 'True'
barargs['fillsize'] = '0.55'
barargs['fillskip'] = 3
barargs['fillstyle'] = bartypes[2][0]
# barargs['fillstyle'] = 'dline1'
p.verticalbars(**barargs)
barargs['stackfields'].append(barargs['yfield'])
# op_time
barargs['yfield'] = 'transfer_time'
barargs['legendtext'] = 'CSR_ST'
barargs['fillcolor'] = 'gray'
barargs['bgcolor'] = 'white'
barargs['fill'] = 'True'
barargs['fillskip'] = 2
barargs['fillsize'] = '0.5'
barargs['fillstyle'] = 'hvline'
p.verticalbars(**barargs)



# draw the fourth cluster - "LZ4" bars
##########################################################
barargs = {'drawable': d, 'table': t4, 'xfield': 'rownumber','legend':L,
           'linewidth': 0.5, 'fill': True, 'barwidth': 0.85, 'stackfields': [], 'cluster':[2,4], 'labelsize':5}

# transfer_time
barargs['yfield'] = 'op_time'
barargs['legendtext'] = 'LZ4_CT'
barargs['fillcolor'] = 'black'
barargs['bgcolor'] = 'darkgray'
barargs['fill'] = 'True'
barargs['fillskip'] = 5
barargs['fillsize'] = '0.55'
barargs['fillstyle'] = bartypes[3][0]
# barargs['fillstyle'] = 'dline1'
p.verticalbars(**barargs)
barargs['stackfields'].append(barargs['yfield'])
# op_time
barargs['yfield'] = 'transfer_time'
barargs['legendtext'] = 'LZ4_ST'
barargs['fillcolor'] = 'gray'
barargs['bgcolor'] = 'white'
barargs['fill'] = 'True'

barargs['fillsize'] = '0.55'
barargs['fillskip'] = 4
barargs['fillstyle'] = bartypes[2][0]
p.verticalbars(**barargs)


# draw the fist cluster - "ZVC" bars
##########################################################
barargs = {'drawable': d, 'table': t1, 'xfield': 'rownumber','legend':L,
           'linewidth': 0.5, 'fill': True, 'barwidth': 0.85,'stackfields': [], 'cluster':[3,4]}

# transfer_time
barargs['yfield'] = 'op_time'
barargs['legendtext'] = 'ZVC_CT'
barargs['fillcolor'] = 'darkgray'
# barargs['fill'] = 'True'
barargs['bgcolor'] = 'white'
barargs['fillsize'] = '0.55'
barargs['fillstyle'] = bartypes[0][0]
# barargs['fillstyle'] = 'dline1'
p.verticalbars(**barargs)
barargs['stackfields'].append(barargs['yfield'])
# op_time
barargs['yfield'] = 'transfer_time'
barargs['legendtext'] = 'ZVC_ST'
barargs['bgcolor'] = 'white'
barargs['fillcolor'] = 'white'
barargs['fill'] = 'True'
barargs['fillsize'] = '0.55'
barargs['fillstyle'] = bartypes[0][0]
p.verticalbars(**barargs)

##########################################################


L.draw(canvas=c, coord=[d.left()+8, d.top()+1], skipnext=2, skipspace=40,
     hspace=4, fontsize=6.5,  width=4, height=4)
p1 = plotter()
c.render()
