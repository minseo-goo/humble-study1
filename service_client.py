#!/usr/bin/env python3
"""5-1, 5-2 스크립트 버전: /turtle1/teleport_absolute 서비스 호출."""
import rclpy
from turtlesim.srv import TeleportAbsolute


def main():
    rclpy.init()
    node = rclpy.create_node('client_test')
    cli = node.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')

    while not cli.wait_for_service(timeout_sec=1.0):
        print('Waiting for service...')

    req = TeleportAbsolute.Request()
    req.x = 9.0
    req.y = 9.0
    req.theta = 1.57

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    print(future.result())

    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
