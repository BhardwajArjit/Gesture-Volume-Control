# Gesture Volume Control using Hand Gestures

Gesture Volume Control is an exciting project that allows you to change the volume of your system by using hand gestures. The project utilizes computer vision and audio control libraries to achieve this functionality. With Gesture Volume Control, you can have a more interactive and intuitive way to manage audio levels on your system.

![Gesture Volume Control GIF](https://github.com/BhardwajArjit/Gesture-Volume-Control/assets/109625851/8ff93da0-059a-4a4c-9f0e-1238de20e4e5)

## Overview

Gesture Volume Control is a Python-based project that uses OpenCV and Mediapipe to track hand movements and recognize hand landmarks. By measuring the distance between the index finger and thumb, the project calculates the desired volume level and adjusts it accordingly using the pycaw library. This project provides a creative way to interact with your computer's audio system and showcases the potential of computer vision in real-world applications.

## Requirements

Before running the project, ensure you have the following libraries installed:

- opencv-contrib-python 4.7.0.72
- mediapipe 0.9.1.0
- pycaw 20220416
- comtypes (a dependency for pycaw)

## Modules

### Module 1 - HandTrackingModule

This module is responsible for tracking hand movements and identifying 21 hand landmarks defined by Google in Mediapipe.

#### Function: `findHand`

This function takes a BGR image as input and converts it to RGB to highlight the 21 hand landmarks along with the connections between them.

#### Function: `findPosition`

The `findPosition` function is used to get the position of a particular landmark on the hand and highlights it by drawing a circle around it.

### Module 2 - VolumeControl

This module is the core of the project and executes the main functionality. It first detects hand movements using the HandTrackingModule. The user needs to specify the landmark numbers for the index finger (8) and thumb (4) provided by Mediapipe.

The module calculates the distance between the index finger and thumb using the `hypot` method from the `math` module. It also calculates the midpoint of the line joining these two landmarks, which changes its color below a certain range.

To implement the volume control, the `pycaw` library is used. The necessary audio initialization and volume control methods are performed on the system's default audio output. The `GetVolumeRange` method is used to determine the range of volume levels for proper conversion.

To display the volume bar on the screen, the `rectangle` method from the OpenCV library is used with appropriate dimensions.

## Setup and Execution

1. Clone this repository:

   ```bash
   git clone https://github.com/BhardwajArjit/gesture-volume-control.git
   ```

2. Install the required libraries from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. Import the necessary modules and functions into your main Python script.

4. Initialize the hand tracking and volume control functionalities.

5. Capture the video feed from the camera or use pre-recorded video.

6. Continuously track the hand landmarks and calculate the distance between the index finger and thumb.

7. Determine the desired volume level based on the calculated distance and apply the volume changes using pycaw.

8. Display the volume bar on the screen to provide visual feedback to the user.

## Important Considerations

- Ensure that the camera or video feed has good lighting and clear visibility of the hand for accurate hand tracking.
- Calibrate the distance range between the index finger and thumb for volume control according to your preference and comfort.
- Handle any exceptions or errors that may occur during the execution to provide a smooth user experience.

## Conclusion

Congratulations on creating the Gesture Volume Control project using hand gestures! This innovative project demonstrates the potential of computer vision and audio control libraries to create interactive and intuitive user experiences. Have fun experimenting with different hand gestures and volume control settings!
