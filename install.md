# LightOTP_Backend 安装构建指南

## 安装方法

[**docker 项目地址**](https://hub.docker.com/r/zhongxiaoma/lightotp-backend)

先安装Docker

```bash
$ docker pull zhongxiaoma/lightotp-backend:202412221333

$ docker run -d -p 8000:8000 --name LightOTP_backend zhongxiaoma/lightotp-backend:202412221333
```

## 构建方法

```bash
$ git clone https://github.com/gitpetyr/LightOTP_backend.git
$ cd LightOTP_backend
$ docker build -t lightotp_backend . #构建
```
