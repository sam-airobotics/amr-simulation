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
