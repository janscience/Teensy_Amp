import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

R1 = '1M'
R2 = '100k'
#R3 = '10k'
R3 = '47k'
R4 = R3
R5 = R3
R6 = R3
R7 = R3
C1 = '10$\\mu$F'


def preamp(pos, index, show_bus=True):
    pn, pp, po, pg, pw = ax.opamp_l(pos, f'OP{1 + index}', 'center', True)
    #gnd1 = ax.ground(pg.down(0.6), 'GND')
    #ax.connect((pg, gnd1))
    #npwr = ax.bus(pw.up(0.5), 'VDD', 'top')
    #ax.connect((pw, npwr))

    ng1 = ax.node(pn.left(0.5))
    r4l, r4r = ax.resistance_h(ng1.left(1), f'R4 {R4}', 'above')
    ngr = ax.node(r4l.left(3.5), f'SIGNAL{1 + index}', 'northeast')
    c1l, c1r = ax.capacitance_h(ngr.left(1), f'C1 {C1}', 'top')
    nsc = ax.node(c1l.left(1))
    nj1 = ax.pin(nsc.left(0.7))
    nj2 = ax.pin(nj1.left(0.6), 'J1', 'southeast')
    nsj = ax.node(nj2.left(0.7))
    ns = ax.pin(nsj.left(1), f'CH{1 + index}', 'left')
    ax.connect((ns, nsj, nj2, None, nj1, nsc, c1l, None, c1r, r4l, None, r4r, ng1, pn))

    r1l, r1r = ax.resistance_h(nsc.up(0.5).left(1), f'R1 {R1}', 'top')
    ax.connect((nsc, r1r, None, r1l, nsj))

    r3l, r3r = ax.resistance_h(ngr.down(0.5).right(1), f'R3 {R3}', 'below')
    nrc = ax.node(r3r.right(0.5))
    ax.connect((ngr, r3l, None, r3r, nrc))
    if show_bus:
        nc = ax.bus(nrc.up(1.5), 'AVRG', 'north')
        ax.connect((nrc.down(2.5), nc))
    else:
        ax.connect((nrc.down(2.5), nrc.up(1.5)))

    np = ax.node(pp.left(2.5))
    ax.connect((np.down(2), np,  pp))
    if show_bus:
        nr = ax.bus(np.up(2), 'VREF', 'north')
        ax.connect((np, nr))
    else:
        ax.connect((np, np.up(2)))

    r2b, r2t = ax.resistance_v(nsc.down(1), f'R2 {R2}', 'left')
    gnd2 = ax.ground(r2b.down(0.5), 'GND')
    ax.connect((nsc, r2t, None, r2b, gnd2))

    ng2 = ax.node(po.right(0.5))
    no = ax.pin(ng2.right(1.5), f'IN{1 + index%4}P', 'right')
    ax.connect((po, ng2, no))

    r5l, r5r = ax.resistance_h(po.left(0.5).up(1.5), f'R5 {R5}', 'above')
    ax.connect((ng2, r5r, None, r5l, ng1))

    nm1 = ax.node(ng2.right(0.5).down(1))
    nm = ax.pin(nm1.right(1), f'IN{1 + index%4}M', 'right')
    if show_bus:
        na = ax.bus(nm1.up(2.5), 'AREF', 'north')
        ax.connect((na, nm1, nm))
        ax.connect((nm1, nm1.down(1.5)))
    else:
        ax.connect((nm1, nm))
        ax.connect((nm1.down(1.5), nm1.up(2.5)))


def refamp(pos):
    pn, pp, po, pg, pw = ax.opamp_l(pos, 'OP0', 'center', True)
    #gnd1 = ax.ground(pg.down(0.6), 'GND')
    #ax.connect((pg, gnd1))
    #npwr = ax.bus(pw.up(1), 'VDD', 'top')
    #ax.connect((pw, npwr))

    ng1 = ax.node(pn.left(0.5))
    r4l, r4r = ax.resistance_h(ng1.left(1), f'R4 {R4}', 'above')
    nc = r4l.left(1.5).up(1)
    ax.connect((nc, r4l, None, r4r, ng1, pn))

    npr = ax.node(pp.left(2.5))
    ax.connect((npr.up(2), npr, pp))
    nrg = ax.node(npr.down(1))
    r6b, r6t = ax.resistance_v(nrg.down(1), f'R7 {R7}', 'right')
    gndr = ax.ground(r6b.down(0.5), 'GND', 'right')
    ax.connect((npr, nrg, r6t, None, r6b, gndr))
    r7l, r7r = ax.resistance_h(nrg.right(2), f'R6 {R6}', 'bottom')
    nr2 = ax.pin(r7r.right(3.5), 'VREF', 'right')
    ax.connect((nrg, r7l, None, r7r, nr2))

    ng2 = ax.node(po.right(0.5))
    no = ng2.right(0.5).up(1.5)
    ax.connect((po, ng2, no))

    r5l, r5r = ax.resistance_h(po.left(0.5).up(1.5), f'R5 {R5}', 'above')
    ax.connect((ng2, r5r, None, r5l, ng1))
    


plt.rcParams['font.size'] = 11

fig, ax = plt.subplots(figsize=(8, 9.5))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')
#ax.set_xticks_off()
#ax.set_yticks_off()

ax.set_xlim(0, 16)
ax.set_ylim(-4, 15)
ax.set_aspect('equal')

preamp((12, 12), 2, True)
preamp((12, 8), 1, False)
preamp((12, 4), 0, False)
refamp((12, 0))

fig.savefig()
plt.show()

