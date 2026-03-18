from launch import LaunchDescription
from launch.actions import ExecuteProcess


def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'ros2', 'launch',
                'turtlebot3_cartographer',
                'cartographer.launch.py',
                'use_sim_time:=True'
            ],
            output='screen'
        )
    ])