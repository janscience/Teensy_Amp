import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(figsize=(18, 8))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')

w = 2*plt.rcParams['circuits.scale']
h = 1.5*w
x, y = 5, -2
ax.add_patch(Rectangle((x - 0.5*w, y - 0.5*h), w, h,
                       edgecolor='none', facecolor='w'))
ax.add_patch(Rectangle((x - 0.5*w, y - 0.5*h), w, h,
                       edgecolor='k', facecolor='none', lw=2))
ax.text(x, y, 'PCM1865', ha='center', va='center')

nch1 = ax.node((x-2, y+1), 'CH1L', align='left')
ax.connect((nch1, nch1.right(1)))

vdd = pt.Pos(x+1, y+1)
nvdd = ax.node(vdd.right(1), 'VDD 3.3V', 'above')
nvc = ax.node(nvdd.right(2))
nvddout = ax.node(nvc.right(5), 'VDD', 'right')
c3b, c3t = ax.capacitance_v(nvc.up(1), 'C4 10$\mu$F')
gnd4 = ax.ground_u(c3t.up(0.8))
ax.connect((vdd, nvdd, nvc, nvddout))
ax.connect((gnd4, c3t, None, c3b, nvc))

vref = pt.Pos(x+1, y)
nvref = ax.node(vref.right(1), 'VREF 1.6V', 'above')
nrc1 = ax.node(nvref.right(2))
r6l, r6r = ax.resistance_h(nrc1.right(1.5), 'R5 10k')
nrc2 = ax.node(r6r.right(1))
nbo = ax.node(nrc2.right(2), 'VREF', 'right')
ax.connect((vref, nvref, nrc1, r6l, None, r6r, nrc2, nbo))

c4b, c4t = ax.capacitance_v(nrc1.down(1), 'C5 10$\mu$F')
gnd4 = ax.ground(c4b.down(0.8))
ax.connect((gnd4, c4b, None, c4t, nrc1))

c5b, c5t = ax.capacitance_v(nrc2.down(1), 'C6 10$\mu$F')
gnd5 = ax.ground(c5b.down(0.8))
ax.connect((gnd5, c5b, None, c5t, nrc2))

agnd = pt.Pos(x+1, y-1)
ngnd = ax.node(agnd.right(1), 'AGND', 'above')
gnd3 = ax.ground(ngnd.down(1), 'GND')
ax.connect((gnd3, ngnd, agnd))

ax.set_xlim(2, 15)
ax.set_ylim(-4.5, 1.5)
ax.set_aspect('equal')
fig.savefig()
plt.show()

