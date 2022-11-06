"""
Baixar dados Hycom
"""
import webbrowser
import os
import datetime
import time

# Sep 1998 e Mar 1999
# 15/10/2010 a 31/01/2012
d0 = '1998-08-01'  #aa-mm-dd
d1 = '1998-08-02'  #aa-mm-dd+1

start = datetime.datetime.strptime(d0, "%Y-%m-%d")
end = datetime.datetime.strptime(d1, "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

dt = []
for date in date_generated:
    dt = date.strftime("%Y-%m-%d")

###############################################################################
# Baixar dados ssh
###############################################################################
    url = f'http://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_53.X/data/{str(dt[0:4])}?var=surf_el&var=water_u&var=water_v&north=-21.5&west=-49&east=-39.5&south=-29&disableProjSubset=on&horizStride=1&time={dt}T12%3A00%3A00Z&vertCoord=&addLatLon=true&accept=netcdf'
    
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    while os.path.isfile(r'C:\Users\Douglas Fraga\Downloads\\'+str(dt[0:4])+'.nc') == False:
        time.sleep(2) 
    else:
        os.rename(str(dt[0:4])+'.nc', f'hycom_uvh_{dt}.nc')

    print(dt)


print(u'Execução bem sucedida!') 