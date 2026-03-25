from pysimverse import Drone
drone = Drone()
drone.connect()

drone.take_off
left_right = 6 
forward_backward = 0
up_down = 0
yaw = 0.1

drone.send_rc_control(
    left_right,
    forward_backward,
    up_down,
    yaw
    )
    

    
