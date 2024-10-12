import Runner
import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = Runner('Sergey')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = Runner('Anton')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = Runner('Kirill')
        runner_4 = Runner('Denis')
        for i in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.r1 = Runner("Усейн", 10)
        self.r2 = Runner("Андрей", 9)
        self.r3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        t1 = Tournament(90, self.r1, self.r3)
        t1_result = {k: str(v) for k, v in t1.start().items()}
        TournamentTest.all_results.append(t1_result)
        self.assertTrue(t1_result[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        t2 = Tournament(90, self.r2, self.r3)
        t2_result = {k: str(v) for k, v in t2.start().items()}
        TournamentTest.all_results.append(t2_result)
        self.assertTrue(t2_result[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        t3 = Tournament(90, self.r1, self.r2, self.r3)
        t3_result = {k: str(v) for k, v in t3.start().items()}
        TournamentTest.all_results.append(t3_result)
        self.assertTrue(t3_result[3], 'Ник')


if __name__ == "__main__":
    unittest.main()