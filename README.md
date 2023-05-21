# Yolov8-based-traffic-signal-determination
</br> 
traffic lights detection for people with Visual and color vision abnormalities. </br>
It is linked to capstone design and graduation works, and it is still incomplete and learning is steadily progressing.
</br></br>
<div align="center">

![KakaoTalk_20230521_175226884](https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/6ecd00b4-89f5-48d0-8ac9-214486df7437)

</div></br></br>

<div align="center">

## Tech Stacks Used
  
</div>

----------------------------------
<div align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Yolov8-00FFFF?style=flat&logo=yolo&logoColor=white" />
<img src="https://img.shields.io/badge/Pytorch-EE4C2C?style=flat&logo=pytorch&logoColor=white" />
</br>
<img src="https://img.shields.io/badge/VSCode-007ACC?style=flat&logo=visualstudiocode&logoColor=white" />
<img src="https://img.shields.io/badge/anaconda-44A833?style=flat&logo=anaconda&logoColor=white" />

 ### + Learning Environments , Intergration
|<img src="https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/dbf9f867-f43b-4585-8181-8ccbbc27396d" height="50%" width="50%">|<img src="https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/6bac6a2e-41b9-455d-8a14-19021b929033" height="80%" width="80%">|<img src="https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/b8f758d9-e83f-4470-910e-f10e61d575a6" height="50%" width="50%">|<img src="https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/f0aefb56-4d28-4280-9352-dbcdc6ba0b9c" height="50%" width="50%">|
|------|---|---|------|

</div>

</br></br>

## data set

--------------

To aim for a high mAP, more than 3,000 photos will be collected and about 800 photos are currently collected.

![image](https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/0957c65c-eb7a-4c82-aa03-e5dcbd3ebafa)

</br>


## How Data is collected
---------------------
* personally
* Crawling
* use Ai hub

</br>


## System Flow and Structural diagram
------------------------------------------
<img src="https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/26ae81a4-4a27-4958-9224-a9908058b752" height="400px" width="480px">
<img src="https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/b4113b36-fb40-4b8c-b14e-d318c09349a3" height="400px" width="480px">



## Why Yolov8?
----------------------
![image](https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/fc818d4c-86e2-497e-bdc4-cfc9262593b9)

</br>

|Model	size(pixels)|mAPval 50-95	Speed|CPU ONNX(ms)|Speed A100 TensorRT(ms)| 	params (M)	|FLOPs(B)|
|------|---|---|------|---|---|
|YOLOv8n|	640|	37.3|	80.4|	0.99|	3.2|	8.7|
|YOLOv8s|	640|	44.9|	128.4|	1.20|	11.2|	28.6|
|YOLOv8m|	640	|50.2	|234.7|1.83|	25.9|	78.9|
|YOLOv8l|	640|	52.9|	375.2|	2.39|	43.7|	165.2|
|YOLOv8x|	640|	53.9|	479.1|	3.53|	68.2|	257.8|

</br>

![image](https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/9de6b5c3-ac94-4e78-bab8-54d946707769)

