from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from thunderlab.dataloader import load_data

def make_title(fig, filepath):
    specs = filepath.replace('.wav', '').split('-')
    nboards = int(specs[1])
    boards = 'two R4.1 boards' if nboards > 1 else 'single R4.1 board'
    gain = 'at gain ' + specs[-1] + ','
    batteries = {'12V': '12V battery',
                 'liion': '3.6V LiIon battery',
                 'powerbank': '5V powerbank'}
    power = batteries[specs[0]] + ','
    isolator = ''
    if specs[2] == 'isolated':
        isolator = 'isolated DC/DC converter' 
    elif specs[2] == 'nonisol':
        isolator = 'non-isolated DC/DC converter' 
    resistor = f'(GNDs connected by {specs[3]})' if len(specs) >= 5 else ''
    resistor = resistor.replace('Ohm', '\u2126')
    title = ' '.join([boards, gain, power, isolator, resistor])
    fig.suptitle(title.rstrip(', '))

    
def plot_trace(ax, data, rate, amax, twin):
    n = len(data)//2
    data = data[n:n + int(twin*rate), 0]
    time = np.arange(len(data))*1000/rate
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.plot(time, data, color='tab:blue', lw=0.5)
    ax.set_xlabel('Time [ms]')
    ax.set_xlim(0, 1000*twin)
    ax.set_ylim(-amax, amax)


def plot_power(ax, data, rate, amax):
    data = data[len(data)//10:, 0]
    data -= np.mean(data)
    freqs, power = welch(data/amax, rate, nperseg=2**11)
    powerdb = 10*np.log10(power*freqs[1])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.axvline(630, ls=':', color='gray', lw=1)
    ax.plot(freqs, powerdb, color='tab:red', lw=1)
    ax.set_xlim(0, 6000)
    ax.set_ylim(-80, -10)
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Power [dBFS]')


def plot(data, rate, unit, amax, filepath):
    plt.rcParams['font.size'] = 7
    fig, (axt, axz, axp) = plt.subplots(1, 3, figsize=(16/2.54, 4/2.54),
                                        layout='constrained')
    make_title(fig, filepath)
    plot_trace(axt, data, rate, amax, 0.02)
    axt.set_ylabel(f'Signal [{unit}]')
    plot_trace(axz, data, rate, amax, 0.004)
    axz.spines['left'].set_visible(False)
    axz.yaxis.set_major_locator(plt.NullLocator())
    plot_power(axp, data, rate, amax)
    fig.savefig(filepath.replace('.wav', '.png'), dpi=200)
    #plt.show()


def main():
    for filepath in sorted(glob('*.wav')):
        print(filepath)
        data, rate, unit, amax = load_data(filepath)
        plot(data, rate, unit, amax, filepath)

if __name__ == '__main__':
    main()
