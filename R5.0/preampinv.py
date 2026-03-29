import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(figsize=(16, 11))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')
#ax.set_xticks_off()
#ax.set_yticks_off()

ax.set_xlim(-1.5, 12)
ax.set_ylim(0, 8)
ax.set_aspect('equal')

pn, pp, po, pg, pw = ax.opamp_l((8, 5), 'OPA1662')
gnd1 = ax.ground(pg.down(0.8), 'GND')
ax.connect((pg, gnd1))
npwr = ax.bus(pw.up(0.9), 'VDD', align='top')
ax.connect((pw, npwr))

ng1 = ax.node(pn.left(0.5))
r4l, r4r = ax.resistance_h(ng1.left(1), 'R4 10k', align='bottom')
ngr = ax.node(r4l.left(2.5))
c1l, c1r = ax.capacitance_h(ngr.left(1), 'C1 10$\\mu$F', align='bottom')
nsc = ax.node(c1l.left(1))
ns1 = ax.pin(nsc.left(1), 'SIGNAL\nx1', align='left')
ax.connect((ns1, nsc, c1l, None, c1r, r4l, None, r4r, ng1, pn))

r1b, r1t = ax.resistance_v(nsc.up(1.5), 'R1 1M', align='left')
ns2 = ax.pin(r1t.up(1).left(1), 'SIGNAL\nx0.1', align='left')
ax.connect((nsc, r1b, None, r1t, ns2))

r3b, r3t = ax.resistance_v(ngr.down(1.5), 'R3 10k', align='left')
nrc = ax.node(r3b.down(0.5).right(1))
ax.connect((ngr, r3t, None, r3b, nrc))
nc = ax.bus(nrc.down(0.5), 'COMMON', align='south')
ax.connect((nrc.up(6), nc))

np = ax.node(pp.left(2.5))
ax.connect((np.up(2.5), np,  pp))
nr = ax.bus(np.down(4), 'VREF', align='south')
ax.connect((np, nr))

r2b, r2t = ax.resistance_v(nsc.down(1.5), 'R2 100k', align='left')
gnd2 = ax.ground(r2b.down(1), 'GND')
ax.connect((nsc, r2t, None, r2b, gnd2))

ng2 = ax.node(po.right(0.5))
no = ax.pin(ng2.right(1), 'INxP', 'right')
ax.connect((po, ng2, no))

r5l, r5r = ax.resistance_h(po.left(0.5).down(2), 'R5 10k', 'below')
ax.connect((ng1, r5l, None, r5r, ng2))

fig.savefig()
plt.show()

