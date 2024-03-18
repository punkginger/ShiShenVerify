# 识身

一个基于flask与sqlalchemy的身份识别系统的web管理系统的后端接口
基于restful api理念开发，前后端分离
硬件端基于nano/fpga等设备开发，用于实现人物身份识别，包括:
    1. 人脸识别 
    2. 指纹识别
    3. 声纹识别
    4. 步态识别
持续开发中

## 安装

1. 克隆该仓库
2. 使用 `pip install -r requirements.txt`安装所需依赖.
3. 运行 `python run.py`以启动.
4. 运行 `./local_server/server.py` 以在本地启动一个http服务器，用于测试环境下的文件上传

## 使用

访问 `http://localhost:8000`.
访问 `http://localhost:8001` 以访问测试用的本地http服务器

## 须知

在config.py中修改部分可修改参数

## api文档

使用apifox管理api，公开文档于此
https://apifox.com/apidoc/shared-48e735ca-7888-4d61-854e-039a4cd559c2/api-156011616