# 介绍
* 自用Subconverter订阅转换配置文件，修改自原作者[ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)  
* 自用Loon全分组多模式配置文件
* ACL4SSR规则为基础合并碎片补充剔除重复
* Adblack广告拦截规则主要来源于项目[anti-AD](https://github.com/privacy-protection-tools/anti-AD) ，使用Actions自动构建
* 规则数量: 8373条
* 最近更新: 2023年11月26日15:27:27
## Clash订阅转换远程配置:
```
https://raw.githubusercontent.com/mphin/ACL4SSR/main/config/ACL4SSR_Online_Full_MultiMode_777.ini
```
## Loon分流配置文件:
* [点击一键导入Loon](https://www.nsloon.com/openloon/import?sub=https://raw.githubusercontent.com/mphin/ACL4SSR/main/config/Loon_config_mphin.conf)
* 通过复制链接从URL下载:
```
https://raw.githubusercontent.com/mphin/ACL4SSR/main/config/Loon_config_mphin.conf
```
## 策略组内容及顺序
> 规则集非碎片化，建议添加所有规则集确保完整性，注意规则集的先后顺序
- **🎯 全球直连**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/LocalAreaNetwork.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/LocalAreaNetwork.list)
- **📢 谷歌服务**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/Google.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/Google.list)
- **🤖 AI｜奈飞**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/OpenaiNetflix.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/OpenaiNetflix.list)
- **🎥 国外媒体**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/ProxyMedia.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/ProxyMedia.list)
- **Ⓜ️ 微软服务**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/Microsoft.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/Microsoft.list)
- **🍎 苹果服务**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/Apple.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/Apple.list)
- **📺 国内媒体**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/ChinaMedia.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/ChinaMedia.list)
- **🎮 游戏平台**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/GamesPlatform.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/GamesPlatform.list)
- **📡 IP｜测速**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/IpinfoSpeedtest.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/IpinfoSpeedtest.list)
- **📲 电报消息**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/Telegram.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/Telegram.list)
- **✈️ 国外常规**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/ProxyGFWlist.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/ProxyGFWlist.list)
- **🎯 全球直连**：
  - [https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/GlobalDirect.list](https://raw.githubusercontent.com/mphin/ACL4SSR/main/rules/GlobalDirect.list)
- **🎯 全球直连[]GEOIP,CN**
- **🐟 漏网之鱼[]FINAL**
## 进阶玩法:
* Loon及Stash策略组图标集:
     > QX及其他未测试应该也支持
```
    https://raw.githubusercontent.com/mphin/GroupIcons/main/GroupIcons_emoji.json
```
## 致谢
- [@ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)
- [@Loon0x00/LoonExampleConfig](https://github.com/Loon0x00/LoonExampleConfig)
- [@privacy-protection-tools/anti-AD](https://github.com/privacy-protection-tools/anti-AD)
## 项目 Star 数增长趋势
[![Stargazers over time](https://starchart.cc/mphin/ACL4SSR.svg)](https://starchart.cc/mphin/ACL4SSR)

**本仓库创建于2023年7月2日**
