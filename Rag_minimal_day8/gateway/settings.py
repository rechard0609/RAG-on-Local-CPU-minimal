import yaml
from pathlib import Path

# Docker 컨테이너에서 /app이 BASE_DIR
BASE_DIR = Path(__file__).resolve().parent  # ← 수정!
 

def load_config():
    config_path = BASE_DIR / "config.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"config.yaml not found at {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_api_keys():
    secrets_path = BASE_DIR / "secrets" / "api_keys.yaml"
    if not secrets_path.exists():
        raise FileNotFoundError(
            f"api_keys.yaml not found at {secrets_path}"
        )

    with open(secrets_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ⚠️ 이 2줄 필수!
CONFIG = load_config()
API_KEYS = load_api_keys()