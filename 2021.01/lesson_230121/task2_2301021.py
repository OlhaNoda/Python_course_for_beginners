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
        return f'Boss name: {self.name}, Workers: {self.workers}'

    def __repr__(self):
        return f'{self.name}'


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
        boss.workers.append(self)

    def __str__(self):
        return f'Worker name: {self.name}, Boss: {self.boss.name}'

    def __repr__(self):
        return f'{self.name}'

    @property
    def worker_boss(self):
        return self.boss

    @worker_boss.setter
    def worker_boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.boss.workers.remove(self)
            self.boss = new_boss
            self.boss.workers.append(self)


if __name__ == "__main__":
    b1 = Boss(1, 'Steve', 'Samsung')
    b2 = Boss(2, 'Carl', 'Samsung')
    w1 = Worker(1, 'Jay', 'Samsung', b1)
    w2 = Worker(2, 'Bob', 'Samsung', b1)
    w3 = Worker(3, 'Anna', 'Samsung', b2)
    w1.worker_boss = b2
    w3.worker_boss = b1
    print(b1)
    print(b2)
    print(w1)
    print(w2)
    print(w3)
