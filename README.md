# ACL4SSR
自用subconverter订阅转换配置文件含自用补充规则，修改自ACL4SSR https://github.com/ACL4SSR/ACL4SSR    
适合多节点用户  

做了以下修改：  
增加油管奈非分组  
增加国外常规分组   
增加五个地区分组  
增加自用补充777规则  
去除广告拦截  
去除应用净化  
去除OpenAi  
去除巴哈姆特  
去除节点选择，合并到国外常规  
去除网易音乐，合并到国内媒体  
去除哔哩哔哩，合并到国内媒体  
去除奈非视频，合并到油管奈非  
将负载均衡和故障转移原所有节点修改为使用地区节点分组的自动测速，尽可能使用到URLTest后的节点  
![360截图20230702141538446](https://github.com/mphin/ACL4SSR/assets/59219235/43e3fa4c-0a7a-4e28-a8dc-3f21de3eed13)
![360截图20230702141524630](https://github.com/mphin/ACL4SSR/assets/59219235/5a581a95-a01b-4b19-a434-47e67a504e0e)

使用方法:
1.使用在线订阅转换，在订阅转换网站上填写远程配置参数：  
https://raw.githubusercontent.com/mphin/ACL4SSR/main/config/ACL4SSR_Online_Full_MultiMode_777.ini  
2.使用本地搭建的订阅转换，将本项目的配置文件和补充规则copy下来  
补充规则文件放入ACL4SSR规则集下即可既*/subconverter/rules/ACL4SSR/Clash/
