from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os


def generate_launch_description():
    map_file = os.path.expanduser('~/ros2_ws/src/my_robot/maps/my_map.yaml')

    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'ros2', 'launch',
                'turtlebot3_navigation2',
                'navigation2.launch.py',
                f'map:={map_file}',
                'use_sim_time:=True'
            ],
            output='screen'
        )
    ])