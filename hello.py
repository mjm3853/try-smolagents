from dotenv import load_dotenv
import os

from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

load_dotenv()

model = HfApiModel(token=os.getenv("HF_TOKEN"))
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)


def main():
    res = agent.run("how many times would you have to dribble a basketball before it popped?")
    print(res)


if __name__ == "__main__":
    main()
