# Spark_2_with_AWS

- AWS 서비스 안에 리눅스를 기반으로 각자의 아나콘다(파이썬)의 계정을 만든 상태
- 아나콘다와 Spark의 ML 라이브러리를 사용
- 스파크의 ML 라이브러리를 이용하면 굉장히 빠른 속도
- 스파크에서 성능을 끌어올리고 싶으면 Scala를 써라
- 오늘은 파이썬을 쓸 것

<br>

<br>

## Map-Reduce

- Big data를 Map이라는 단위들로 쪼갠다.
- Map들 각각 수행한다. 이들을 취합하여 Reduce(처리, 확산, 취합)한다. => Output
- Inmemory
- 스파크의 기본적인 특성
  - **스파크는 분산 인메모리 프로세싱 엔진**
  - 스파크는 반드시 하둡과 같이 사용될 필요는 없다.
  - 하지만 스파크는 하둡을 지원. 예를 들면 스파크는 하둡이 사용하는 파일 시스템인 HDFS (Hadoop Distributed File System) 의 데이터를 읽어올 수도 있고, 반대로 데이터를 쓸 수도 있다. 
  - 스파크는 HDFS 에 저장된 데이터를 **하둡 코어 라이브러리를 호출**함으로써 메모리로 불러온 후, **변환 및 계산 등을 거쳐 최종 원하는 결과물을 산출**
  - 스파크는 인메모리 프로세싱을 하기 때문에 Disk I/O 가 많이 일어나는 하둡의 맵-리듀스보다 특정 작업 (ex. multi-pass map reduce)에서는 더 빠르게 수행될 수 있다. 

<br>

- RDD

<br>

<br>

## Mllib

- 데이터 전처리, 모형, 평가

- ML라이브러리를 가져다 쓰려면 그 형태는 꼭 features라고 하는 이름의 벡터 정보! 그리고 label이라는 이름의 double을 함께 보낸다.

- Spark에서 제공하는 MLlib에서 제공하는 클래스로 쓰려면 

  ```python
  features | label 형식으로 구성
  (vector  | double)
  ```

- FPR: 오류율

- TPR: 정답률

- precision: 정밀도

- recall = sensitive

- 민감도는 높고, 특이도가 낮은 것이 좋은 것! 

- y축은 민감도, x축은 특이도 따라서 ROC 곡선은 y축 쪽으로 굽은 그래프가 좋은 것!

<br>

<br>