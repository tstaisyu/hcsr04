# 実行

sudo chmod 777 /dev/gpiomem  
cd /ros2_my_python_ws  
colcon build  
source install/setup.bash  
ros2 run hcsr04 talker  
ros2 run hcsr04 listener

# 参考

http://make.bcde.jp/raspberry-pi/%E8%B6%85%E9%9F%B3%E6%B3%A2%E8%B7%9D%E9%9B%A2%E3%82%BB%E3%83%B3%E3%82%B5hc-sr04%E3%82%92%E4%BD%BF%E3%81%86/#
