import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# channels, duration:
anker_capacity = 10 # Ah
anker_efficiency = 0.75
anker_data = [[16, '19h35min'],
              [16, '19h35min'],
              [12, '22h30min'],
              [12, '21h50min'],
              [12, '22h25min'],
              [ 8, '27h35min'],
              [ 8, '28h05min'],
              [ 8, '28h05min'],
              [ 4, '32h50min'],
              [ 4, '32h45min']]

keep_capacity = 11 # Ah
keep_efficiency = 1
keep_data = [[16, '33h05min'],
             [16, '33h05min'],
              [8, '49h00min']]

             
def analyze_power_consumption(brand, data, capacity):
    volt = 3.3 # V
    channels = []
    durations = []
    for c, d in data:
        h = int(d.split('h')[0])
        m = int(d.split('h')[1].replace('min', ''))
        channels.append(c)
        durations.append(h*60+m)
    durations = np.array(durations)
    currents = capacity/(durations/60)
    r = linregress(channels, currents)
    x = np.linspace(0, 18, 10)
    l = x*r.slope + r.intercept
    c16 = r.intercept + r.slope*16
    print(f'{brand}:')
    print(f'  Teensy draws {1000*r.intercept:.0f}mA of current')
    print(f'  Each pcm chip draws {1000*r.slope*4:.0f}mA of current')
    print(f'  16 channels draw {1000*c16:.0f}mA of current: {c16*volt:.2f}W')
    chans = np.sort(np.unique(channels))
    durs = []
    curs = []
    for c in chans:
        durs.append(np.mean(durations[channels == c]))
        curs.append(np.mean(currents[channels == c]))
    durs = np.array(durs)
    curs = np.array(curs)

    fig, (axd, axc, axp) = plt.subplots(1, 3, layout='constrained')
    fig.suptitle(brand)
    jitter = 0.5*(np.random.rand(len(channels)) - 0.5)
    axd.plot(channels + jitter, durations/60, 'o',  color='C0')
    axd.plot(chans, durs/60, '-',  color='C0')
    axd.set_xlabel('channels')
    axd.set_ylabel('duration [h]')
    axd.set_xlim(0, 18)
    axd.set_ylim(0, 50)
    axc.plot(channels + jitter, 1000*currents, 'o',  color='C0')
    axc.plot(chans, 1000*curs, '-',  color='C0')
    axc.plot(x, 1000*l, color='C1')
    axc.set_xlabel('channels')
    axc.set_ylabel('current [mA]')
    axc.set_xlim(0, 18)
    axc.set_ylim(0, 500)
    axp.plot(channels + jitter, currents*volt, 'o', color='C0')
    axp.plot(chans, curs*volt, '-', color='C0')
    axp.plot(x, l*volt, color='C1')
    axp.set_xlabel('channels')
    axp.set_ylabel('power [W]')
    axp.set_xlim(0, 18)
    axp.set_ylim(0, 2)
    plt.show()
    print()


analyze_power_consumption('Anker PowerCore 10000 redux powerbank', anker_data, anker_efficiency*anker_capacity)
analyze_power_consumption('KeepPower 26650 5500mAh x 2', keep_data, keep_efficiency*keep_capacity)

