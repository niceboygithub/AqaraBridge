# Aqara Bridge for Home Assistant

基于Aqara开放平台，通过云端api进行设备控制以及订阅

[![version](https://img.shields.io/github/manifest-json/v/meishild/AqaraBridge?filename=custom_components%2Faqara_bridge%2Fmanifest.json)](https://github.com/meishild/AqaraBridge/releases/latest) [![stars](https://img.shields.io/github/stars/meishild/AqaraBridge)](https://github.com/meishild/AqaraBridge/stargazers) [![issues](https://img.shields.io/github/issues/meishild/AqaraBridge)](https://github.com/meishild/AqaraBridge/issues) [![hacs](https://img.shields.io/badge/HACS-Default-orange.svg)](https://hacs.xyz)


## 需要开发者账号支持

申请AqaraIOT开发者：[Aqara IoT Cloud](https://developer.aqara.com/register).

* 提示：如果在安装过程中出现此集成不支持通过UI配置，大概率是因为rocketmq的链接库不存在，当前版本仅自动集成了x86和arm64。
* 当前支持通过hacs商店进行配置，自定义存储库URL: meishild/AqaraBridge

重点提示：
* 需要自己申请aqara的开发者账号，使用插件自带的信息会导致状态丢失。
* 申请流程1：[注册账号](https://developer.aqara.com/register)，申请通过以后需要选择个人认证，输入姓名和身份证号进行开发者认证。
* 申请流程2：申请通过以后就会有一个DEMO应用，进入项目管理-->详情-->消息推送-->编辑-->选择中国服务、MQ消息推送、消息密钥默认应该只有一个、全订阅-->保存
* 申请流程3：返回概况，Appid&密钥这个点击展开，找到中国服务，记录appId、appkey（需要点击小眼睛）、keyid，然后将这三个参数填写到插件对应的三个值上。
* 消息查看：如果需要确认消息可以将这个插件的日志级别改成info可以查看对应消息情况。

## 版本修订
当前版本V2.0.3修复大部分错误为当前最稳定版本，后续小问题修复延迟合并，主要通过dev2.0分支进行修改。

V2.0.3
* 修复开发者配置问题，可以使用自己开发者信息。


V2.0.2
* 修复错误保存问题，增加启动依赖，需要在homekit启动正常以后。
* 修复flow的option操作错误，可以重新通过手机号刷新失效token，并修复部分错误提示。
* hass图标已经通过，当前可以正常显示组件图标，以及设备厂商图标。
* 修复其他常规错误。

V2.0.1
* 整体合并到master，原有的配置方式需要使用dev分支，该分支不继续维护。
* 修改flow，将多个网关合并到账号，拆分开发者认证信息允许自行配置自己的开发者AK等。
* 修复大部分组件获取状态异常，以及历史状态修改。
* 感谢[银狼](https://bbs.hassbian.com/?62352)新增部分组件配置：支持无线旋钮H1，H1 12头磁吸格栅灯，无线按钮（升级版）。同时墙壁开关拆分为两部分，其中零火的加入了电量监测，led驱动模块加了电力监测。

V1.0.1
* 修复了大部分组件的问题，增加了无线按键。当前的按键都同时事件订阅刷新时间整体速度还不错，不是轮训机制了。
* 增加房间位置获取。
* 增加按键类开关对应按键名称获取。
* 增加arm64的rocketmq动态链接库，除了X86和arm64其他暂时没处理。
* 增加各类的历史数据获取刷新了最后的trigger_time或者last_update_time。
* 增加button类型，将无线开关从传感器上拆分。
* 配置了大部分常见的网关、无线开关、单火/零火开关、温湿度传感器、智能插座、人体传感器等。
* 增加了部分错误提示，至少不会在配置没任何错误了。

V1.0.0

还有我只支持了大部分我有的设备和类似的组件，如果发现有不支持的懂python的修改：
[custom_components/aqara_bridge/core/aiot_mapping.py](https://github.com/meishild/AqaraBridge/blob/master/custom_components/aqara_bridge/core/aiot_mapping.py)

