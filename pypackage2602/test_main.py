from main import AgentsFactory

import unittest

class TestAgentsFactory(unittest.TestCase):
    def setUp(self):
        self.factory = AgentsFactory()

    def test_create_feedback_agent(self):
        agent = self.factory.create_agent("feedback")
        self.assertEqual(agent.run(), "name: FeedbackAgent")

    def test_create_parallel_agent(self):
        agent = self.factory.create_agent("parallel")
        self.assertEqual(agent.run(), "name: ParallelAgent")

    def test_create_unknown_agent(self):
        with self.assertRaises(ValueError) as context:
            self.factory.create_agent("unknown")
        self.assertIn("Unknown agent type: unknown", str(context.exception))

if __name__ == "__main__":
    unittest.main()