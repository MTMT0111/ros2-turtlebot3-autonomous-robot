import rclpy
from rclpy.node import Node


class HelloNode(Node):

    def __init__(self):
        super().__init__('hello_node')

        self.get_logger().info("Hello ROS2! 我的第一个节点启动了")


def main(args=None):

    rclpy.init(args=args)

    node = HelloNode()

    rclpy.spin_once(node, timeout_sec=1)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()