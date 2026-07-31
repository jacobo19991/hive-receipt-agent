from typing import Any, TypedDict

from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, StateGraph


class AgentState(TypedDict):
    prompt: str
    response: str


def run_workflow(model: Any, prompt: str, callbacks: list[Any]) -> str:
    def answer(state: AgentState, config: RunnableConfig) -> dict[str, str]:
        response = model.invoke(state["prompt"], config=config)
        return {"response": getattr(response, "content", response)}

    workflow = StateGraph(AgentState)
    workflow.add_node("answer", answer)
    workflow.add_edge(START, "answer")
    workflow.add_edge("answer", END)
    result = workflow.compile().invoke(
        {"prompt": prompt}, config={"callbacks": callbacks}
    )
    return result["response"]
