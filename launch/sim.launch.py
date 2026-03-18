from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os


def generate_launch_description():
    turtlebot3_model = os.environ.get('TURTLEBOT3_MODEL', 'burger')

    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'ros2', 'launch',
                'turtlebot3_gazebo',
                'turtlebot3_world.launch.py'
            ],
            output='screen'
        )
    ])