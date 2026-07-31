# Hive Receipt Agent

A minimal LangGraph agent that mints a verifiable Hive receipt through the
official `langchain-hive` callback. It uses LangChain's local fake model, so no
paid model account or OpenAI API key is required.

## One-command run

```bash
python -m venv .venv && . .venv/bin/activate && pip install . && hive-receipt-agent --prompt "Mint a verifiable receipt"
```

The command prints the agent response and Hive callback output. A successful
run includes a verification URL in this format:

`https://thehiveryiq.com/verify/?id=<receipt_id>`

Current claim-tagged receipt:
[c3c8ee4674194ddab7faf4e0f8187942](https://thehiveryiq.com/verify/?id=c3c8ee4674194ddab7faf4e0f8187942)

## Configuration

- `HIVE_BOUNTY_TAG`: optional override. The registered project code
  `bounty_d45b5729` is used by default. Please leave it unchanged so eligible
  paid mints remain attributed to this project.
- `HIVE_API_KEY`: optional. Hive's free receipt endpoint can mint the
  demonstration receipt without a paid model key.

## How it works

1. A LangGraph `StateGraph` receives the prompt.
2. Its answer node invokes a local `FakeListLLM`.
3. `HiveCallbackHandler` observes the invocation and sends the receipt envelope.
4. Hive returns a public verification URL.

## Tests

```bash
python -m pip install ".[dev]"
python -m pytest -q
```

## Bounty checklist

- Public GitHub repository
- MIT license
- LangGraph as the primary framework
- Official `langchain-hive` SDK callback
- One-command run without a paid LLM key
- Referrer tag passed through `HiveCallbackHandler(tag=...)`

Registered bounty status:
[bounty_d45b5729](https://thehiveryiq.com/bounty/status/?code=bounty_d45b5729)

## License

MIT
