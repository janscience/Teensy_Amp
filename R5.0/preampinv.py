import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(figsize=(16, 7.1))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')
#ax.set_xticks_off()
#ax.set_yticks_off()

ax.set_xlim(-1.5, 12)
ax.set_ylim(1, 7)
ax.set_aspect('equal')

pn, pp, po, pg, pw = ax.opamp_l((8, 5), 'OPA1662')
gnd1 = ax.ground(pg.down(0.6), 'GND')
ax.connect((pg, gnd1))
npwr = ax.bus(pw.up(0.5), 'VDD', align='top')
ax.connect((pw, npwr))

ng1 = ax.node(pn.left(0.5))
r4l, r4r = ax.resistance_h(ng1.left(1), 'R4 10k', align='bottom')
ngr = ax.node(r4l.left(2.5), 'SIGNALx', 'north')
c1l, c1r = ax.capacitance_h(ngr.left(1), 'C1 10$\\mu$F', align='top')
nsc = ax.node(c1l.left(1))
ns1 = ax.pin(nsc.left(1), 'CHx\nx1', align='left')
ax.connect((ns1, nsc, c1l, None, c1r, r4l, None, r4r, ng1, pn))

r1b, r1t = ax.resistance_v(nsc.up(1), 'R1 1M', align='left')
ns2 = ax.pin(r1t.up(0.5).left(1), 'CHx\nx0.1', align='left')
ax.connect((nsc, r1b, None, r1t, ns2))

r3b, r3t = ax.resistance_v(ngr.down(1), 'R3 10k', align='left')
nrc = ax.node(r3b.down(0.5).right(1))
ax.connect((ngr, r3t, None, r3b, nrc))
nc = ax.bus(nrc.down(0.5), 'AVRG', align='south')
ax.connect((nrc.up(4.5), nc))

np = ax.node(pp.left(2.5))
ax.connect((np.up(1.5), np,  pp))
nr = ax.bus(np.down(3.5), 'VREF', align='south')
ax.connect((np, nr))

r2b, r2t = ax.resistance_v(nsc.down(1), 'R2 100k', align='left')
gnd2 = ax.ground(r2b.down(0.5), 'GND')
ax.connect((nsc, r2t, None, r2b, gnd2))

ng2 = ax.node(po.right(0.5))
no = ax.pin(ng2.right(1.5), 'INxP', 'right')
ax.connect((po, ng2, no))

r5l, r5r = ax.resistance_h(po.left(0.5).down(2), 'R5 10k', 'below')
ax.connect((ng1, r5l, None, r5r, ng2))

nm1 = ax.node(ng2.right(0.5).down(1))
nm = ax.pin(nm1.right(1), 'INxM', 'right')
na = ax.bus(nm1.down(2), 'AREF', align='south')
ax.connect((na, nm1, nm))
ax.connect((nm1, nm1.up(3)))

fig.savefig()
plt.show()

