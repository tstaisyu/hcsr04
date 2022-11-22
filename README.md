# 実行

sudo chmod 777 /dev/gpiomem  
cd /ros2_my_python_ws  
colcon build  
source install/setup.bash  
ros2 run hcsr04 talker  
ros2 run hcsr04 listener

