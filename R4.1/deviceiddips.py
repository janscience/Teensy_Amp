import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

plt.rcParams['font.size'] = 18

fig, ax = plt.subplots(figsize=(11, 7))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')

n = 6
ax.text(-0.4, 0, 'Teensy pins:', ha='right', va='center')
np = ax.pin((0, 0), '41', 'right')
for i in range(n):
    nti = ax.pin(np.right((i+1)*1.5), f'{40-i}', 'right')
    sb, st = ax.switch_v(nti.ups(1.5), f'DIP{i}')
    nt = ax.node(st.ups(1))
    rb, rt = ax.resistance_v(nti.downs(1.5), f'R{i}')
    nb = ax.node(rb.downs(1))
    ax.connect((nt, st, None, sb, nti, rt, None, rb, nb))
gnd = ax.ground(np.right(1.5).down(4), 'GND')
ax.connect((np, nt.left(n*1.5), nt))
ax.connect((gnd, nb.left((n-1)*1.5), nb))


ax.set_xlim(-2.3, n*1.5+1.2)
ax.set_aspect('equal')
fig.savefig()
plt.show()

