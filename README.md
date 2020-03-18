## IoT 도시데이터 관리시스템
IoT 도시데이터 관리시스템 분석용 샘플 데이터 제공




## 샘플 데이터

### 데이터 속성

- 데이터 출처
  * 기관 : 서울시
  * 서비스명 : S-DoT(서울시 도시데이터 센서)_측정자료

- 데이터 속성
  * 전체 길이 : 108
  * 헤더 길이 : 18
  * 상세 정보 : data_detail.xlsx 

- 데이터 설명 1 : data_info/sensor_data_information.csv
  * 모델명
  * 시리얼
  * 미세먼지2.5(초미세먼지) (㎍/㎥)
  * 미세먼지10(미세먼지) (㎍/㎥)
  * 기온 (℃)
  * 상대습도 (%)
  * 풍향 (m/s)
  * 풍속 (m/s)
  * 돌풍 풍향 (m/s)
  * 돌풍 풍속 (m/s)
  * 조도 (lux)
  * 자외선 (UV)
  * 소음 (dB)
  * 진동(x) (mm/s)
  * 진동(y) (mm/s)
  * 진동(z) (mm/s)
  * 진동(x) 최대 (mm/s)
  * 진동(y) 최대 (mm/s)
  * 진동(z) 최대 (mm/s)
  * 흑구 온도 (℃)
  * pm25 보정 (㎍/㎥)
  * pm10 보정 (㎍/㎥)
  * 측정시간 (yyyymmddhi)
  * 등록 일시 (yyyy-mm-dd hh:mm:ss)


- 데이터 설명 2 : data_info/sensor_longitude_latitude.csv
  * 시리얼
  * 위도
  * 경도 
 

  
  
### 샘플 데이터

- 2020.02.16 측정 데이터
  * PUBDATA_20200216.csv




## 샘플 분석 소스 

### 분석 소스 설명
- .csv 파일을 json 형태로 읽어드립니다.

### 분석 소스 실행 방법
1. 파이썬을 설치합니다. <https://www.python.org/downloads/>(설치 시 Add Python 3.8 to PATH 체크 박스 체크)
2. csvfile.py 파일과 실행할 .csv 파일을 Github에서 다운받습니다.
3. 명령프롬프트(cmd)창을 실행한 후 csvfile.py 파일을 다운받은 경로로 이동합니다.    
 ex) cd (파일을 다운받은 경로)
4. python csvfile.py 를 입력합니다.
5. 실행할 .csv 파일을 선택합니다.
6. 실행결과는 다음과 같습니다.
---
<img src="/cvsfile_result.png" width="850px" height="450px" title="cvsfile_result" alt="cvsfile_result"></img><br/>
