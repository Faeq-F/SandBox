import wmi
import os

c = wmi.WMI ()
for p in c.Win32_Process (Name="BatchIconExtractor.exe"):
    os.system("taskkill /im BatchIconExtractor.exe")
