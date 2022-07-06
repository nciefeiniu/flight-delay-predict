# flight-delay-predict
flight delay predict with weather data
数据清洗项目
1.首先根据原航班信息数据对应天气信息网站手动做出机场-城市编码参考字典，其中只选择了部分机场

2.对应填充机场的经纬度

3.首先进行第一次清洗：删除出发、到达机场不在给出的参考机场字典中的项

4.进行第二次清洗：删除同一时间航线（即为出发地点和到达地点都一样的航班）重复的项

5.其中对最原始的数据集的处理还有：

  通过原始的时间戳计算计划出发、达到与实际出发、达到的时间
  
  通过不同机场之间的经纬度计算出各个机场之间的距离并整合填充至各个航班相应的信息栏中
  
6.通过构建的机场-城市参考字典进行天气信息的爬取、填充

  首先构建不同城市的各个的以天为单位的天气信息文件.CSV
  
  进行相应的网络爬虫读取数据并写道城市天气文件中
  
  通过城市->定位所要访问的文件；预计出发日期->定位到具体要填充的项
  
7.之后保存写入，得到初始清洗好的数据集了
