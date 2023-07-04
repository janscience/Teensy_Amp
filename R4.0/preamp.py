import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots()
fig.subplots_adjust(nomargins=True)
ax.show_spines('')

pn, pp, po, pg, pw = ax.opamp_l((8, 5), 'OPA1662')
gnd1 = ax.ground(pg.down(1), 'GND')
ax.connect((pg, gnd1))
npwr = ax.node(pw.up(1), 'VDD')
ax.connect((pw, npwr))

ng1 = ax.node(pn.left(1))
r1l, r1r = ax.resistance_h(ng1.left(1), 'R1 800')
n1 = ax.node(r1l.left(1))
c1l, c1r = ax.capacitance_h(n1.left(1), 'C1 10$\mu$F')
nn = ax.node(c1l.left(1), 'SIGNAL', align='left')
ax.connect((nn, c1l, None, c1r, n1, r1l, None, r1r, ng1, pn))

n2 = ax.node(pp.left(3.5).up(2))
np = ax.node(nn.up(2.65), 'VREF', align='left')
r2b, r2u = ax.resistance_v(n1.up(1.3), 'R2 200')
ax.connect((n1, r2b, None, r2u, n2))

ax.connect((np, n2,n2.right(2),  pp))

r3l, r3r = ax.resistance_h(po.right(1), 'R3 100')
ng2 = ax.node(r3r.right(1))
r4l, r4r = ax.resistance_h(ng2.right(1), 'R4 300')
nlp = ax.node(r4r.right(1))
no = ax.node(nlp.right(2), 'CH1L')
ax.connect((po, r3l, None, r3r, ng2, r4l, None, r4r, nlp, no))

r5l, r5r = ax.resistance_h(po.right(1).down(2), 'R5 10k')
ax.connect((ng1, r5l, None, r5r, ng2))

c2b, c2t = ax.capacitance_v(nlp.down(1), 'C2 22nF')
gnd2 = ax.ground(c2b.down(1), 'GND')
ax.connect((nlp, c2t, None, c2b, gnd2))


w = 2*plt.rcParams['circuits.scale']
h = 1.5*w
x, y = 3, -1
ax.add_patch(Rectangle((x - 0.5*w, y - 0.5*h), w, h,
                       edgecolor='none', facecolor='w'))
ax.add_patch(Rectangle((x - 0.5*w, y - 0.5*h), w, h,
                       edgecolor='k', facecolor='none', lw=2))
ax.text(x, y, 'PCM1865', ha='center', va='center')

nch1 = ax.node((x-2, y+1), 'CH1L',align='left')
ax.connect((nch1, nch1.right(1)))

vdd = pt.Pos(x+1, y+1)
nvdd = ax.node(vdd.right(1), 'VDD 3.3V', 'above')
nvc = ax.node(nvdd.right(2))
c3b, c3t = ax.capacitance_v(nvc.up(1), 'C3 10$\mu$F')
gnd4 = ax.ground_u(c3t.up(0.8))
ax.connect((vdd, nvdd, nvc))
ax.connect((gnd4, c3t, None, c3b, nvc))

vref = pt.Pos(x+1, y)
nvref = ax.node(vref.right(1), 'VREF 1.6V', 'above')
nrc1 = ax.node(nvref.right(2))
r6l, r6r = ax.resistance_h(nrc1.right(1.5), 'R6 10k')
nrc2 = ax.node(r6r.right(1))
pn, pp, po, pg, pw = ax.opamp_l(nrc2.right(3).down(0.3), '')
nb = ax.node(po.right(1))
nbc = ax.node(nb.right(1))
nbo = ax.node(nbc.right(1), 'VREF', 'above')
ax.connect((vref, nvref, nrc1, r6l, None, r6r, nrc2, pp, None, po, nb, nbc, nbo))

gnd1 = ax.ground(pg.down(1), 'GND')
ax.connect((pg, gnd1))
npwr = ax.node(pw.up(1), 'VDD')
ax.connect((pw, npwr))

ax.connect((pn, pn.left(0.5), pn.left(0.5).down(2), nb))

c6b, c6t = ax.capacitance_v(nbc.down(1), 'C6 10$\mu$F')
gnd6 = ax.ground(c6b.down(0.8))
ax.connect((gnd6, c6b, None, c6t, nbc))


c4b, c4t = ax.capacitance_v(nrc1.down(1), 'C4 10$\mu$F')
gnd4 = ax.ground(c4b.down(0.8))
ax.connect((gnd4, c4b, None, c4t, nrc1))

c5b, c5t = ax.capacitance_v(nrc2.down(1), 'C5 10$\mu$F')
gnd5 = ax.ground(c5b.down(0.8))
ax.connect((gnd5, c5b, None, c5t, nrc2))

agnd = pt.Pos(x+1, y-1)
ngnd = ax.node(agnd.right(1), 'AGND', 'above')
gnd3 = ax.ground(ngnd.down(1), 'GND')
ax.connect((gnd3, ngnd, agnd))

ax.set_xlim(0, 18)
ax.set_ylim(-4, 7.5)
ax.set_aspect('equal')
fig.savefig()
plt.show()

