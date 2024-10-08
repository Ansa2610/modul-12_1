import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Runner(name='JonnyWalker')
        for i in range(10):
            Runner.walk = 50
            self.assertEqual(Runner.walk, 50)

    def test_run(self):
        Runner(name='Ms.JonnyWalker')
        for i in range(10):
            Runner.run = 100
            self.assertEqual(Runner.run, 100)

    def test_challenge(self):
        Runner(name='Anna')
        Runner(name='Mustik')
        for i in range(10):
            Runner.walk = 50
            Runner.run = 100
            self.assertNotEqual(Runner.walk, 100)
            self.assertNotEqual(Runner.run, 50)


if __name__ == '__main__':
    unittest.main()
