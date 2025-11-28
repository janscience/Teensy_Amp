import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(figsize=(16, 6))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')

pn, pp, po, pg, pw = ax.opamp_l((8, 5), 'OPA1662')
gnd1 = ax.ground(pg.down(0.7), 'GND')
ax.connect((pg, gnd1))
npwr = ax.node(pw.up(1), 'VDD')
ax.connect((pw, npwr))

ng1 = ax.node(pn.left(1))
r1l, r1r = ax.resistance_h(ng1.left(1.5), 'R3 10k', align='bottom')
nn = ax.node(r1l.left(0.5).up(1.95), 'COMMON', align='right')
ax.connect((nn, r1l, None, r1r, ng1, pn))

np = ax.node(pp.left(1.5).up(1.3), 'VREF', align='right')
ax.connect((np,  pp))

ng2 = ax.node(po.right(1.5))
no = ax.node(ng2.right(1), 'M', 'right')
ax.connect((po, ng2, no))

r5l, r5r = ax.resistance_h(po.left(0.5).down(2), 'R4 10k', 'below')
ax.connect((ng1, r5l, None, r5r, ng2))

ax.set_xlim(-1.5, 12)
ax.set_ylim(2.5, 7)
ax.set_aspect('equal')
fig.savefig()
plt.show()

