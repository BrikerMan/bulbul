# encoding: utf-8

# author: BrikerMan
# contact: eliyar917@gmail.com
# blog: https://eliyar.biz

# file: builtins.py
# time: 11:31 上午

from typing import List, Dict, Any
from pydantic import BaseModel, Field


class Query(BaseModel):
    original: str  # Original Query Text
    text: str  # Processes Query Text
    # Tokenized Texts
    tokenized_texts: Dict[str, List[str]]  # {"Tokenizer Name": ["token1", "token2"]}


class Intention(BaseModel):
    val: str
    confidence: float = Field(ge=0, le=1)
    module: str  # Module name of the intent tagger
    extra: Dict  # Additional_info


class SlotItem(BaseModel):
    val: str
    entity: str
    confidence: float = Field(ge=0, le=1)


class Slot(BaseModel):
    vals: List[SlotItem] = Field(default_factory=list)
    confidence: float = Field(ge=0, le=1)
    module: str  # Module name of the slot tagger
    extra: Dict  # Additional_info


class NLUResult(BaseModel):
    query: Query
    intent: Intention
    slots: Slot


class SkillResponse(BaseModel):
    data: Any
    confidence: float = Field(ge=0, le=1)
    module: str  # Module name of the skill result
    tts: str  # unified tts text


if __name__ == "__main__":
    pass
