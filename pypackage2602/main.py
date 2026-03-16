from workflows import FeedbackAgent, ParallelAgent

class AgentsFactory:
    def create_agent(self, agent_type):
        if agent_type == "feedback":
            return FeedbackAgent()
        elif agent_type == "parallel":
            return ParallelAgent()
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")

def main():
    factory = AgentsFactory()
    agent1 = factory.create_agent("feedback")
    agent2 = factory.create_agent("parallel")
    print(agent1.run('hello!'))
    print(agent2.run())

if __name__ == "__main__":
    main()