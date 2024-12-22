# 使用官方的Python基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用运行的端口
EXPOSE 8000

# 启动应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
