from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_path = get_package_share_directory('ros2_gazebo_simulation_tutorial')

    world_file = os.path.join(pkg_path, 'worlds', 'sensor_world.sdf')
    urdf_file = os.path.join(pkg_path, 'urdf', 'amr.urdf')

    return LaunchDescription([

        # Start Gazebo with sensor world
        ExecuteProcess(
            cmd=['gz', 'sim', world_file],
            output='screen'
        ),

        # Spawn robot
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-file', urdf_file,
                '-entity', 'amr'
            ],
            output='screen'
        )
    ])
