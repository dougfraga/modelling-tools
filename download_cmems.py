"""
Baixar dados do MyOcean
Autor: Douglas Fraga Rodrigues
"""
import os
import datetime
import time
import numpy as np

###############################################################################
# Definir o diretório de trabalho
###############################################################################
os.chdir(r"C:\Users\Douglas Fraga\Google Drive\OCN_DEVOP\pre_processing")

storage_dir = r'C:\nc'
today = datetime.datetime.today()
start_date = (today + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
end_date = (today + datetime.timedelta(days=5)).strftime('%Y-%m-%d')

command_line = f'python3 -m motuclient --motu https://nrt.cmems-du.eu/motu-web/Motu --service-id GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS --product-id global-analysis-forecast-phy-001-024 --longitude-min -45.5 --longitude-max -43 --latitude-min -24.2 --latitude-max -22.7 --date-min "{start_date} 12:00:00" --date-max "{end_date} 12:00:00" --depth-min 0.493 --depth-max 155.8508 --variable so --variable thetao --variable uo --variable vo --variable zos --out-dir {storage_dir} --out-name cmems_{start_date}.nc --user drodrigues --pwd Fluzao841012!'

np.savetxt("download_cmems.bat", np.array(command_line).reshape(1,), fmt='%s')

os.startfile("download_cmems.bat")

while os.path.isfile(f'{storage_dir}\cmems_{start_date}.nc') == False:
    time.sleep(10)

print(u'Execução bem sucedida!') 