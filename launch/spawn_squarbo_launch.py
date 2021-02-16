from launch import LaunchDescription

import launch.actions
import launch_ros.actions


def generate_launch_description():

    return LaunchDescription([
        # TODO(orduno) might not be necessary to have it's own package
        launch_ros.actions.Node(
            package='squarbo_gazebo',
            executable='spawner_squarbo',
            output='screen',
            arguments=[
                '--robot_name', launch.substitutions.LaunchConfiguration('robot_name'),
                '--robot_namespace', launch.substitutions.LaunchConfiguration('robot_name'),
                '-x', launch.substitutions.LaunchConfiguration('x_pose'),
                '-y', launch.substitutions.LaunchConfiguration('y_pose'),
                '-z', launch.substitutions.LaunchConfiguration('z_pose')]),
    ])
