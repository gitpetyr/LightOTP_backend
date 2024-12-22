# LightOTP API 文档

## 1. 注册用户

**URL:** `/register`

**方法:** `GET`

**参数:**
- `userid` (str): 用户ID
- `usertoken` (str): 用户Token

**响应:**
- 成功: `{"res": "Ok", "requests": {"userid": "your_userid", "usertoken": "your_usertoken"}}`
- 失败: `{"Fail": "错误信息", "debug": "调试信息"}`

**示例:**
```bash
curl -X GET "http://localhost:8000/register?userid=testuser&usertoken=testtoken"
```

## 2. 检查用户Token

**URL:** `/test/checktoken`

**方法:** `GET`

**参数:**
- `userid` (str): 用户ID
- `usertoken` (str): 用户Token

**响应:**
- 成功: `{"res": {"Ok": True}, "requests": {"userid": "your_userid", "usertoken": "your_usertoken"}}`
- 失败: `{"res": {"Ok": False}, "requests": {"userid": "your_userid", "usertoken": "your_usertoken"}}`

**示例:**
```bash
curl -X GET "http://localhost:8000/test/checktoken?userid=testuser&usertoken=testtoken"
```

## 3. 添加TOTP

**URL:** `/addtotp`

**方法:** `GET`

**参数:**
- `userid` (str): 用户ID
- `usertoken` (str): 用户Token
- `totpname` (str): TOTP名称
- `totpkey` (str): TOTP密钥

**响应:**
- 成功: `{"res": "Ok", "requests": {"userid": "your_userid", "usertoken": "your_usertoken", "totpname": "your_totpname", "totpkey": "your_totpkey"}}`
- 失败: `{"Fail": "错误信息", "debug": "调试信息"}`

**示例:**
```bash
curl -X GET "http://localhost:8000/addtotp?userid=testuser&usertoken=testtoken&totpname=testtotp&totpkey=testkey"
```

## 4. 获取TOTP即时密码

**URL:** `/gettotp`

**方法:** `GET`

**参数:**
- `userid` (str): 用户ID
- `usertoken` (str): 用户Token
- `totpname` (str): TOTP名称

**响应:**
- 成功: `{"res": {"totpkey": "your_now_totpkey"}, "requests": {"userid": "your_userid", "usertoken": "your_usertoken", "totpname": "your_totpname"}}`
- 失败: `{"Fail": "错误信息", "debug": "调试信息"}`

**示例:**
```bash
curl -X GET "http://localhost:8000/gettotp?userid=testuser&usertoken=testtoken&totpname=testtotp"
```

## 5. 获取TOTP列表

**URL:** `/gettotplist`

**方法:** `GET`

**参数:**
- `userid` (str): 用户ID
- `usertoken` (str): 用户Token

**响应:**
- 成功: `{"res": {"totpnames": ["totpname1", "totpname2"]}, "requests": {"userid": "your_userid", "usertoken": "your_usertoken"}}`
- 失败: `{"Fail": "错误信息", "debug": "调试信息"}`

**示例:**
```bash
curl -X GET "http://localhost:8000/gettotplist?userid=testuser&usertoken=testtoken"
```

## 6. 删除TOTP

**URL:** `/deltotp`

**方法:** `GET`

**参数:**
- `userid` (str): 用户ID
- `usertoken` (str): 用户Token
- `totpname` (str): TOTP名称

**响应:**
- 成功: `{"res": "Ok", "requests": {"userid": "your_userid", "usertoken": "your_usertoken", "totpname": "your_totpname"}}`
- 失败: `{"Fail": "错误信息", "debug": "调试信息"}`

**示例:**
```bash
curl -X GET "http://localhost:8000/deltotp?userid=testuser&usertoken=testtoken&totpname=testtotp"
```

## 安全说明

为了确保用户的TOTP密钥安全，系统采用了以下措施：

1. **Token加密**: 用户密码usertoken 在数据库中散列值加密。
2. **加密存储**: 所有用户的TOTP密钥在存储前都会使用 用户密码usertoken 进行AES加密。这样即使数据库泄露，攻击者和 LightOTP 均无法直接获取到**明文**的TOTP密钥。
3. **Token验证**: 每次访问 TOTP 密钥时，LightOTP 都会验证 用户密码usertoken，确保只有合法用户才能访问其 TOTP 密钥。