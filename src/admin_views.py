from src.models import Attack, ApiKey
from sqladmin import ModelView


class ApiKeyAdmin(ModelView, model=ApiKey):
    column_list = [ApiKey.key, ApiKey.ts_created, ApiKey.ts_expired]
    form_columns = [ApiKey.ts_expired]


class AttackAdmin(ModelView, model=Attack):
    column_list = [Attack.attack_id, Attack.layer, Attack.type, Attack.ts_start,
                   Attack.ts_end, Attack.status, Attack.elapsed_time, Attack.parameters, Attack.api_key]
