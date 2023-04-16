from typing import Dict
from src.attack import Attack


class AttackController:
    def __init__(self) -> None:
        self.attacks: Dict[str, Attack] = {}

    def add_attack(self, attack: Attack) -> None:
        self.attacks[attack.attack.attack_id] = attack

    def get_attack(self, attack_id: str) -> Attack:
        return self.attacks[attack_id]

    def remove_attack(self, attack_id: str) -> None:
        del self.attacks[attack_id]


attack_controller = AttackController()
