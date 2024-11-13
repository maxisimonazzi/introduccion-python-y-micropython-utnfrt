import machine
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))

print('\033[2J\033[H') # Limpiamos la pantalla
print('Escaneando bus I2C en busca de dispositivos...\n')
devices = i2c.scan()

if len(devices) == 0:
  print("No se encontraron dispositivos I2C conectados.\n")
else:
  print(f'Se encontraron {len(devices)} dispositivos conectados.\n')

  for i in range(len(devices)):  
    print(f'Dispositivo {i+1}, direccion en decimal: {devices[i]} | direccion en hexa {hex(devices[i])}')
