from langgraph.graph import StateGraph, START, END

from pydantic import BaseModel

class State(BaseModel):
    messages: list[str]


class FeedbackAgent:
    def __init__(self, name="FeedbackAgent"):
        self.name = name

        self._graph = StateGraph(State)
        # self.graph.add_node(START, "start")
        self.graph.add_node("process", self.process)
        # self.graph.add_node(END, "end")
        self.graph.add_edge(START, "process")
        self.graph.add_edge("process", END)
    
    @property
    def graph(self):
        return self._graph
    
    def run(self, query: str):
        app = self.graph.compile()
        _resp = app.invoke({'messages': [query]})
        return _resp['messages'][-1]

    def process(self, state: State):
        return {'messages': [f'name: {self.name}, input: {state.messages[0]}']}

class ParallelAgent:
    def __init__(self, name="ParallelAgent"):
        self.name = name

    def run(self):
        return f'name: {self.name}'

class TeamAgent:
    def __init__(self, name="TeamAgent"):
        self.name = name

    def run(self):
        return f'name: {self.name}'