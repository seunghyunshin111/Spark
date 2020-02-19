# Spark

- 미들웨어: RDBMS, Spark
- Spark: 빅데이터 (일반 대용량 데이터보다 훨씬 많은 양)
- RDBMS: 일반 대용량 데이터를 보관하는 데이터베이스 (분산 병렬 처리)
- Hadoop: Spark에 Hadoop을 설치하면 좋음 (호환이 잘 됨)
- 정형화된 기존 RDBMS에서는 '빅데이터'를 처리하지 못함. 스파크는 정형화 비정형화된 데이터를 다 활용할 수 있음.
- Hadoop
  - Map + Reduce(맵리듀스) 처리와 HDFS 저장
  - 서버가 낮은 것들을 모아서 처리할 수 있음
- Spark
  - 처리 기술이 좋으나 저장이 없어서, 하둡의 저장기능을 가져와서 처리를 스파크로 쓰면 처리 속도가 100배가 빠르다.
  - 맵리듀스(처리)를 보완한 것이 스파크

---

- Spark를 회사 내에서 쓰인다 하면 '스칼라' 공부는 필수 병행해야 함.
- 간단한 것은 스파크의 ML 라이브러리를 사용하면 좋음.
- 현재 아마존 서버에 쓸 수 있게 설치를 해놓은 상태
- 아파치 하둡 : 자바꺼
- 아파치 스파크
- 스파크 스트리밍: 서버에서 바로 영상이나 미디어 정보를 구축하게 하는 것 (다운로드 받지 않고!), 저렴한 가격에 미디어 서비스를 구축할 수 있다.

---

- 아마존 서버 로그인
- 푸티 접속 계정 (주소 적고, 포트 번호, 푸티 비밀번호 입력 후 실행)
- 내 lab11 아이디로 접속

<br>

## Linux

- $ (명령어 입력 신호)

- pwd 확인

- clear: 화면 다 지워짐

- man ls: 추가 상세 설명 보고 싶을 때

- ls -al: 있는 것들 보임

- mkdir test

- ls

- ./test

- test (위와 동일)

- ls

- cd /opt/spark

- sudo

  : 일시적으로 루트계정을 알 수 있음! (여기서 mkdir 하고 다시 원래 계정으로 돌아와야 함! 루트 계정 아니면 디렉토리를 생성할 수 없음)

- 웹서버는 다 리눅스! (윈도우는 잘 안 씀.)

- 웹 서버: 적은 사양을 엮어서 늘리는 것을 써야 하는데, 윈도우는 웹 서버당 라이센스 비용을 지불해야 하기 때문에 잘 안씀.

- 대부분 리눅스를 베이스로 한 것을 많이 사용. 하둡도 리눅스를 사용하면 굉장히 속도가 빨라짐

- spark는 bin에서 모든 실행 유틸이 있음.

- cd bin

- ls

- cd .. (bin에 실행 권한이 없어서 상위 계정에서)

- ./bin/spark-shell   ( 이렇게 실행 !)

---

## Scala



- scala> 창이 뜬다.

- var a:Int =1

  :변수 a를 int로 설정하고 1로 초기화

- var: 가변변수

- val: 상수 (한번 정하면 못 바꾼다!)

- variable / value

- def display(x:string)={println(x)}

- display("hello world")

- 객체 지향을 잘 지원하고, 함수 지향도 잘 지원 하는데, class도 제대로 지원하는 편

- def display(x:string)={println(x)}

  - 데이터 타입은 항상 뒤 쪽에
  - 리턴 타입은 스트링 뒤의 함수 끝 자락에 쓰면 됨. 지금은 없는 상태

- 들여쓰기 필요 없음

- 확장자는 스칼라로 저장하고, 스칼라 명령으로 실행하면 됨.

- scla에서 class 생성

  ```scala
  class Test{
      var a=1
      def set(n:Int)={
          a=n
      }
      def print()={println(a)}
  }
  ```

  <br>

  ```scala
  val tobj = new Test()
  tobj.print()
  # a에 해당하는 값 잘 나옴
  # 1
  ```

  ```scala
  Array로 만든 것 값 변경도 가능하지만,
  List는 변경 불가 (파이썬의 튜플과 비슷)
  ```

  <br>

  ---

  ## Python
  
  ### Spark의 MLLib를 Python 기반의 Jupyter notebook을 이용해서 빅데이터 서비스(저장/관리/전처리)를 한다.
  
  ### MLLib를 Python으로 불러오기 위해서 Pyspark를 사용해야 한다.
  
  - 스칼라 나가기: ctrl + c 
  - 모든 명령 프롬프트는 일단 exit을 눌러보기
  
  <br>
  
  - 스파크 환경에서 /opt/spark
  - spark-shell: scala 기반을 불러오기
  - pyspark: 스파크 기반을 불러오는 것
  
  ---
  
  ```
  conda activate test
  conda create -n test3 python=3.6 jupyter tensorflow
  ```
  
  ```python
  import findspark
  findspark.init("/opt/spark")
  
  # 프롬프트 pip install pyspark=2.3.2
  import pyspark
  from pyspark.sql import SparkSession
  
  pyspark.__version__
  
  ## Spark 2.x
  spark = SparkSession.builder.getOrCreate()
  ```
  
  
  
  
  
  
  
  