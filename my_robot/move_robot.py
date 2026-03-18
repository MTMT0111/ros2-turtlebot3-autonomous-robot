import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MoveRobot(Node):

    def __init__(self):
        super().__init__('move_robot')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        self.timer = self.create_timer(0.5, self.timer_callback)

        self.get_logger().info('move_robot 节点已启动，正在发布 /cmd_vel')

    def timer_callback(self):
        msg = Twist()

        msg.linear.x = 0.2
        msg.angular.z = 0.0

        self.publisher_.publish(msg)
        self.get_logger().info(f'发布速度: linear.x={msg.linear.x}, angular.z={msg.angular.z}')


def main(args=None):
    rclpy.init(args=args)

    node = MoveRobot()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()