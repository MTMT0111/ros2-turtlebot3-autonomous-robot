import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class AvoidObstacle(Node):

    def __init__(self):
        super().__init__('avoid_obstacle')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.get_logger().info('avoid_obstacle started')

    def clean_distance(self, value):
        if math.isinf(value) or math.isnan(value):
            return 10.0
        return value

    def scan_callback(self, msg):
        cmd = Twist()

        total = len(msg.ranges)
        front = self.clean_distance(msg.ranges[total // 2])
        left = self.clean_distance(msg.ranges[(total * 3) // 4])
        right = self.clean_distance(msg.ranges[total // 4])

        if front < 0.7:
            cmd.linear.x = 0.0
            if left > right:
                cmd.angular.z = 0.4
            else:
                cmd.angular.z = -0.4
        else:
            cmd.linear.x = 0.12
            cmd.angular.z = 0.0

        self.publisher_.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = AvoidObstacle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()