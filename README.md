the best concept for a lora network with lilygo is to take a lilygo without and sensor and load micropython + freakwan. thsi computer will recieve data all lora lilygo with sensor.
for sensor

how to connect a sensor to lilygo.

it depends of sensor, if it is a sensor like dht11, as i had to test, just change the name the default (DHT22) in the sensor you use.
we need only th change 2 files sensor.py and wan_config.py.

if it is a sensor with a I2C connection, we must chang a lot see sensor.py


lilygo as access point

see the file accesspoint.py
