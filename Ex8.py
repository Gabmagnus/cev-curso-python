metro = float(input('Medida em metros: '))

print('A medida de {}M corresponde a\n{}Km\n{}hm\n{}Dam\n{}dm\n{}cm\n{}mm'.format(metro, metro/1000, metro/100, metro/10, metro*10, metro*100, metro*1000))