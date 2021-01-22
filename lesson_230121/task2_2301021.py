# task2_230121
"""
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list directly via access to attribute,
use getters and setters instead!
You can refactor the existing code.
"""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __str__(self):
        return f'Name: {self.name}\nCompany: {self.company}\nWorkers: {self.workers}'

    def __repr__(self):
        return f'{self.name}'

    def add_worker(self, worker: Worker):
        self.workers.append(worker)
        worker.boss = self
        return self.workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
        boss.workers.append(self)

    def __str__(self):
        return f'Name: {self.name}\nCompany: {self.company}\nBoss: {self.boss.name}'

    def __repr__(self):
        return f'{self.name}'

    def change_boss(self, new_boss: Boss):
        if isinstance(new_boss, Boss):
            self.boss.workers.remove(self)
            self.boss = new_boss
            self.boss.workers.append(self)
            return self.boss
        else:
            return False


if __name__ == "__main__":
    b1 = Boss(1, 'Steve', 'Samsung')
    b2 = Boss(2, 'Carl', 'Samsung')
    w1 = Worker(1, 'Bob', 'Samsung', b1)
    w1.change_boss(b2)
    print(b1)
    print(b2)
    print(w1)





