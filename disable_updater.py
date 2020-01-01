import winreg

key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\wuauserv')
winreg.SetValueEx(key, 'Start', 0, winreg.REG_SZ, '4')
key.Close()