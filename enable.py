import winreg

medic = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\WaaSMedicSvc')
winreg.SetValueEx(medic, 'Start', 0, winreg.REG_SZ, '1')
medic.Close()
wua = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\wuauserv')
winreg.SetValueEx(wua, 'Start', 0, winreg.REG_SZ, '1')
wua.Close()