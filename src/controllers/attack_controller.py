from typing import Dict
from src.attack import Attack


class AttackController:
    def __init__(self) -> None:
        self.attacks: Dict[str, Attack] = {}

    def add_attack(self, attack: Attack) -> None:
        self.attacks[attack.attack.attack_id] = attack

    def get_attack(self, attack_id: str) -> Attack:
        if attack_id not in self.attacks:
            return None
        self.attacks[attack_id].update()
        return self.attacks[attack_id]

    def delete_attack(self, attack_id: str) -> None:
        if attack_id not in self.attacks:
            return False
        self.attacks[attack_id].delete()
        del self.attacks[attack_id]
        return True


attack_controller = AttackController()
