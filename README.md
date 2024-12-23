# LightOTP Backend

[![GitHub license](https://img.shields.io/github/license/gitpetyr/LightOTP_backend?style=flat-square)](LICENSE)
![GitHub Repo size](https://img.shields.io/github/repo-size/gitpetyr/LightOTP_backend?style=flat-square&color=3cb371)
![GitHub Repo Languages](https://img.shields.io/github/languages/top/gitpetyr/LightOTP_backend?style=flat-square)
![Build](https://img.shields.io/badge/buildwith-docker-brightgreen)

LightOTP_backend 是一个提供轻量级的双因素认证（2FA）系统，提供基于时间的一次性密码（TOTP）功能的后端API。

## 安装 

[参考install.md](./install.md)

## 功能

- 用户注册
- 用户Token验证
- 添加TOTP密钥
- 获取TOTP即时密码
- 获取TOTP列表
- 删除TOTP密钥

## 如何贡献

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

使用以下命令启动服务器：
```bash
uvicorn main:app --reload --host=0.0.0.0 --port=8000
```

## API 文档

详细的API文档请参见 [API Docs](./API%20Docs.md)。

## 安全说明

为了确保用户的TOTP密钥安全，系统采用了以下措施：

1. **Token加密**: 用户密码usertoken 在数据库中散列值加密。
2. **加密存储**: 所有用户的TOTP密钥在存储前都会使用 用户密码usertoken 进行AES加密。这样即使数据库泄露，攻击者和 LightOTP 均无法直接获取到**明文**的TOTP密钥。
3. **Token验证**: 每次访问 TOTP 密钥时，LightOTP 都会验证 用户密码usertoken，确保只有合法用户才能访问其 TOTP 密钥。

温馨提示：用户不要把 totpkey 的过多信息写在 totpname 中。

## 客户端

欢迎贡献

提供一个简易客户端
```python
import requests
import getpass

BASE_URL = "http://localhost:8000"

def register(userid, usertoken):
    response = requests.get(f"{BASE_URL}/register", params={"userid": userid, "usertoken": usertoken})
    return response.json()

def check_token(userid, usertoken):
    response = requests.get(f"{BASE_URL}/test/checktoken", params={"userid": userid, "usertoken": usertoken})
    return response.json()

def add_totp(userid, usertoken, totpname, totpkey):
    response = requests.get(f"{BASE_URL}/addtotp", params={"userid": userid, "usertoken": usertoken, "totpname": totpname, "totpkey": totpkey})
    return response.json()

def get_totp(userid, usertoken, totpname):
    response = requests.get(f"{BASE_URL}/gettotp", params={"userid": userid, "usertoken": usertoken, "totpname": totpname})
    return response.json()

def get_totp_list(userid, usertoken):
    response = requests.get(f"{BASE_URL}/gettotplist", params={"userid": userid, "usertoken": usertoken})
    return response.json()

def delete_totp(userid, usertoken, totpname):
    response = requests.get(f"{BASE_URL}/deltotp", params={"userid": userid, "usertoken": usertoken, "totpname": totpname})
    return response.json()

def main():

    action = input("请选择操作: 1. 注册 3. 添加TOTP 4. 获取TOTP 5. 获取TOTP列表 6. 删除TOTP\n")

    userid = input("请输入用户名: ")
    usertoken = getpass.getpass("请输入密码: ")
    
    if action == "1":
        print(register(userid, usertoken))
    elif action == "2":
        print(check_token(userid, usertoken))
    elif action == "3":
        totpname = input("请输入TOTP名称: ")
        totpkey = input("请输入TOTP密钥: ")
        print(add_totp(userid, usertoken, totpname, totpkey))
    elif action == "4":
        totpname = input("请输入TOTP名称: ")
        print(get_totp(userid, usertoken, totpname))
    elif action == "5":
        print(get_totp_list(userid, usertoken))
    elif action == "6":
        totpname = input("请输入TOTP名称: ")
        print(delete_totp(userid, usertoken, totpname))
    else:
        print("无效操作")

if __name__ == "__main__":
    while True:
        main()
```

## 贡献

欢迎贡献代码！请提交Pull Request或报告问题。

## 许可证

详情请参见 [LICENSE](./LICENSE) 文件。

## 鸣谢

- [sunlightlt](https://github.com/sunlightlt/)
- [1000ttank](https://github.com/1000ttank/) 提供的思路