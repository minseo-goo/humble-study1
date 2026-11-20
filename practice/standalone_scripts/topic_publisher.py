#!/usr/bin/env python3
"""4-3 스크립트 버전: /turtle1/cmd_vel 을 0.1초 주기로 4번 발행하고 종료."""
import rclpy
from geometry_msgs.msg import Twist


def main():
    rclpy.init()
    node = rclpy.create_node('pub_test')
    pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    msg = Twist()
    msg.linear.x = 2.0
    msg.angular.z = 2.0
    count = {'n': 0}

    def timer_callback():
        count['n'] += 1
        print(count['n'])
        pub.publish(msg)
        if count['n'] > 3:
            raise SystemExit

    node.create_timer(0.1, timer_callback)
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
