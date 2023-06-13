import netmiko

cisco1 = {
    "ip": "192.168.152.129",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",
}

# Comando para obtener información de IP y estado de las interfaces
interface_command = "show ip interface brief"

# Comando para obtener el running-config
running_config_command = "show running-config"

# Comando para obtener el show version
show_version_command = "show version"

with netmiko.ConnectHandler(**cisco1) as net_connect:
    print("1. IP y estado de las interfaces")
    print("2. Running-config")
    print("3. Show version")
    option = input("Seleccione una opción (1-3): ")

    if option == "1":
        # Obtener información de IP y estado de las interfaces
        interface_output = net_connect.send_command(interface_command)
        print("IP y estado de las interfaces:")
        print(interface_output)
    elif option == "2":
        # Obtener el running-config
        running_config_output = net_connect.send_command(running_config_command)
        print("Running-config:")
        print(running_config_output)
    elif option == "3":
        # Obtener el show version
        show_version_output = net_connect.send_command(show_version_command)
        print("Show version:")
        print(show_version_output)
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1-3).")

