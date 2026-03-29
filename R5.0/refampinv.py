import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(figsize=(16, 6))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')
#ax.set_xticks_off()
#ax.set_yticks_off()

ax.set_xlim(-1.5, 12)
ax.set_ylim(2.5, 7.5)
ax.set_aspect('equal')

pn, pp, po, pg, pw = ax.opamp_l((8, 5), 'OPA1662')
gnd1 = ax.ground(pg.down(0.6), 'GND')
ax.connect((pg, gnd1))
npwr = ax.bus(pw.up(0.5), 'VDD', align='top')
ax.connect((pw, npwr))

ng1 = ax.node(pn.left(0.5))
r4l, r4r = ax.resistance_h(ng1.left(1), 'R4 10k', align='bottom')
nc = ax.bus(r4l.left(1.5).up(2), 'VCOM', align='north')
ax.connect((nc, r4l, None, r4r, ng1, pn))

npr = ax.node(pp.left(2.5))
nr1 = ax.bus(npr.up(1), 'VREF', align='north')
ax.connect((nr1,  npr, pp))
nr2 = ax.bus(npr.down(2), 'VREF', align='south')
ax.connect((nr2,  npr))

ng2 = ax.node(po.right(0.5))
no = ax.pin(ng2.right(1), 'INxM', 'right')
ax.connect((po, ng2, no))

r5l, r5r = ax.resistance_h(po.left(0.5).down(2), 'R5 10k', 'below')
ax.connect((ng1, r5l, None, r5r, ng2))

fig.savefig()
plt.show()

