import datetime
import imp
import locale
import openpyxl
import pprint


dt_now = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, '')

print(dt_now.strftime('%m_%d_%H_%M'))

