
import matplotlib.pyplot as plt
import plottools.plottools as pt
from matplotlib.patches import Rectangle

R0 = '1M'         # voltage divider
R1 = '300k'       # voltage divider
R2 = R1           # referencing input
R3 = R1           # averaging 
R4 = '10k'
R5 = '100k'       # gain = 1 + R5/R4
C1 = '10$\\mu$F'  # tau=R2*C1*(R2+2*R0)/(R2+R0) , if R1=R2.
                  # should be less than 1s
RB = '100'        # VGND voltage divider

preamp_style = dict(facecolor='#AADDAA')
refamp_style = dict(facecolor='#AAAADD')
vdiv_style = dict(facecolor='#DDAAAA')


def preamp(pos, ident, top='none'):
    pn, pp, po, pg, pw = ax.opamp_l(pos, f'OP{ident}', 'center', False,
                                    **preamp_style)
    gnd1 = ax.ground(pg.down(0.5), 'GND')
    ax.connect((pg, gnd1))
    npwr = ax.node(pw.up(0.6).right(2))
    ax.connect((npwr, pw))
    if top == 'bus':
        na = ax.bus(npwr.up(0.5), 'AVDD', 'north')
        ax.connect((npwr.down(3.5), na))
    elif top == 'break':
        bb, bt = ax.break_v(npwr.up(1))
        ax.connect((npwr.down(3.5), bb))
    else:
        ax.connect((npwr.down(3.5), npwr.up(0.5)))

    ng1 = ax.node(pn.left(0.5))
    r4l, r4r = ax.resistance_h(ng1.left(1), f'R4 {R4}', 'below',
                               **preamp_style)
    ax.connect((pn, ng1, r4r, None, r4l))

    np = ax.node(r4l.left(0.5))
    ax.connect((np.down(1.8), np,  r4l))
    if top == 'bus':
        nvr = ax.bus(np.up(2.2), 'VGND', 'north')
        ax.connect((np, nvr))
    elif top == 'break':
        bb, bt = ax.break_v(np.up(2.7))
        ax.connect((np, bb))
    else:
        ax.connect((np, np.up(2.2)))
    
    ngr = ax.node(pp.left(4), f'SIG{ident}', 'north')
    r3b, r3t = ax.resistance_v(ngr.down(1), f'R3\n{R3}', 'left',
                               **refamp_style)
    nra = ax.node(r3b.down(0.5).right(0.5))
    ax.connect((ngr, r3t, None, r3b, nra))
    if top == 'bus':
        ba = ax.bus(nra.up(3.2), 'AVRG', 'north', **refamp_style)
        ax.connect((nra.down(0.8), ba))
    elif top == 'break':
        bb, bt = ax.break_v(nra.up(3.7))
        ax.connect((nra.down(0.8), bb))
    else:
        ax.connect((nra.down(0.8), nra.up(3.2)))

    nrv = ax.node(ngr.left(1.5))
    r2b, r2t = ax.resistance_v(nrv.down(1), f'R2\n{R2}', 'left',
                               **preamp_style)
    nv = ax.node(r2b.down(1))
    nv1 = ax.node(nv.right(3))
    ax.connect((nrv, r2t, None, r2b, nv, nv1))
    """
    if top == 'bus':
        bv = ax.bus(nv1.up(3.2), 'VGND', 'north', **preamp_style)
        ax.connect((nv1.down(0.8), bv))
    elif top == 'break':
        bb, bt = ax.break_v(nv1.up(3.7))
        ax.connect((nv1.down(0.8), bb))
    else:
        ax.connect((nv1.down(0.8), nv1.up(3.2)))
    """
    c1l, c1r = ax.capacitance_h(nrv.left(1), f'C1 {C1}', 'top')
    nsc = ax.node(c1l.left(1))
    ns1 = ax.pin(nsc.left(2.5), f'x1 CH{ident}', 'left',
                 **preamp_style)
    ax.connect((pp, ngr, nrv, c1r, None, c1l, nsc, ns1))

    r1b, r1t = ax.resistance_v(nsc.down(1), f'R1\n{R1}', 'left',
                               **vdiv_style)
    ax.connect((nsc, r1t, None, r1b, nv))
    r0l, r0r = ax.resistance_h(nsc.up(0.5).left(1), f'R0 {R0}', 'top',
                               **vdiv_style)
    ns2 = ax.pin(r0l.left(1), f'x0.1 CH{ident}', 'left',
                 **vdiv_style)
    ax.connect((nsc, r0r, None, r0l, ns2))

    ng2 = ax.node(po.right(0.5))
    no = ax.pin(ng2.right(2.5), f'IN{ident}P', 'right',
                **preamp_style)
    ax.connect((po, ng2, no))

    r5l, r5r = ax.resistance_h(po.left(0.75).down(1.75), f'R5 {R5}', 'below',
                               **preamp_style)
    ax.connect((ng1, r5l, None, r5r, ng2))

    nm1 = ax.node(ng2.right(1.5).down(1))
    nm = ax.pin(nm1.right(1), f'IN{ident}M', 'right',
                **refamp_style)
    if top == 'bus':
        na = ax.bus(nm1.up(2.7), 'AREF', 'north', **refamp_style)
        ax.connect((na, nm1, nm))
        ax.connect((nm1, nm1.down(1.3)))
    elif top == 'break':
        bb, bt = ax.break_v(nm1.up(3.2))
        ax.connect((nm1, nm))
        ax.connect((nm1.down(1.3), bb))
    else:
        ax.connect((nm1, nm))
        ax.connect((nm1.down(1.3), nm1.up(2.7)))


def refamp(pos):
    pn, pp, po, pg, pw = ax.opamp_l(pos, 'OP0', 'center', False,
                                    **refamp_style)
    gnd1 = ax.ground(pg.down(0.5), 'GND')
    ax.connect((pg, gnd1))
    npwr = ax.node(pw.up(0.6).right(2))
    ax.connect((npwr.up(0.5), npwr, pw))

    pd = ax.pin(pp.left(3), 'DIFF', 'north')
    ps = ax.pin(pd.left(0.5), 'S1', 'below')
    pm = ax.pin(ps.left(0.5), 'MONO', 'north')
    nr = pm.down(1)
    ax.connect((pp, pd, None, pm, nr, None, ps, ps.up(1.2)))

    ng1 = ax.node(pn.left(0.5))
    r4l, r4r = ax.resistance_h(ng1.left(1), f'R4 {R4}', 'below',
                               **refamp_style)
    nr1 = ax.node(r4l.left(0.5))
    """
    pl, pr, pt, pb = ax.chip(nr1.left(3), pins_left=0,
                             pins_right=[None, '', None],
                             pins_top=[''], pins_bottom=[''],
                             palign='bottom', label='VGND',
                             align='center', rotation='vertical')
    ax.connect((npwr, pt[0]))
    gnd2 = ax.ground(pb[0].down(0.5), 'GND')
    ax.connect((pb[0], gnd2))
    br = ax.bus(nr1.down(0.5), 'VGND ', 'south')
    """
    ax.connect((nr, nr1, r4l, None, r4r, ng1, pp))
    ax.connect((nr1, nr1.up(2.2)))

    ng2 = ax.node(po.right(0.5))
    spo = ax.pin(ng2.right(1), 'DIFF', 'above')
    no = ax.pin(spo.right(0.5), 'S2', 'below')
    ax.connect((po, ng2, spo, None, no, no.up(1.7)))
    r5l, r5r = ax.resistance_h(po.left(0.75).down(1.75), f'R5 {R5}', 'below',
                               **refamp_style)
    ax.connect((ng1, r5l, None, r5r, ng2))

    
def vgnd(pos):
    pb = ax.pin(pos, 'MICBIAS', 'right')
    r1b, r1t = ax.resistance_v(pb.down(1), f'R {RB}', 'right')
    nb = ax.node(r1b.down(0.5))
    r2b, r2t = ax.resistance_v(nb.down(1), f'R {RB}', 'right')
    gnd = ax.ground(r2b.down(0.5), 'GND')
    ax.connect((pb, r1t, None, r1b, nb, r2t, None, r2b, gnd))
    bb = ax.bus(nb.right(0.5), 'VGND', 'right')
    nbo = ax.node(nb.left(0.5))
    spb = ax.pin(nbo.left(0.5), 'MONO', 'above')
    ax.connect((bb, nb, nbo, spb))
    ax.connect((nbo, nbo.down(2.5), nbo.down(2.5).left(7), nbo.up(0.5).left(7)))
    

plt.rcParams['font.size'] = 11

fig, ax = plt.subplots(figsize=(9, 9.1))
fig.subplots_adjust(nomargins=True)
ax.show_spines('')
#ax.set_xticks_off()
#ax.set_yticks_off()

ax.set_xlim(-0.5, 18.5)
ax.set_ylim(-3, 16.2)
ax.set_aspect('equal')

preamp((12, 13), '$i$', 'bus')
preamp((12, 8), 2, 'break')
preamp((12, 4), 1, 'none')
refamp((12, 0))
vgnd((16.5, 2))

fig.savefig()
plt.show()

