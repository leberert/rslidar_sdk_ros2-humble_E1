from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    rviz_config = get_package_share_directory('rslidar_sdk') + '/rviz/rviz2.rviz'

    return LaunchDescription([

        DeclareLaunchArgument(
            'ext_config',
            default_value='',
            description='Path to the external config file'
        ),

        Node(
            package='rslidar_sdk',
            executable='rslidar_sdk_node',
            name='rslidar_sdk_node',
            output='screen',
            arguments=['--ext_config', LaunchConfiguration('ext_config')]
        ),

        Node(namespace='rviz2', package='rviz2', executable='rviz2', arguments=['-d', rviz_config]),

        Node(package='tf2_ros', executable='static_transform_publisher',
             arguments=['--x', '0', '--y', '0', '--z', '1.5',
                        '--roll', '0.0', '--pitch', '0.0', '--yaw', '0.0',
                        '--frame-id',
                        'world',
                        '--child-frame-id',
                        'rslidar'
                        ])

    ])
