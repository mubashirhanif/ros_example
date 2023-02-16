import rclpy
from rclpy.node import Node

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class Runner(Node):
    def __init__(self, a: Point, b: Point):
        super().__init__("example_node")
        self.algorithm(a, b)

    def algorithm(self, a: Point, b: Point):
        print(a)
        print(b)
        pass

def main(*args, **kwargs):
    rclpy.init()
    a = Point(0,0)
    b = Point(2,2)
    node : Node = Runner(a, b)
    node.get_logger().info(f"{args} --------- {kwargs}")
    while rclpy.ok():
        rclpy.spin_once(node=node, timeout_sec=0.1)
    rclpy.shutdown()