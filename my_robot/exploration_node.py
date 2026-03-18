import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid


class ExplorationNode(Node):
    def __init__(self):
        super().__init__('exploration_node')

        self.subscription = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10
        )

        self.get_logger().info('exploration_node started, waiting for /map ...')

    def is_frontier(self, data, width, height, x, y):
        index = y * width + x

        # frontier 条件1：当前点必须是未知区域
        if data[index] != -1:
            return False

        # frontier 条件2：它周围至少有一个已知空闲区域
        neighbors = [
            (x - 1, y), (x + 1, y),
            (x, y - 1), (x, y + 1)
        ]

        for nx, ny in neighbors:
            if 0 <= nx < width and 0 <= ny < height:
                n_index = ny * width + nx
                if data[n_index] == 0:
                    return True

        return False

    def map_callback(self, msg):
        width = msg.info.width
        height = msg.info.height
        data = msg.data

        frontier_count = 0

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                if self.is_frontier(data, width, height, x, y):
                    frontier_count += 1

        self.get_logger().info(
            f'map received: size={width}x{height}, frontier cells={frontier_count}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = ExplorationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()