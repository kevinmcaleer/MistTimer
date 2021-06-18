# Cameleon Mist for Pico
# Kevin McAleer
# June 2021
# Save this file as main.py on the pico for it to automatically run

from machine import Pin
from utime import sleep, ticks_ms

relay_pin = Pin(12, Pin.OUT)

# Timer settings
sleep_seconds = 20 # the number of seconds to keep the relay on for
cycle_time = 240 # number of minutes (4 hours = 60 * 4 )
cycle_time_in_milliseconds = cycle_time * 60 * 1000 #convert to milliseconds

def switch_on_relay():
    """ This will switch on the relay for the number of seconds in 'sleep_seconds' """
    print("Spraying mist now, for", sleep_seconds, "seconds")

    # switch the relay on to mist the tank
    relay_pin.on() 
    sleep(sleep_seconds)
    relay_pin.off()

    print("Spray turned off.")

# get the current time
start_time = ticks_ms()

# The main program loop - will run forever
while True:
    current_ms = ticks_ms()
    countdown = (start_time + cycle_time_in_milliseconds) - current_ms
    print("current time is:", current_ms, round(countdown/1000/60,1), ", minutes to go")
    sleep(1)
    
    # check if the current time is greater than our cycle time
    if current_ms >= (start_time + cycle_time_in_milliseconds):
        
        print("its mist time!")
        # switch on the relay
        switch_on_relay()

        # set the start time to now
        start_time = ticks_ms()

