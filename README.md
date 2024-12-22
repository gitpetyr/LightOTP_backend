# LightOTP Backend

LightOTP_backend 是一个提供轻量级的双因素认证（2FA）系统，提供基于时间的一次性密码（TOTP）功能的后端API。

## 功能

- 用户注册
- 用户Token验证
- 添加TOTP密钥
- 获取TOTP即时密码
- 获取TOTP列表
- 删除TOTP密钥

## 安装

1. 克隆项目到本地：
    ```bash
    git clone https://github.com/gitpetyr/LightOTP_backend.git
    cd LightOTP_backend
    ```

2. 创建并激活虚拟环境：
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

## 运行

使用以下命令启动服务器：
```bash
uvicorn main:app --reload --host=0.0.0.0 --port=8000
```

## API 文档

详细的API文档请参见 [API Docs](./API%20Docs.md)。

## 安全说明

为了确保用户的TOTP密钥安全，系统采用了以下措施：

1. **Token加密**: 用户密码$usertoken$ 在数据库中散列值加密。
2. **加密存储**: 所有用户的TOTP密钥在存储前都会使用 用户密码$usertoken$ 进行AES加密。这样即使数据库泄露，攻击者和 LightOTP 均无法直接获取到**明文**的TOTP密钥。
3. **Token验证**: 每次访问 TOTP 密钥时，LightOTP 都会验证用户密码$usertoken$，确保只有合法用户才能访问其 TOTP 密钥。

温馨提示：用户不要把 $totpkey$ 的过多信息写在 $totpname$ 中。

## 客户端

暂无，欢迎贡献

## 贡献

欢迎贡献代码！请提交Pull Request或报告问题。

## 许可证

本项目采用MIT许可证。详情请参见 [LICENSE](./LICENSE) 文件。

## 鸣谢

- [sunlightlt](https://fastapi.tiangolo.com/)