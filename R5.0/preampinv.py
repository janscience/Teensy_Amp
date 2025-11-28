import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(figsize=(16, 8))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')

pn, pp, po, pg, pw = ax.opamp_l((8, 5), 'OPA1662')
gnd1 = ax.ground(pg.down(0.7), 'GND')
ax.connect((pg, gnd1))
npwr = ax.node(pw.up(1), 'VDD')
ax.connect((pw, npwr))

ng1 = ax.node(pn.left(1))
r1l, r1r = ax.resistance_h(ng1.left(1.5), 'R3 10k', align='bottom')
n4 = ax.node(r1l.left(1.5))
c1l, c1r = ax.capacitance_h(n4.left(1), 'C1 10$\\mu$F', align='bottom')
n1 = ax.node(c1l.left(1))
nn = ax.node(n1.left(1), 'SIGNAL', align='left')
ax.connect((nn, n1, c1l, None, c1r, r1l, None, r1r, ng1, pn))

r4b, r4t = ax.resistance_v(n4.down(1.5), 'R2 10k', align='left')
n5 = ax.node(r4b.down(1).right(1))
ax.connect((n4, r4t, None, r4b, n5))
n6 = ax.node(n5.down(1), 'COMMON', align='right')
ax.connect((n5.up(5), n5.down(1)))

np = ax.node(pp.left(1.5))
ax.connect((np.up(1.3), np,  pp))
n7 = ax.node(np.down(4.65), 'VREF', align='right')
ax.connect((np, n7))

r2b, r2t = ax.resistance_v(n1.down(1.5), 'R1 100k', align='left')
gnd2 = ax.ground(r2b.down(1), 'GND')
ax.connect((n1, r2t, None, r2b, gnd2))

ng2 = ax.node(po.right(1.5))
no = ax.node(ng2.right(1), 'P', 'right')
ax.connect((po, ng2, no))

r5l, r5r = ax.resistance_h(po.left(0.5).down(2), 'R4 10k', 'below')
ax.connect((ng1, r5l, None, r5r, ng2))

ax.set_xlim(-1.5, 12)
ax.set_ylim(0.5, 7)
ax.set_aspect('equal')
fig.savefig()
plt.show()

