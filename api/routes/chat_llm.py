from enum import Enum
from typing import Annotated

from fastapi import APIRouter, Depends
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from pydantic import BaseModel, Field

from core.chat_llm import ChatLLM

from ..dependencies import get_chat_model

router = APIRouter(dependencies=[Depends(get_chat_model)])


class ChatMessageRole(str, Enum):
    """
    Role of the message

    Attributes:
        Human (str): Human role
        Ai (str): AI role
        System (str): System role
    """

    Human = "human"
    Ai = "ai"
    System = "system"


class ChatMessage(BaseModel):
    """
    Chat message

    Attributes:
        role (ChatMessageRole): Role of the message
        content (str): Content of the message
    """

    role: ChatMessageRole = Field(
        ...,
        title="Role of the message",
        description="Role of the message",
    )
    content: str = Field(
        ...,
        title="Content of the message",
        description="Content of the message",
        examples=["Hello, how can I help you today?"],
    )


class ChatInput(BaseModel):
    """
    Chat input

    Attributes:
        messages (list[ChatMessage]): Messages
    """

    messages: list[ChatMessage] = Field(
        ...,
        title="Messages",
        description="Messages",
    )


class ChatOutput(BaseModel):
    """
    Chat output

    Attributes:
        content (str): Content of the message
    """

    content: str = Field(
        ...,
        title="Content of the message",
        description="Content of the message",
        examples=["Hello, how can I help you today?"],
    )


def transform_message(message: Annotated[ChatMessage, "Chat Message"]):
    """
    Transform a chat message to a message object

    Args:
        message (ChatMessage): Chat message

    Returns:
        BaseMessage: Message object
    """
    if message.role == ChatMessageRole.Human:
        return HumanMessage(content=message.content)
    if message.role == ChatMessageRole.Ai:
        return AIMessage(content=message.content)
    if message.role == ChatMessageRole.System:
        return SystemMessage(content=message.content)
    raise ValueError(f"Invalid message role: {message.role}")


@router.post(
    "",
    description="Chat with the chat model",
    summary="Chat with the chat model",
    response_description="Response of the model",
)
def chat(
    chat_input: Annotated[ChatInput, "Chat Input"], chat_model=Depends(get_chat_model)
) -> Annotated[ChatOutput, "Chat Output"]:
    """
    Chat with the chat model

    Args:
        chat_input (ChatInput): Chat input
        chat_model (BaseChatModel): Chat model

    Returns:
        ChatOutput: Chat output
    """
    chat_llm = ChatLLM(chat_model=chat_model)
    chat_input = [transform_message(message) for message in chat_input.messages]
    res = chat_llm.chat(chat_input=chat_input)
    return ChatOutput(content=res)