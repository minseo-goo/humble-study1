#!/usr/bin/env python3
"""4-1, 4-2 스크립트 버전: /turtle1/pose 를 3번 받고 종료."""
import rclpy
from turtlesim.msg import Pose


def main():
    rclpy.init()
    node = rclpy.create_node('test')
    count = {'n': 0}

    def callback(data):
        count['n'] += 1
        print(count['n'], data.x, data.y)
        if count['n'] >= 3:
            raise SystemExit

    node.create_subscription(Pose, '/turtle1/pose', callback, 10)
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
