from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():

    gazebo = ExecuteProcess(
        cmd=['ros2','launch','turtlebot3_gazebo','turtlebot3_world.launch.py'],
        output='screen'
    )

    slam = ExecuteProcess(
        cmd=['ros2','launch','turtlebot3_cartographer','cartographer.launch.py','use_sim_time:=True'],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        slam
    ])