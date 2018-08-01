#For each year of data
#Find the amount of days from the start of the year
#Plot the amount of days against the corresponding flows
#Best fit exponential line
#Extract constants
#Dates are passed in as a string in dd/mm/yyyy format
import numpy

def days_from_start(date_list):
    '''
    Calculates the amount of days from the start of the year
    :param date_list: a list of dates in format dd/mm/yy as string
    :return: a list of amount of days from the start of the year
    '''
    month_day_dict = {'1':31, '2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}
    days_from_start_result = []
    for date in date_list:
        days = 0
        month = 1
        while month != date.month:
            days += month_day_dict[str(month)]
            month += 1
        days += date.day
        days_from_start_result.append(days)
    return days_from_start_result

def fit_curve(days_list, flow_list):
    '''
    Fits the data to an exponential curve
    :param days_list: list of days from start of year: x_axis
    :param flow_list: list of corresponding flows: y_axis
    :return: a tuple of the equation constants
    '''
    constant_list = numpy.polyfit(days_list, numpy.log(flow_list), 1)
    return numpy.exp(constant_list[1]), constant_list[0]

def find_flow(constants_tuple, day):
    '''
    Calculates the flow at a particular day using exponential decay
    :param constants_tuple: a tuple of exponential constants
    :param day: day to find flow on
    :return: flow on particular day
    '''
    a = constants_tuple[0]
    b = constants_tuple[1]
    flow = round(a * numpy.exp(b * day), 3)
    return flow

def recession(flow_dict):
    '''
    Splits dict into lists of years and flows
    :return: tuple of lists
    '''
    month_list = []
    flow_list = []
    single_month = []
    single_flow = []
    minimum_flows = []
    for x in flow_dict.keys():
        #if month list is empty or next value is in same year
        if len(month_list) == 0 or month_list[-1].year == x.year:
            month_list.append(x)
            flow_list.append(flow_dict[x])
        else:
            if len(month_list) == 1:
                single_month.append(month_list[-1].year)
                single_flow.append(flow_list[-1])
            else:
                # year = month_list[-1].year
                x_array = days_from_start(month_list)
                equation_constants = fit_curve(x_array, flow_list)
                flow = find_flow(equation_constants, 150)
                # gallons = round(flow * 200 * 86400/ 1000000, 2)
                minimum_flows.append(flow)
            month_list.clear()
            flow_list.clear()
    return minimum_flows

def flow_freq(flows):
    '''
    Generate the probability streamflows
    Parameters:
    flows: A list of 150 day flows
    returns: a dictionary of return period keys with the frequency streamflow
            by return period
    '''
    flows150 = []
    K = {1:3.137, 2:2.592, 4:2.044, 10:1.305, 20:0.719, 50:-0.164, 80:-0.821, 90:-1.100}
    for year in K.keys():
        tempdict = {"x":year, "y":round(numpy.mean(flows) + K[year] * numpy.std(flows), 2)}
        flows150.append(tempdict)
    return flows150
