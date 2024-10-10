import pandas as pd
import sys
# temporary hack until I get access to the processing code repo 
sys.path.append("/mnt/vsi-db/Measurements/SAXS002/processingCode/source")
from SAXSClasses import readLog

rL = readLog("/mnt/vsi-db/Measurements/SAXS002/logbooks/Logbook_MAUS.xls")
rL._dropThresh = 6  # GISAXS and mapping positions have fewer than 12
                    # columns filled
sampleenv = rL.read(sheetName=1)
sampleenv.set_index("sampos", inplace = True)
#print(sampleenv.columns)
