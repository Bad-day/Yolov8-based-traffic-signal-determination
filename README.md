# Yolov8-기반 시각 및 색각이상자를 위한 신호 판정 시스템
</br> 
traffic lights detection for people with Visual and color vision abnormalities. </br>
It is linked to capstone design and graduation works, and it is still incomplete and learning is steadily progressing.
</br></br>
<div align="center">

![KakaoTalk_20230521_175226884](https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/6ecd00b4-89f5-48d0-8ac9-214486df7437)

![KakaoTalk_20230521_175226884](https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/blob/main/KakaoTalk_20250706_234532345.gif?raw=true)
</div></br></br>

## Tech Stacks Used


----------------------------------
<div align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Yolov8-00FFFF?style=flat&logo=yolo&logoColor=white" />
<img src="https://img.shields.io/badge/Pytorch-EE4C2C?style=flat&logo=pytorch&logoColor=white" />
</br>
<img src="https://img.shields.io/badge/VSCode-007ACC?style=flat&logo=visualstudiocode&logoColor=white" />
<img src="https://img.shields.io/badge/anaconda-44A833?style=flat&logo=anaconda&logoColor=white" />

 ### + Learning Environments , Intergration

</div>

 <div align="center">
    <a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-colab-small.png" width="15%"/>
    </a>
    <a href="https://hub.docker.com/r/ultralytics/yolov5">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-docker-small.png" width="15%"/>
    </a>
    <a href="https://github.com/ultralytics/yolov5/wiki/GCP-Quickstart">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-gcp-small.png" width="15%"/>
    </a>
  </br>
      <a href="https://roboflow.com/?ref=ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-roboflow-long.png" width="49%"/>
    </a>
  
</div>
</br></br>

## Data set

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
<img src="https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/blob/main/KakaoTalk_20250706_233951822.jpg?raw=true" height="400px" width=480px">



## Why Yolov8?
----------------------
![image](https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/fc818d4c-86e2-497e-bdc4-cfc9262593b9)
</br>
<div align="center">
   <a href="https://github.com/ultralytics/yolov5/actions"><img src="https://github.com/ultralytics/yolov5/workflows/CI%20CPU%20testing/badge.svg" alt="CI CPU testing"></a>
   <a href="https://zenodo.org/badge/latestdoi/264818686"><img src="https://zenodo.org/badge/264818686.svg" alt="YOLOv5 Citation"></a>
   <a href="https://hub.docker.com/r/ultralytics/yolov5"><img src="https://img.shields.io/docker/pulls/ultralytics/yolov5?logo=docker" alt="Docker Pulls"></a>
   <br>
   <a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
   <a href="https://www.kaggle.com/ultralytics/yolov5"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a>
   <a href="https://join.slack.com/t/ultralytics/shared_invite/zt-w29ei8bp-jczz7QYUmDtgo6r6KcMIAg"><img src="https://img.shields.io/badge/Slack-Join_Forum-blue.svg?logo=slack" alt="Join Forum"></a>
</div>

</br>

|Model	size(pixels)|mAPval 50-95	Speed|CPU ONNX(ms)|Speed A100 TensorRT(ms)| 	params (M)	|FLOPs(B)|
|------|---|---|------|---|---|
|YOLOv8n|	640|	37.3|	80.4|	0.99|	3.2|	8.7|
|YOLOv8s|	640|	44.9|	128.4|	1.20|	11.2|	28.6|
|YOLOv8m|	640	|50.2	|234.7|1.83|	25.9|	78.9|
|YOLOv8l|	640|	52.9|	375.2|	2.39|	43.7|	165.2|
|YOLOv8x|	640|	53.9|	479.1|	3.53|	68.2|	257.8|

</br>



<!--
<a align="center" href="https://ultralytics.com/yolov5" target="_blank">
<img width="800" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/banner-api.png"></a>
-->


  
![image](https://github.com/Bad-day/Yolov8-based-traffic-signal-determination/assets/75732202/9de6b5c3-ac94-4e78-bab8-54d946707769)

