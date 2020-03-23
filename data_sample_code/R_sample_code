library(data.table)
library(tidyverse)
library(dplyr)
library(ggplot2)
library(ggthemes)
library(directlabels)
 
 
#모든 파일 읽기
alldata <- list.files(pattern = "*.csv") %>%  map_df(~fread(.))
 
#데이터 구조 확인
str(alldata)
 
#데이터 요약 
summary(alldata)
 
#날짜/시간 분리 
alldata$yyyymmdd <- as.Date(alldata$`등록 일시`)
str(alldata$yyyymmdd)
 
#데이터 수집 일자 체크 확인 
unique(alldata$yyyymmdd)
 
#데이터 수집 센서 갯수 확인
length(unique(alldata$시리얼))
 
#서울시 센서 수집 갯수(일별)
alldata %>% group_by(yyyymmdd) %>% summarize(수집센서갯수 = n_distinct(시리얼))
 
#서울시 센서별 측정 기록(일별)
dust_average <- alldata %>% 
  group_by(yyyymmdd) %>% summarize(일평균미세먼지 = mean(`미세먼지10(미세먼지) (㎍/㎥)`), 일평균초미세먼지 = mean(`미세먼지2.5(초미세먼지) (㎍/㎥)`))
 
#서울시 미세먼지 농도(일평균)
ggplot(dust_average, aes(x = yyyymmdd, y =일평균미세먼지, fill = 일평균미세먼지)) + 
  theme_economist() +
  geom_bar(stat="identity") +
  geom_text(aes(label = sprintf("%0.2f", 일평균미세먼지)), vjust=-0.5, size=3) +
  scale_fill_gradient(low = "skyblue1", high ="royalblue4") +
  theme(legend.position="null") +
  ggtitle("서울시 미세먼지 농도(일평균)") + xlab("날짜") + ylab("미세먼지 농도")
  
#서울시 초미세먼지 농도(일평균)
ggplot(dust_average, aes(x = yyyymmdd, y =일평균초미세먼지, fill = 일평균초미세먼지)) + 
  theme_economist() +
  geom_bar(stat="identity") +
  geom_text(aes(label = sprintf("%0.2f", 일평균초미세먼지)), vjust=-0.5, size=3) +
  scale_fill_gradient(low = "skyblue1", high ="royalblue4") +
  theme(legend.position="null") +
  ggtitle("서울시 미세먼지 농도(일평균)") + xlab("날짜") + ylab("초미세먼지 농도")
 
 
  
  
