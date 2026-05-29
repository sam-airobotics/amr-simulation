from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import SetEnvironmentVariable

from launch_ros.actions import Node

from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue

from launch.actions import TimerAction

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    # =========================
    # PACKAGE PATH
    # =========================

    pkg_path = get_package_share_directory('amr_description')

    # =========================
    # XACRO FILE
    # =========================

    xacro_file = os.path.join(
        pkg_path,
        'urdf',
        'amr.xacro'
    )

    # =========================
    # WORLD FILE
    # =========================

    world_file = os.path.join(
        pkg_path,
        'worlds',
        'clean_world',
        'model.sdf'
    )

    # =========================
    # ROBOT DESCRIPTION
    # =========================

    robot_description = ParameterValue(
        Command([
            'xacro ',
            xacro_file
        ]),
        value_type=str
    )

    #==========================
    #Resource Path set
    #==========================

    gazebo_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=os.path.join(
            pkg_path
        )
    )

    # =========================
    # GAZEBO HARMONIC
    # =========================

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': f'-r {world_file}'
        }.items()
    )

    # =========================
    # ROBOT STATE PUBLISHER
    # =========================

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',

        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True
        }],

        output='screen'
        )

    # =========================
    # JOINT STATE PUBLISHER
    # =========================

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen'
    )

    # =========================
    # SPAWN ROBOT
    # =========================

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',

        arguments=[
            '-topic',
            'robot_description',

            '-name',
            'amr',

            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.0',

            '-R', '0.0',
            '-P', '0.0',
            '-Y', '3.1415926535' 
        ],

        output='screen'
    )

    # =========================
    # JOINT STATE BROADCASTER
    # =========================

    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',

        arguments=[
            'joint_state_broadcaster'
        ],

        output='screen'
    )


    clock_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock'
        ],
        output='screen'
    )
    
    camera_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/camera/image_raw@sensor_msgs/msg/Image[gz.msgs.Image'
        ]
    )

    lidar_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan'
        ]
    )
    
    # =========================
    # LAUNCH DESCRIPTION
    # =========================

    return LaunchDescription([

        gazebo_resource_path,

        gazebo,

        robot_state_publisher,

        joint_state_publisher,

        joint_state_broadcaster_spawner,

        spawn_robot,
        
        clock_bridge,

        camera_bridge,

        lidar_bridge,

    ])
