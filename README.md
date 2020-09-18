# studyNote

### YOLO
- R-CNN 은 5초, Fast R-CNN 0.5프레임, Faster R-CNN 7프레임이 최대인 당시 YOLO 가 등장하여 45프레임을 보여주었고 빠른 버전의 경우 155프레임을 기록 <br>
    --> R-CNN - Fast R-CNN - Faster R-CNN - YOLO 는 대략 10배씩 속도차이가 남.
- 객체 검출(object detection)의 방법으로 격자 그리드로 나누어 한 번에 클래스를 판단하고 이를 통합해 최종 객체를 구분합니다.  <br>
    --> R-CNN은 region proposal이라는 수백개의 이미지 후보를 생성하고 각각에 대해서 분류를 함.
