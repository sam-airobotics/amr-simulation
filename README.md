# 🚀 ROS2 AMR Simulation

This project focuses on building and simulating a simple **Autonomous Mobile Robot (AMR)** using ROS2 and Gazebo.

The simulation environment is designed for understanding the core concepts of mobile robotics, robot control, sensor integration, and robot visualization in a realistic simulation setup.

---

# 🤖 AMR Robot

<ul>
<li>A simple Differential Drive Autonomous Mobile Robot (AMR).</li>
<li>Built for ROS2 and Gazebo simulation.</li>
<li>Modular and easy to expand for advanced robotics applications.</li>
</ul>

![AMR](images/amr_rviz.png)
![AMR](images/amr_gazebo.png)

---

# 🌍 Simulation Environments

## 🟢 Basic Simulation World

A minimal environment for testing robot motion and control.

### Features
- Differential drive motion
- Keyboard teleoperation
- ROS2 `/cmd_vel` control
- Gazebo simulation support

### Purpose
- Robot movement testing
- Velocity control validation
- Simulation environment setup

![Clean World](images/clean_world_gz_sim.png)

---

## 🟡 Obstacle Environment

A world containing obstacles for testing robot interaction and movement behavior.

### Features
- Static obstacles
- Narrow passages
- Turning and maneuvering tests

### Purpose
- Obstacle interaction
- Motion behavior analysis
- Navigation testing

![Obstacle World](images/obstacle_world_gz_sim.png)

---

## 🔵 Sensor Environment

A structured environment for testing robot sensors and visualization.

### Features
- Lidar integration
- RViz visualization
- `ros2 bag` recording and playback
- Sensor data streaming

### Purpose
- Sensor simulation
- Data visualization
- Perception system testing

![Sensor World](images/sensor_world_gz_sim.png)

---

# 🎯 Project Goals

- Develop a simple AMR simulation platform
- Explore ROS2 and Gazebo integration
- Simulate robot movement and sensing
- Provide a foundation for autonomous robotics development
- Support future navigation and perception systems

---

# ⚙️ Requirements

- ROS2 Jazzy (or compatible)
- Gazebo Sim
- Python
- RViz2

---

# ▶️ Running the Simulation

```bash
# Build workspace
colcon build

# Source workspace
source install/setup.bash

# Launch simulation
ros2 launch amr_description sim.launch.py

#Launch Mapping
ros2 launch amr_slam online_async_launch.py

# Control robot
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

<h2>AMR Simulation Status</h2>

<h3>✅ Completed</h3>
<ul>
    <li>Robot model visualized in RViz.</li>
    <li>Camera sensor integrated and visualized.</li>
    <li>LiDAR sensor integrated and visualized.</li>
    <li>Map generation working using <code>amr_slam</code>.</li>
    <li>Occupancy map can be viewed in RViz.</li>
</ul>

![AMR in RViz](images/amr_camera_lidar.png)
![AMR in World](images/amr_world_lidar.png)

<h3>⚠️ Current Issues</h3>
<ul>
    <li>Robot movement via <code>teleop_twist_keyboard</code> is unstable.</li>
    <li>Collision geometries are inaccurate.</li>
    <li>Robot exhibits irregular motion in Gazebo.</li>
    <li>Reliable and accurate mapping is not yet possible.</li>
</ul>

![AMR Mapping](images/amr_mapping_ongoing.png)
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/9c33b825-2532-46b7-96a8-413d8e94b024" />

<h3>🔧 Next Steps</h3>
<ul>
    <li>Fix wheel and chassis collision models.</li>
    <li>Tune robot dynamics and friction parameters.</li>
    <li>Debug DiffDrive configuration.</li>
    <li>Improve odometry and motion stability.</li>
</ul>

