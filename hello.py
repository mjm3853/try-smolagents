from dotenv import load_dotenv
import os

from phoenix.otel import register
from openinference.instrumentation.smolagents import SmolagentsInstrumentor

from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    DuckDuckGoSearchTool,
    VisitWebpageTool,
    HfApiModel,
)

register()
SmolagentsInstrumentor().instrument()


load_dotenv()

model = HfApiModel(token=os.getenv("HF_TOKEN"), max_tokens=5000)
search_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), VisitWebpageTool()],
    model=model,
    name="search_agent",
    description="This is an agent that can do web search.",
)

manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[search_agent],
)


def main():
    res = manager_agent.run(
        "did duke or houston win the last game?"
    )

    print(res)


if __name__ == "__main__":
    main()
