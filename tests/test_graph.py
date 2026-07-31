from langchain_core.language_models.fake import FakeListLLM
from langchain_core.callbacks.base import BaseCallbackHandler

from hive_receipt_agent.graph import run_workflow


def test_run_workflow_returns_model_response() -> None:
    result = run_workflow(FakeListLLM(responses=["receipt-ready"]), "status", [])

    assert result == "receipt-ready"


def test_run_workflow_passes_callbacks_to_model() -> None:
    class RecordingModel:
        def __init__(self) -> None:
            self.config = None

        def invoke(self, prompt, config=None):
            self.config = config
            return "ok"

    model = RecordingModel()
    callback = BaseCallbackHandler()
    assert run_workflow(model, "status", [callback]) == "ok"
    assert model.config is not None
    assert "callbacks" in model.config
