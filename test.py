import os
from elevate import elevate
import subprocess
elevate()
result = subprocess.run(['"F:\\Quokka\\assets\\Python scripts\\Everything search.exe"', 'Quokka'], stdout=subprocess.PIPE)
result.stdout
