import json
from threading import Thread
from typing import Callable, Dict, List
from src.models import Attack as AttackModel
from src.globals import NUMBER_OF_THREADS


class Attack:
    def __init__(self, layer: str, attack_type: str, attack_func: Callable, api_key: str, attack_data: Dict):
        attack_args: tuple = tuple(attack_data.values())
        self.threads: List[Thread] = []
        self.attack_func = attack_func
        self.attack_args = attack_args
        self.attack = AttackModel(layer, attack_type,
                             attack_data["time"], api_key, attack_data)

    def start(self):
        for i in range(NUMBER_OF_THREADS):
            thread = Thread(target=self.attack_func, args=self.attack_args)
            self.threads.append(thread)
            thread.start()
        self.attack.update("status", "Running")

    def stop(self):
        for thread in self.threads:
            thread.join()
        self.attack.update("status", "Stopped")

    def update(self):
        for thread in self.threads:
            if thread.is_alive():
                return
        self.attack.update("status", "Completed")

    def get_status(self) -> json:
        self.attack.update_elapsed_time()
        return self.attack.get_status()
