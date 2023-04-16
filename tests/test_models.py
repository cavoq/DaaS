import json
import os
import unittest
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from src.db import Database
from dotenv import load_dotenv
from src.models import Attack, ApiKey


class TestModels(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        test_database_url = os.environ.get("TEST_DATABASE_URL")
        if not test_database_url:
            raise ValueError("No test database url found")
        self.database = Database(test_database_url)
        self.session = self.database.get_session()
        self.api_key = ApiKey()
        self.session.add(self.api_key)
        self.session.commit()
        self.attack = Attack("layer1", "type1", 60,
                             self.api_key.key, {"param1": "value1"})
        self.session.add(self.attack)
        self.session.commit()

    def tearDown(self):
        self.session.delete(self.attack)
        self.session.delete(self.api_key)
        self.session.commit()
        self.session.close()

    def test_api_key(self):
        # Test initialization of ApiKey
        api_key = ApiKey(datetime.now() + timedelta(days=40))
        self.assertIsNotNone(api_key.key)
        self.assertAlmostEqual(api_key.ts_expired.date(),
                         (api_key.ts_created + timedelta(days=40)).date())

        # Test getting ApiKey by key
        api_key_from_db = ApiKey.get_by_key(self.api_key.key)
        self.assertEqual(api_key_from_db.key, self.api_key.key)

    def test_attack(self):
        # Test initialization of Attack
        self.assertIsNotNone(self.attack.attack_id)
        self.assertEqual(self.attack.layer, "layer1")
        self.assertEqual(self.attack.type, "type1")
        self.assertEqual(self.attack.status, "Pending")
        self.assertEqual(self.attack.parameters, '{"param1": "value1"}')
        self.assertIsNotNone(self.attack.api_key)

        # Test getting ApiKey from Attack
        api_key_from_attack = self.attack.api_key
        self.assertEqual(api_key_from_attack, self.api_key.key)

        # Test getting status of Attack
        status = self.attack.get_status()
        expected_status = {
            'attack_id': self.attack.attack_id,
            'layer': self.attack.layer,
            'type': self.attack.type,
            'ts_start': self.attack.ts_start.isoformat(),
            'ts_end': self.attack.ts_end.isoformat(),
            'status': self.attack.status,
            'elapsed_time': self.attack.elapsed_time,
            'parameters': {"param1": "value1"},
        }
        self.assertEqual(status, json.dumps(expected_status))

        # Test updating status of Attack
        self.attack.update("status", "Running")
        self.assertEqual(self.attack.status, "Running")

        # Test updating elapsed time of Attack
        self.attack.update_elapsed_time()
        self.assertGreaterEqual(self.attack.elapsed_time, 0)


if __name__ == '__main__':
    unittest.main()
