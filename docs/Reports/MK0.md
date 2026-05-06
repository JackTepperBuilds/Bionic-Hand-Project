# MK0 - Ada Hand ([Open Source](https://github.com/Open-Bionics/Ada_3D_model_files/tree/master/STLs/Right%20Hand), 5 DOF)

Brief description of what MK0 is and what was achieved including challenges faced.

## Bill of Materials
See BOM folder for full parts list and costs.

## Code
See Firmware folder. Built with Python, OpenCV, MediaPipe on Raspberry Pi 5.

## Images
See Images folder for wiring and build layout.

## Vidoes
See Videos folder for links to tests and demos.

## Demo
[Watch on YouTube](https://www.youtube.com/watch?v=RLUshVP_gwQ) - Keyboard input

[Watch on YouTube](https://www.youtube.com/shorts/l--I8Azhv_0) - Gesture Recognition

## Challenges
Some challenges I came across were improper alignment with the servo horn and servo motor. At first when trying to run my hand I came across an issue where the finger wasn't being pulled down enough by the servo. Some ways I tried to overcome this obstacle were completely taking apart the inside of the palm thinking that there was friction on the tendons
preventing full movement of the fingers. However, after some trial and error that didn't fix my issue. Once I found out trying to move the tendon system around didnt work I tried changing the pulse signals thinking that that would solve my issue but I quickly found out it made things worse. Finally, after much time was wasted I managed to figure out the issue and it was as simple as the servo horns needing to be rotated a little more so that the full 180 degree rotation was utilized when pulling the fingers.

A second challenge was trying to get the Raspberry Pi camera and MediaPipe to work cohesively. When I say cohesively I mean getting a frame that was captured through the camera and passing it into MediaPipe to be recognized. These issues were solved by looking at documentation and online code examples. I utilized a generator for capturing the frames and threading for MediaPipe so that the recognition loop could run with my main loop.

I also encountered some GitHub authentication issues when trying to push and pull needing to continuously type my username and password. However, I managed to fix this by generating an access token. I also happened to come across some library installation issues when trying to run MediaPipe. I managed to solve this issue by downgrading to an earlier version, one being TensorFlow for example.

## Lessons Learned
After completing MK0 I have learned that there are some limitations with my bionic hand. One of which includes the design of the hand itself.
The hand created by OpenBionics is meant to be printed in TPU allowing the fingers to bend naturally instead of needing joints. 
However, because there are no joints the movements of the fingers are more stiff and less dexterous than if there were joints.
Another notable lesson I learned is the importance of proper tendon routing. While the printed hand was made by OpenBionics, the rest of 
the bionic hand design was originally done by me. Because of this, the inside of the hand doesn't have a proper tendon routing system. While the 
PTFE tubing I used for the tendon system helped with the flawed design and reduced friction on the fishing line a better tendon workflow and servo
enclosure would allow better torque with the servos and movement of the fingers. Additionally, the servo enclosure lacked sufficient space to secure 
hex nuts to the screws, making it difficult to properly fasten the servo motors.

## What will change for MK1
I plan to bring the experiences I faced from MK0 and make a better bionic hand (MK1). One of the issues I said I faced was the fact that the hand I was using for MK0 was largely printed in TPU and its lack of joints was what was holding it back from moving fully and being as dexterous as it could have been. These functionality issues will be resolved when using the opensource Legacy - Orca V1 hand [Link to site](https://www.orcahand.com/legacy/files). I will be utilizing the palm of their build which uses bearings which snap together onto the hand acting as joints. The build will consist of the Orca hand, my own designed timed pulley and belt wrist system specifically sized for my MG995 servos, and a custom designed servo enclosure also specifically designed for the MG995 servos.

The hand will also come with more DOF, 17 to be exact compared to the original 5 DOF with the MK0. The increased DOF will allow more complex gestures
and better dexterity. MK0 had issues gripping objects and was overall very weak, however, MK1 will be much stronger and more functional.
The opensource hand also features a more complex tendon routing system where all 32 tendon holes will be routed with PTFE tubing limiting friction as much
as possible allowing for as much torque as possible from the servos for pulling the fingers. Creating my own servo enclosure for the MG995 servos will also 
allow me to fix my biggest issue with the MK0 enclosure which was there not being enough room for hex nuts to properly secure the servos into the enclosure.
