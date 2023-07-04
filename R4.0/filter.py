import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(cmsize=(30, 12))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')

nn = ax.node((-4, 0), 'SIGNAL', align='left')
c1l, c1r = ax.capacitance_h(nn.right(1), 'C1 10$\mu$F')
nr = ax.node(c1r.right(1))
r1l, r1r = ax.resistance_h(nr.right(1), 'R1 330')
nc = ax.node(r1r.right(1))
ax.connect((nn, c1l, None, c1r, nr, r1l, None, r1r, nc, nc.right(2.5)))

r2b, r2t = ax.resistance_v(nr.down(1.5), 'R2 330')
gnd1 = ax.ground(r2b.down(1))
ax.connect((nr, r2t, None, r2b, gnd1))

c2b, c2t = ax.capacitance_v(nc.down(1.5), 'C2 22nF')
gnd2 = ax.ground(c2b.down(1.3))
ax.connect((nc, c2t, None, c2b, gnd2))


w = 2*plt.rcParams['circuits.scale']
h = 1.5*w
x, y = 5, -1
ax.add_patch(Rectangle((x - 0.5*w, y - 0.5*h), w, h,
                       edgecolor='none', facecolor='w'))
ax.add_patch(Rectangle((x - 0.5*w, y - 0.5*h), w, h,
                       edgecolor='k', facecolor='none', lw=2))
ax.text(x, y, 'PCM1865', ha='center', va='center')

nch1 = ax.node((3, 0), 'CH1L', align='top')
ax.connect((nch1, nch1.right(1)))

agnd = pt.Pos(6, -2)
ngnd = ax.node(agnd.right(1), 'AGND')
gnd3 = ax.ground(ngnd.down(1), 'GND')
ax.connect((gnd3, ngnd, agnd))

ax.set_xlim(-6, 9)
ax.set_ylim(-3.5, 1)
ax.set_aspect('equal')
fig.savefig()
plt.show()

