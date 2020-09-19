# studyNote

### FAST RCNN
- SPP-net(SPP-net. Spatial Pyramid Pooling) RCNN 아이디어로 공간 풀링 통해 구배를 계산한다.

### YOLO(You only Look Once)
- R-CNN 은 5초, Fast R-CNN 0.5프레임, Faster R-CNN 7프레임이 최대인 당시 YOLO 가 등장하여 45프레임을 보여주었고 빠른 버전의 경우 155프레임을 기록 <br>
    - R-CNN - Fast R-CNN - Faster R-CNN - YOLO 는 대략 10배씩 속도차이가 남.
- 객체 검출(object detection)의 방법으로 격자 그리드로 나누어 한 번에 클래스를 판단하고 이를 통합해 최종 객체를 구분합니다.  <br>
-각 이미지를 S x S 개의 그리드로 분할하고, 그리드의 신뢰도를 계산한다. 신뢰도는 그리드 내 객체 인식 시 정확성을 반영한다. <br>
- Darknet 프레임웍 기반으로 동작한다. <br>
    - R-CNN은 region proposal이라는 수백개의 이미지 후보를 생성하고 각각에 대해서 분류를 함.
- 경계 상자를 예측하기 위한 알고리즘
    - 슬라이딩 윈도우 방식 : 이미지의 슬라이딩 윈도우 영역 이미지가 객체 클래스 예측 함수에 전달된다. 이미지의 객체 탐색을 위해, 이미지 좌상단부터 일정 크기의 경계 상자를 만들어, 그 안에 객체를 탐색하는 과정을 반복한다. (Hog Features)
- YOLO 이용해 표지판 데이터를 훈련하고, 실시간 영상을 통해 객체를 추출하기 위해, 다양한 색상, 재질, 모양의 이미지와 라벨 데이터를 준비해야 한다. 그리고, 이 데이터를 darknet 포맷으로 변환하고, 학습해야 한다.
    - 신경망 훈련 데이터 준비 및 훈련
    1) 데이터 수집 및 라벨링
    2) 비디오로 촬영하고, 정지 이미지를 만듬
    3) 각 정지 이미지에 인식되기 원하는 객체 영역을 선택하고, 라벨링을 함(BBox-Label-Tool 사용 - 라벨링 
    함)
    4) Darknet 포맷으로 변환
    5) 신경망 훈련을 위한 포맷으로 VOC 데이터를 사용면, scripts/voc_label.py를 이용해, 기존 VOC 포맷을 다크넷 포맷으로 변환.
    6) 만약 자체 수집된 데이터를 사용한다면, cripts/convert.py 를 이용해 데이터 포맷을 변환.
    7) 코드 수정 및 컴파일
        - YOLO 소스코드에서 src/yolo.c 의 클래스 수(라벨 수)와 클래스 이름을 적절히 수정한다. src/yolo_kernels.cu 도 수정한다. 학습 데이터 클래스 수에 맞게, cfg/yolo.cfg 도 수정한다. 원본 yolo 설정을 고려해, pre-trained weights 을 활용한다.
    8) 훈련시작
        - ./darknet yolo train cfg/yolo.cfg extraction.conv.weights
    <br>--> 추출된 weights 파일을 이용해 실시간 영상에 포함되어 있는 객체를 다음과 같이 추출할 수 있다. 



