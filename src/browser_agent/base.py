from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseNode(ABC):
    """基础节点类，定义节点接口"""

    @abstractmethod
    async def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """执行节点逻辑

        Args:
            params: 节点参数

        Returns:
            执行结果
        """
        pass

    @abstractmethod
    async def agent_execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """执行节点并将结果转换为统一格式

        Args:
            params: 节点参数

        Returns:
            统一格式的执行结果
        """
        pass

    @abstractmethod
    async def close(self):
        """清理资源"""
        pass
