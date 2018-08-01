import numpy

def short_int(dailyRain):
    '''
    Creates lists of short duration rainfall for 5, 10, 20, 30, 60,
    2hr, 3hr, 6hr, 12hr, 24hr

    dailyRain: list of maximum daily rainfall amounts
    '''
    short = {5:[], 10:[], 15:[], 20:[], 25:[], 30:[], 60:[], 120:[], 180:[], 360:[], 720:[], 1440:[]}
    for key in short.keys():
        for val in dailyRain:
            short[key].append(round((val*((key/60)/24)**(1/3))/key*60, 2))
    return short


def freq_int(short):
    '''
    Create a list of rainfall intensities based on return period
    This is to create the graph
    '''
    K = {2:-0.164, 5:0.719, 10:1.305, 25:2.044, 50:2.592, 100:3.137}
    periods = {2:[], 5:[], 10:[], 25:[], 50:[], 100:[]}

    for year in K.keys():
        for duration in short.values():
            periods[year].append(round(numpy.mean(duration) + K[year] * numpy.std(duration)))
    return periods

def dur_freq(short):
    '''
    Create a list of rainfall intensities based on return period
    This is for display pruposes in the table
    Parameters:
    short: a dictionary of duration keys with the short duration rainfall
            calculated for each year
    returns: a dictionary of duration keys with the frequency rainfall
            by return period
    '''
    duration_rainfall = {5:[], 10:[], 15:[], 20:[], 25:[], 30:[], 60:[], 120:[], 180:[], 360:[], 720:[], 1440:[]}
    K = {2:-0.164, 5:0.719, 10:1.305, 25:2.044, 50:2.592, 100:3.137}
    for duration in short.keys():
        for year in K.keys():
            duration_rainfall[duration].append(round(numpy.mean(short[duration]) + K[year] * numpy.std(short[duration]), 2))
    return duration_rainfall

def ddf_int(dailyRain):
    '''
    Depth-Duration-Frequency. No dividing by time.
    '''
    short = {5:[], 10:[], 15:[], 20:[], 25:[], 30:[], 60:[], 120:[], 180:[], 360:[], 720:[], 1440:[]}
    for key in short.keys():
        for val in dailyRain:
            short[key].append(round(val*((key/60)/24)**(1/3), 2))
    return short
