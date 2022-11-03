import machine
import utime

sensor_pin = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(15, machine.Pin.OUT)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("Alarm!! something is transpassing")
        for i in range(50):
            buzzer.toggle()
            utime.sleep_ms(100)

sensor_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)