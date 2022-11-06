"""
Baixar dados Hycom
"""
import webbrowser
import os
import datetime
import time

# Sep 1998 e Mar 1999
# 15/10/2010 a 31/01/2012
d0 = '2011-01-02'  #aa-mm-dd
d1 = '2012-02-01'  #aa-mm-dd+1

start = datetime.datetime.strptime(d0, "%Y-%m-%d")
end = datetime.datetime.strptime(d1, "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

dt = []
for date in date_generated:
    dt.append(date.strftime("%Y-%m-%d"))

###############################################################################
# Baixar dados ssh
###############################################################################
#url = 'http://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_53.X/data/'+str(d0[0:4])+'?var=surf_el&north=-22&west=-48&east=-42&south=-26&horizStride=1&time_start='+dt[0]+'T00%3A00%3A00Z&time_end='+dt[len(dt)-1]+'T21%3A00%3A00Z&timeStride=1&vertCoord=&addLatLon=true&accept=netcdf'
#
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#webbrowser.get(chrome_path).open(url)
#while os.path.isfile('C:\Users\Douglas Fraga\Downloads\\'+str(d0[0:4])+'.nc') == False:
#    time.sleep(2) 
#else:
#    os.rename(str(d0[0:4])+'.nc', 'ssh_'+dt[0]+'_'+dt[len(dt)-1]+'.nc')

###############################################################################
# Baixar dados u e v
###############################################################################
for k in dt:
    url = 'http://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_53.X/data/'+str(d0[0:4])+'?var=surf_el&var=salinity&var=water_temp&var=water_u&var=water_v&north=-22&west=-48&east=-42&south=-26&disableProjSubset=on&horizStride=1&time_start='+k+'T00%3A00%3A00Z&time_end='+k+'T21%3A00%3A00Z&timeStride=1&vertCoord=&addLatLon=true&accept=netcdf'    
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    while os.path.isfile('C:\Users\Douglas Fraga\Downloads\\'+str(d0[0:4])+'.nc') == False:
        time.sleep(2) 
    else:
        os.rename(str(d0[0:4])+'.nc', 'uv_'+k+'.nc')

print 'FIM'