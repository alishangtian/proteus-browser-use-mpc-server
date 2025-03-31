from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import uvicorn
import logging
from .browser_agent import BrowserAgentNode

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建FastAPI应用
app = FastAPI(title="Browser Agent API")

# 创建BrowserAgentNode实例
browser_agent = BrowserAgentNode()

# 请求模型
class BrowserTaskRequest(BaseModel):
    task: str
    params: Dict[str, Any] = {}

@app.post("/browser_use")
async def execute_task(request: BrowserTaskRequest):
    """
    执行浏览器自动化任务
    
    Args:
        request: 包含task和可选params的请求体
        
    Returns:
        执行结果
    """
    try:
        # 合并task到params
        params = request.params.copy()
        params["task"] = request.task
        
        # 执行任务
        result = await browser_agent.agent_execute(params)
        return result
    except Exception as e:
        logger.error(f"执行任务失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("shutdown")
async def shutdown_event():
    """
    应用关闭时清理资源
    """
    await browser_agent.close()

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )