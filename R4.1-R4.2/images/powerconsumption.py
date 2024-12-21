import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# channels, duration:
anker_brand = 'Anker PowerCore 10000 redux powerbank'
anker_capacity = 10 # Ah
anker_efficiency = 0.75  # 0.86^2
anker_capacity *= anker_efficiency
anker_channel_data = [[16, '19h35min'],
                      [16, '19h35min'],
                      [12, '22h30min'],
                      [12, '21h50min'],
                      [12, '22h25min'],
                      [ 8, '27h35min'],
                      [ 8, '28h05min'],
                      [ 8, '28h05min'],
                      [ 4, '32h50min'],
                      [ 4, '32h45min']]
anker_cpu_data = [[600, '16h45min'],
                  [150, '18h25min'],
                  [24, '19h35min'],
                  [24, '19h35min']]
anker_usb_data = [[0, '19h35min'],
                  [0, '19h35min'],
                  [1, '19h20min'],
                  [1, '19h40min'],
                  [2, '19h55min'],
                  [2, '20h00min'],
                  [2, '19h40min'],
                  #[2, '19h10min'],
                  [2, '19h45min'],
                  [2, '19h25min']]
anker_sdspi_data = [[1, '16h40min'],
                    [1, '16h30min'],
                    [0, '18h20min'],
                    [0, '18h55min']]
anker_rate_data = [[24, '19h50min'],
                   [24, '19h45min'],
                   [24, '19h40min'],
                   [48, '19h55min'],
                   [48, '20h00min'],
                   [48, '19h40min'],
                   [48, '19h45min'],
                   [48, '19h25min'],
                   [96, '17h25min'],
                   [96, '17h10min'],
                   [96, '17h10min'],
                   [96, '17h25min']]


keep_brand = 'KeepPower 26650 5500mAh x 2'
keep_capacity = 11 # Ah
keep_efficiency = 1
keep_capacity *= keep_efficiency
keep_channel_data = [[16, '33h05min'],
                     [16, '33h05min'],
                     [16, '33h00min'],
                     [16, '32h35min'],
                     [8, '49h00min']]


def analyze_currents(data, capacity):
    durations = []
    parameters = []
    for p, d in data:
        h = int(d.split('h')[0])
        m = int(d.split('h')[1].replace('min', ''))
        durations.append(h*60+m)
        parameters.append(p)
    durations = np.array(durations)
    currents = capacity/(durations/60)
    return durations, currents, np.array(parameters)


def mean_currents(durations, currents, parameters):
    params = np.sort(np.unique(parameters))
    durs = []
    curs = []
    for p in params:
        durs.append(np.mean(durations[parameters == p]))
        curs.append(np.mean(currents[parameters == p]))
    durs = np.array(durs)
    curs = np.array(curs)
    return durs, curs, params


def plot_regression(brand, parameters, durations, currents,
                    param_values, mean_durations, mean_currents,
                    line_x, line_y, xlabel, max_x):
    volt = 3.3 # V
    fig, (axd, axc, axp) = plt.subplots(1, 3, layout='constrained')
    fig.suptitle(brand)
    jitter = 0.5*(np.random.rand(len(parameters)) - 0.5)
    axd.plot(parameters + jitter, durations/60, 'o',  color='C0')
    axd.plot(param_values, mean_durations/60, '-',  color='C0')
    axd.set_xlabel(xlabel)
    axd.set_ylabel('duration [h]')
    axd.set_xlim(0, max_x)
    axd.set_ylim(0, 50)
    axc.plot(parameters + jitter, 1000*currents, 'o',  color='C0')
    axc.plot(param_values, 1000*mean_currents, '-',  color='C0')
    axc.plot(line_x, 1000*line_y, color='C1')
    axc.set_xlabel(xlabel)
    axc.set_ylabel('current [mA]')
    axc.set_xlim(0, max_x)
    axc.set_ylim(0, 500)
    axp.plot(parameters + jitter, currents*volt, 'o', color='C0')
    axp.plot(param_values, mean_currents*volt, '-', color='C0')
    axp.plot(line_x, line_y*volt, color='C1')
    axp.set_xlabel(xlabel)
    axp.set_ylabel('power [W]')
    axp.set_xlim(0, max_x)
    axp.set_ylim(0, 2)
    plt.show()

    
def plot_categories(brand, parameters, durations, currents,
                    param_values, mean_durations, mean_currents,
                    xticks):
    volt = 3.3 # V
    fig, (axd, axc, axp) = plt.subplots(1, 3, layout='constrained')
    fig.suptitle(brand)
    jitter = 0.5*(np.random.rand(len(parameters)) - 0.5)
    axd.plot(parameters + jitter, durations/60, 'o',  color='C0')
    axd.plot(param_values,  mean_durations/60, '-',  color='C0')
    axd.xaxis.set_major_locator(plt.FixedLocator(np.arange(len(param_values))))
    axd.xaxis.set_major_formatter(plt.FixedFormatter(xticks))
    plt.setp(axd.xaxis.get_majorticklabels(), rotation=45)
    axd.set_ylabel('duration [h]')
    axd.set_xlim(-0.5, len(param_values) - 0.5)
    axd.set_ylim(0, 50)
    axc.plot(parameters + jitter, 1000*currents, 'o',  color='C0')
    axc.plot(param_values, 1000*mean_currents, '-',  color='C0')
    axc.xaxis.set_major_locator(plt.FixedLocator(np.arange(len(param_values))))
    axc.xaxis.set_major_formatter(plt.FixedFormatter(xticks))
    plt.setp(axc.xaxis.get_majorticklabels(), rotation=45)
    axc.set_ylabel('current [mA]')
    axc.set_xlim(-0.5, len(param_values) - 0.5)
    axc.set_ylim(0, 500)
    axp.plot(parameters + jitter, currents*volt, 'o', color='C0')
    axp.plot(param_values, mean_currents*volt, '-', color='C0')
    axp.xaxis.set_major_locator(plt.FixedLocator(np.arange(len(param_values))))
    axp.xaxis.set_major_formatter(plt.FixedFormatter(xticks))
    plt.setp(axp.xaxis.get_majorticklabels(), rotation=45)
    axp.set_ylabel('power [W]')
    axp.set_xlim(-0.5, len(param_values) - 0.5)
    axp.set_ylim(0, 2)
    plt.show()

    
def analyze_rate_power(brand, data, capacity):
    volt = 3.3 # V
    max_rate = 100
    durations, currents, sampling_rates = analyze_currents(data, capacity)
    durs, curs, rates  = mean_currents(durations, currents, sampling_rates)
    r = linregress(sampling_rates, currents)
    line_x = np.linspace(0, max_rate, 10)
    line_y = line_x*r.slope + r.intercept
    print(f'{brand}:')
    print(f'  sampling rate of 24kHz consumes {1000*(curs[1] - curs[0]):3.0f}mA less than 48kHz')
    print(f'  sampling rate of 96kHz consumes {1000*(curs[2] - curs[1]):3.0f}mA more than 48kHz')
    plot_regression(brand, sampling_rates, durations, currents,
                    rates, durs, curs,
                    line_x, line_y, 'sampling rate [kHz]', max_rate)
    print()

    
def analyze_cpu_power(brand, data, capacity):
    volt = 3.3 # V
    max_speed = 650
    durations, currents, speeds = analyze_currents(data, capacity)
    durs, curs, cpus = mean_currents(durations, currents, speeds)
    r = linregress(speeds, currents)
    line_x = np.linspace(0, max_speed, 10)
    line_y = line_x*r.slope + r.intercept
    print(f'{brand}:')
    print(f'  CPU speed draws {1e6*r.slope:3.0f}uA/MHz    of current: {1e3*r.slope*volt:.2f}mW')
    print(f'  CPU speed draws {1e3*r.slope*600:3.0f}mA/600MHz of current: {r.slope*600*volt:.2f}W')
    plot_regression(brand, speeds, durations, currents,
                    cpus, durs, curs,
                    line_x, line_y, 'CPU speed [MHz]', max_speed)
    print()

             
def analyze_usb_power(brand, data, capacity):
    volt = 3.3 # V
    durations, currents, usbss = analyze_currents(data, capacity)
    durs, curs, usbs = mean_currents(durations, currents, usbss)
    print(f'{brand}:')
    print(f'  Serial.end()   spares {1000*(curs[0] - curs[1]):.0f}mA of current: {(curs[0] - curs[1]):.2f}W')
    print(f'  shutdown_usb() spares {1000*(curs[0] - curs[2]):.0f}mA of current: {1000*(curs[0] - curs[2]):.2f}mW')
    plot_categories(brand, usbss, durations, currents,
                    usbs, durs, curs, ['none', 'Serial.end()', 'shutdown_usb()'])
    print()

             
def analyze_channel_power(brand, data, capacity):
    volt = 3.3 # V
    max_chans = 18
    durations, currents, channels = analyze_currents(data, capacity)
    durs, curs, chans = mean_currents(durations, currents, channels)
    r = linregress(channels, currents)
    line_x = np.linspace(0, max_chans, 10)
    line_y = line_x*r.slope + r.intercept
    c16 = r.intercept + r.slope*16
    print(f'{brand}:')
    print(f'  Teensy draws {1000*r.intercept:.0f}mA of current')
    print(f'  Each pcm chip draws {1000*r.slope*4:.0f}mA of current')
    print(f'  16 channels draw {1000*c16:.0f}mA of current: {c16*volt:.2f}W')

    plot_regression(brand, channels, durations, currents,
                    chans, durs, chans,
                    line_x, line_y, 'channels', max_chans)
    print()


def analyze_sdspi_power(brand, data, capacity):
    volt = 3.3 # V
    durations, currents, usedspi = analyze_currents(data, capacity)
    durs, curs, spis = mean_currents(durations, currents, usedspi)
    print(f'{brand}:')
    print(f'  Additional SD card on SPI bus draws {1000*(curs[1] - curs[0]):.0f}mA of current: {(curs[1] - curs[0])*volt:.2f}W')
    plot_categories(brand, usedspi, durations, currents,
                    spis, durs, curs, ['none', 'backup SD'])
    print()


analyze_cpu_power(anker_brand, anker_cpu_data, anker_capacity)
analyze_sdspi_power(anker_brand, anker_sdspi_data, anker_capacity)
analyze_usb_power(anker_brand, anker_usb_data, anker_capacity)
analyze_rate_power(anker_brand, anker_rate_data, anker_capacity)
analyze_channel_power(anker_brand, anker_channel_data, anker_capacity)
analyze_channel_power(keep_brand, keep_channel_data, keep_capacity)

