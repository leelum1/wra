from django.apps import apps
from django.db.models import Max, Sum, Count
from .rainfallstats import raingauges
import numpy
from datetime import datetime

def rainStatsCalc():
    with open("rainstats.csv", 'w') as f:
        for gauge in raingauges:
            current_model = apps.get_model('data_app', gauge)
            record_start = current_model.objects.order_by('date').first().date
            record_end = current_model.objects.order_by('date').last().date

            #Daily max
            dailymax = current_model.objects.get(rainfall=current_model.objects.aggregate(Max('rainfall'))['rainfall__max'])
            dailydate = datetime.strftime(dailymax.date, '%Y-%m-%d')
            dailystr = str(dailymax.rainfall) + ", " + str(dailydate)

            #Average and Maximum Yearly
            avg_rainfall = []
            max_year = (0, 0)
            for year in range(record_start.year, record_end.year + 1):
                max_rain = current_model.objects.filter(date__year=year).aggregate(Sum('rainfall'))['rainfall__sum']
                if max_rain != None and max_rain > max_year[1]:
                    max_year = (year, round(max_rain, 1))
                if max_rain != None and max_rain > 800:
                    avg_rainfall.append(max_rain)
            yearaverage = round(sum(avg_rainfall)/len(avg_rainfall), 1)
            yearstats = str(yearaverage) + ", " + str(max_year[1]) + ", " + str(max_year[0])

            # #Monthly Stats
            # #Need to average each month, and then average those averages
            # #Use a for loop to cycle through each month, and a nested for loop to cycle through each year
            # #Add each to list and clear list after each month to be reused
            month_avg = ""
            month_max = ""
            for month in range(1, 13):
                temp_avg = []
                temp_max = 0
                for year in range(record_start.year, record_end.year + 1):
                    sum_month_rain = current_model.objects.filter(date__year = year, date__month=month).aggregate(Sum('rainfall'))['rainfall__sum']
                    count_month_rain = current_model.objects.filter(date__year = year, date__month=month).aggregate(Count('rainfall'))['rainfall__count']
                    if sum_month_rain != None and count_month_rain > 25:
                        temp_avg.append(numpy.mean(sum_month_rain))
                        if sum_month_rain > temp_max:
                            temp_max = sum_month_rain
                month_max += str(round(temp_max,1)) + ", "
                month_avg += str(round(numpy.mean(temp_avg), 1)) + ", "

            line = str(gauge) + ", " + dailystr + ", " + yearstats + ", " + month_avg + month_max + "\n"
            f.write(line)
