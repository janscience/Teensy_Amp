import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(figsize=(16, 8.6))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')
#ax.set_xticks_off()
#ax.set_yticks_off()

ax.set_xlim(-1, 15)
ax.set_ylim(-0.7, 7.9)
ax.set_aspect('equal')

pn, pp, po, pg, pw = ax.opamp_l((8.5, 4), 'OPA1662')
gnd1 = ax.ground(pg.down(0.8), 'GND')
ax.connect((pg, gnd1))
npwr = ax.bus(pw.up(0.9), 'VDD', align='top')
ax.connect((pw, npwr))

ng1 = ax.node(pn.left(0.5).down(1.5))
r4l, r4r = ax.resistance_h(ng1.left(1), 'R4 10k', align='bottom')
ngr = ax.node(r4l.left(0.5))
ax.connect((pn, ng1, r4r, None, r4l, ngr, ngr.up(5.5)))
nr = ax.bus(ngr.down(1), 'VREF', align='south')
ax.connect((ngr, nr))

ncc = ax.node(pp.left(4.5))
c1l, c1r = ax.capacitance_h(ncc.left(1), 'C1 10$\\mu$F', align='bottom')
nsc = ax.node(c1l.left(1))
ns1 = ax.pin(nsc.left(1), 'SIGNAL\nx1', align='left')
ax.connect((ns1, nsc, c1l, None, c1r, ncc, pp))

r1b, r1t = ax.resistance_v(nsc.up(1.5), 'R1 1M', align='left')
ns2 = ax.pin(r1t.up(1).left(1), 'SIGNAL\nx0.1', align='left')
ax.connect((nsc, r1b, None, r1t, ns2))

r2b, r2t = ax.resistance_v(nsc.down(1.5), 'R2 100k', align='left')
gnd2 = ax.ground(r2b.down(1), 'GND')
ax.connect((nsc, r2t, None, r2b, gnd2))

r3b, r3t = ax.resistance_v(ncc.down(1.5), 'R3 10k', align='left')
nrc = ax.node(r3b.down(0.5).right(1))
nc = ax.bus(nrc.down(1), ' COMMON', align='south')
ax.connect((ncc, r3t, None, r3b, nrc, nc))
ax.connect((nrc.up(5.5), nrc))

ng2 = ax.node(po.right(0.5))
r6l, r6r = ax.resistance_h(ng2.right(1.5), 'R6 1k', 'below')
no = ax.pin(r6r.right(1), 'INxP', 'right')
ax.connect((po, ng2, r6l, None, r6r, no))

r5l, r5r = ax.resistance_h(ng1.right(1.5), 'R5 10k', 'below')
ax.connect((ng1, r5l, None, r5r, ng2))

fig.savefig()
plt.show()

