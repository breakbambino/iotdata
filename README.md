## 서울시 IoT 도시데이터 시스템 
(서울 미세먼지, 초미세먼지, 온도, 습도, 소음, 진동, 풍향, 풍속 등 공공데이터 제공)
- 서울시에서 발생하는 도시데이터를 실시간으로 수집하고 IoT기반 스마트 인프라를 구축하여 다양한 분석과 활용이 가능한 데이터를 제공합니다. 

  

## 데이터 속성

- 데이터 출처
  * 기관 : 서울시
  * 서비스명 : 서울시 IoT 도시데이터 시스템 

- 센서 데이터 구조 (data_info[/sensor_data_information.csv](https://github.com/seoul-iotdata/iotdata/blob/master/data_info/sensor_data_information.csv))

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


-  센서가 설치된 위도,경도 데이터 (data_info[/sensor_longitude_latitude.csv] (https://github.com/seouliotdata/iotdata/blob/master/data_info/sensor_longitude_latitude.csv))
   * 시리얼
   * 위도
   * 경도 
 

  
  
### 데이터 RAW (용량 제한으로 ZIP으로 압축)(data_raw\)
- 2020-03-15 ~ 2020-03-21 수집 데이터 (2분 간격)

  * ALLDATA_20200315.csv -> 파일용량 약 110메가 
  * ALLDATA_20200316.csv -> 파일용량 약 110메가 
  * ALLDATA_20200317.csv -> 파일용량 약 110메가 
  * ALLDATA_20200318.csv -> 파일용량 약 110메가 
  * ALLDATA_20200319.csv -> 파일용량 약 110메가 
  * ALLDATA_20200320.csv -> 파일용량 약 110메가 
  * ALLDATA_20200321.csv -> 파일용량 약 110메가 




## 샘플 분석 소스 

### 파이선 분석 소스 
1. 파이썬을 설치합니다. <https://www.python.org/downloads/>(설치 시 Add Python 3.8 to PATH 체크 박스 체크)
2. python_sample_code.py 파일과 실행할 .csv 파일을 Github에서 다운받습니다.
3. 명령프롬프트(cmd)창을 실행한 후 csvfile.py 파일을 다운받은 경로로 이동합니다.    
 ex) cd (파일을 다운받은 경로)
4. python csvfile.py 를 입력합니다.
5. 실행할 .csv 파일을 선택합니다.
6. 실행결과는 다음과 같습니다.
---
<img src="/cvsfile_result.png" width="850px" height="450px" title="cvsfile_result" alt="cvsfile_result"></img><br/>
