import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(figsize=(16, 8))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')
#ax.set_xticks_off()
#ax.set_yticks_off()

ax.set_xlim(-1, 15)
ax.set_ylim(0.5, 8.5)
ax.set_aspect('equal')

pn, pp, po, pg, pw = ax.opamp_l((8.5, 5), 'OPA1662')
gnd1 = ax.ground(pg.down(0.8), 'GND')
ax.connect((pg, gnd1))
npwr = ax.bus(pw.up(0.9), 'VDD', align='top')
ax.connect((pw, npwr))

ng1 = ax.node(pn.left(0.5).down(1.5))
r4l, r4r = ax.resistance_h(ng1.left(1), 'R4 10k', align='bottom')
ngr = ax.node(r4l.left(0.5))
nr = ax.bus(ngr.up(3.5), 'VREF', align='top')
ax.connect((pn, ng1, r4r, None, r4l, ngr, nr))
nr = ax.bus(ngr.down(1), 'VREF', align='bottom')
ax.connect((ngr, nr))

nc = ax.bus(pp.left(3.5).up(1), 'COMMON ', align='top')
ax.connect((nc,  pp))

ng2 = ax.node(po.right(0.5))
r6l, r6r = ax.resistance_h(ng2.right(1.5), 'R6 1k', 'below')
ng3 = ax.node(r6r.right(1))
no = ax.pin(ng3.right(1), 'INxM', 'right')
ax.connect((po, ng2, r6l, None, r6r, ng3, no))

r5l, r5r = ax.resistance_h(ng1.right(1.5), 'R5 10k', 'below')
ax.connect((ng1, r5l, None, r5r, ng2))

r7b, r7t = ax.resistance_v(ng3.down(1.5), 'R7 110k', 'right')
gnd2 = ax.ground(r7b.down(1), 'GND')
ax.connect((ng3, r7t, None, r7b, gnd2))

fig.savefig()
plt.show()

