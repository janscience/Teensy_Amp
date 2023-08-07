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
r1l, r1r = ax.resistance_h(ng1.left(1), 'R2 4.7k')
c1l, c1r = ax.capacitance_h(r1l.left(1), 'C1 10$\mu$F')
n1 = ax.node(c1l.left(1))
nn = ax.node(n1.left(1), 'SIGNAL', align='left')
ax.connect((nn, n1, c1l, None, c1r, r1l, None, r1r, ng1, pn))

np = ax.node(nn.up(2.65), 'VREF', align='left')
ax.connect((np, np.right(4.7),  pp))

r2b, r2t = ax.resistance_v(n1.down(1.3), 'R1 100k')
gnd2 = ax.ground(r2b.down(0.7), 'GND')
ax.connect((n1, r2t, None, r2b, gnd2))

ng2 = ax.node(po.right(1.5))
no = ax.node(ng2.right(1), 'CH1L', 'right')
ax.connect((po, ng2, no))

r5l, r5r = ax.resistance_h(po.right(0.5).down(2), 'R3 47k', 'below')
ax.connect((ng1, r5l, None, r5r, ng2))

ax.set_xlim(0.5, 12.5)
ax.set_ylim(1.5, 7.5)
ax.set_aspect('equal')
fig.savefig()
plt.show()

