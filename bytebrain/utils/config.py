import os
from dataclasses import dataclass
from typing import Optional
import torch


@dataclass
class Config:
    """项目配置类"""
    
    # 模型配置
    model_name: str = "IEITYuan/Yuan2-2B-July-hf"
    model_path: Optional[str] = None
    embed_model_name: str = "AI-ModelScope/bge-small-zh-v1.5"
    embed_model_path: Optional[str] = None
    
    # 数据配置
    knowledge_path: str = "./knowledge.txt"
    finetune_data_path: str = "./finetune_data.json"
    
    # 训练配置
    output_dir: str = "./finetuned_model"
    num_train_epochs: int = 3
    per_device_train_batch_size: int = 2
    learning_rate: float = 2e-5
    
    # 推理配置
    max_seq_length: int = 2048
    max_new_tokens: int = 512
    torch_dtype: torch.dtype = torch.bfloat16
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    
    # RAG配置
    top_k: int = 3
    similarity_threshold: float = 0.5
    
    def __post_init__(self) -> None:
        """后初始化"""
        if self.model_path is None:
            self.model_path = f"./{self.model_name.replace('/', '/')}"
        if self.embed_model_path is None:
            self.embed_model_path = f"./{self.embed_model_name.replace('/', '/')}"
        
        if self.device == "cpu":
            self.torch_dtype = torch.float32
