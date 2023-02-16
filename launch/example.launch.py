from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    example = Node(
        package="example",
        name=f"example",
        executable=f"example",
    )
    ld.add_action(example)

    return ld