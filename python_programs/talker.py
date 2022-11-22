import time
import RPi.GPIO as GPIO
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from std_msgs.msg import String


class Talker(Node):

    def __init__(self):
        super().__init__('talker')
        self.i = 0
        self.pub = self.create_publisher(String, 'chatter', 10)
        timer_period = 1.0
        self.tmr = self.create_timer(timer_period, self.time_callback)

    def reading(self, sensor):
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BOARD)
        TRIG = 11
        ECHO = 13

        if sensor == 0:
            GPIO.setup(TRIG,GPIO.OUT)
            GPIO.setup(ECHO,GPIO.IN)
            GPIO.output(TRIG, GPIO.LOW)
            time.sleep(0.3)

            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            while GPIO.input(ECHO) == 0:
              signaloff = time.time()

            while GPIO.input(ECHO) == 1:
              signalon = time.time()

            timepassed = signalon - signaloff
            distance = timepassed * 17000
            return distance
            GPIO.cleanup()
        else:
            print ("Incorrect usonic() function varible.")

    def time_callback(self):
        msg = String()
        msg.data = 'Hello World: "{0}"'.format(self.reading(0))
        self.get_logger().info('Publishing: "{0}"'.format(msg.data))
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = Talker()

    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()

