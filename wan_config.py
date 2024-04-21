michel@ubu220401:~/microProssermi/pyserialmi/micropythonmi/freakwan-venv/freakwan_20240408/freakwanCo2Sensor/fromUsb$ sudo ../../../../../../talk32mi/talk32/talk32 /dev/ttyACM1 get wan_config.py
### IMPORTANT NOTICE
###
### Please, be aware that certain things configured in this file
### can also be configured with bang commands, like !wifi, !irc
### and so forth. After a "!config save" command, the configuration
### saved in "settings.txt" overrides what you define here.

class UserConfig:
    config = {}
    # This is just your nickname, how the network will know you.
    # If not set, a fixed one from the device mac address is
    # generated.
    #
    # config['nick']="mynickname"
    config['nick']="chris"

    # This is a status message sent using HELLO packets, to make
    # others aware of our presence. Other folks will see this message
    # when listing active nodes.
    config['status']="Hi There!"

    # LoRa configuration
    config['lora_sp']=12            # Spreading
    config['lora_bw']=250000        # Bandwidth
    config['lora_cr']=8             # Coding rate
    config['lora_fr']=869500000     # Frequency
    config['lora_pw']=17            # TX power (dbm, range 2-20)

   # WiFi network, in order to use the IRC interface.
    config['wifi'] = {
        'mynetwork1': 'mypassword',
        'ssid2': 'password2'
    }

    # WiFi network to join at startup.
    config['wifi_default_network'] = False

    # IRC configuration. Just if it is enabled or not. The channel name is
    # automatically created from the nick of the device. See README.
    config['irc'] = {
        'enabled': False
    }

    # Bluetooth. Please note that certain combinations of
    # MicroPython versions and ESP32 chips models have
    # issues. If you see the device crashing on startup try
    # to disable Bluetooth.
    config['ble_enabled'] = True

    # Goes to deep sleep when this percentage is reached, in order to
    # avoid damaging the battery.
    config['sleep_battery_perc'] = 20

    config['sensor'] = {
        'enabled': True,
        #'type': 'DHT11',
        #'type': 'co2',
        'type': 'SCD4X',
        #'dht_pin': 25,
        #'co2_pin': [21, 22],
        #'period': 30000, # In milliseconds
        #'period': 5000, # In milliseconds
        'period': 0, # In milliseconds
        'key_name': "sensor_key", # Encryption key for sensor data
        'key_secret': "123456",
    }




michel@ubu220401:~/microProssermi/pyserialmi/micropythonmi/freakwan-venv/freakwan_20240408/freakwanCo2Sensor/fromUsb$ 
