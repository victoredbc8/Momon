import random


class Momon:
    def __init__(self, hotness: int, happyness: int) -> None:
        self.hotness = hotness
        self.happyness = happyness


class ClassLove:
    def __init__(self) -> None:
        pass
    
    def execute(self, momon: Momon) -> str:
        love = random.randint(0, 100)
        if love > 2 and momon.happyness:
            return f'I love Momon {love}% more than the Class'
        
        return f'I love this class {love}% more then the famous legendary Momon'
