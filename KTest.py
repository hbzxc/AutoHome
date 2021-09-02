import smbus2
import bme280

port = 1
address = 0x77
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
print('Data ID: %d' % data.id)
print('Date: %s' % str(data.timestamp))
print("Temperature: %s0.2fC" % str(round(data.temperature,2)).strip("0"))
print('Pressure: %s0.2fHg' % str(round((data.pressure/33.86),2)).strip("0"))
print('Humidity: %s%%' % str(round(data.humidity,2)).strip("0"))

# there is a handy string representation too
print(data)