# Browser Use FastAPI Server

一个基于FastAPI的浏览器自动化服务器，集成了LangChain和OpenAI能力，支持智能化的浏览器操作任务执行。

## 功能特点

- 基于FastAPI构建的高性能异步API服务
- 集成LangChain和OpenAI实现智能化任务分析和执行
- 支持多线程并发处理浏览器任务
- 提供统一的错误处理和资源管理机制
- 支持自定义浏览器配置和任务执行参数

## 环境要求

- Python 3.12+
- Chrome浏览器

## 安装配置

1. 克隆项目并安装依赖：
```bash
git clone [repository-url]
cd proteus-browser-use-mpc-server
pip install -r requirements.txt
playwright install
```

2. 配置环境变量（创建.env文件）：
```env
BROSWER_PATH=<Chrome浏览器路径>
BROSWER_USE_MODEL=gpt-4o-mini  # 或其他支持的模型
BROSWER_USE_BASE_URL=<OpenAI API基础URL或者其他推理服务>
BROSWER_USE_API_KEY=<OpenAI API密钥或者其他apikey>
BROSWER_SAVE_CONVERSATION_PATH=<对话保存路径>
BROSWER_GENERATE_GIF=false  # 是否生成操作GIF
BROWSER_AGENT_THREADS=4  # 线程池大小
```

## API使用

### 执行浏览器任务

**Endpoint:** POST /

**请求体格式：**
```json
{
    "task": "要执行的任务描述"
}
```

**响应格式：**
```json
{
    "result": "任务执行结果或错误信息"
}
```

## 示例

```python
import requests

response = requests.post(
    "http://localhost:8000",
    json={
        "task": "访问百度并搜索Python"
    }
)
print(response.json())
```

## 开发说明

项目结构：
```
src/
├── server.py              # FastAPI服务器入口
├── browser_agent/
    ├── __init__.py
    ├── base.py           # 基础节点抽象类
    └── browser_agent.py  # 浏览器代理实现
```

## 启动服务

```bash
uvicorn src.server:app --host 0.0.0.0 --port 8000 --reload
```

## 注意事项

1. 确保Chrome浏览器已正确安装并配置
2. 环境变量中的路径使用绝对路径
3. API密钥等敏感信息请妥善保管
4. 建议在生产环境中适当调整线程池大小

## 错误处理

服务会自动处理常见错误并返回统一格式的错误信息：
- 任务执行失败
- 浏览器操作异常
- 参数验证错误

## License

[License信息]
