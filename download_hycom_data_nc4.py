"""
Baixar dados Hycom
"""
import webbrowser
import os
import datetime
import time

d0 = '2018-02-15'  #aa-mm-dd
d1 = '2018-02-18'  #aa-mm-dd+1

start = datetime.datetime.strptime(d0, "%Y-%m-%d")
end = datetime.datetime.strptime(d1, "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

dt = []
for date in date_generated:
    dt.append(date.strftime("%Y-%m-%d"))

###############################################################################
# Baixar dados ssh
###############################################################################
url = 'http://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_93.0/ssh?var=surf_el&north=-22&west=312&east=318&south=-25&horizStride=1&time_start='+dt[0]+'T00%3A00%3A00Z&time_end='+dt[len(dt)-1]+'T21%3A00%3A00Z&timeStride=1&addLatLon=true&accept=netcdf4'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
while os.path.isfile('C:\Users\Douglas Fraga\Downloads\ssh.nc4') == False:
    time.sleep(2) 
else:
    os.rename('ssh.nc4', 'ssh_'+dt[0]+'_'+dt[len(dt)-1]+'.nc4')

###############################################################################
# Baixar dados u e v
###############################################################################
for k in dt:
    url = 'http://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_93.0/uv3z?var=water_u&var=water_v&north=-22&west=312&east=318&south=-25&horizStride=1&time_start='+k+'T00%3A00%3A00Z&time_end='+k+'T21%3A00%3A00Z&timeStride=1&vertCoord=&addLatLon=true&accept=netcdf4'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    while os.path.isfile('C:\Users\Douglas Fraga\Downloads\uv3z.nc4') == False:
        time.sleep(2) 
    else:
        os.rename('uv3z.nc4', 'uv_'+k+'.nc4')

print 'FIM'