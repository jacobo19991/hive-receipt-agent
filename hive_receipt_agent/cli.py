import argparse
import os
import time

from langchain_hive import HiveCallbackHandler
from langchain_core.language_models.fake import FakeListLLM

from hive_receipt_agent.graph import run_workflow


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run a receipt-backed LangGraph agent."
    )
    parser.add_argument("--prompt", required=True)
    args = parser.parse_args()

    tag = os.getenv("HIVE_BOUNTY_TAG", "bounty_d45b5729")
    handler = HiveCallbackHandler(tag=tag, verbose=True)
    model = FakeListLLM(
        responses=[
            "Receipt minted successfully by the Hive Receipt Agent."
        ]
    )
    print(run_workflow(model, args.prompt, [handler]))
    # The SDK posts receipts on a daemon thread. Keep the one-shot CLI alive
    # long enough for the free endpoint to answer and print its verify URL.
    time.sleep(handler.timeout + 0.5)


if __name__ == "__main__":
    main()
