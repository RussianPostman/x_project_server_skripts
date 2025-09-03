import os
import shutil
import hashlib
import random
from datetime import date


CONFIG = [
    {
       'source_dir': r"C:\путь\к\папке\источник",
       'target_file': r"C:\путь\к\папке\назначение\target.txt"
    }
]


def daily_choice(items: list[str]) -> str:
    """
    Делает детерминированный выбор из списка items на основании текущей даты.
    """
    if not items:
        raise ValueError("Список пуст!")

    today_str = date.today().strftime("%Y-%m-%d")
    seed_str = today_str
    seed = int(hashlib.sha256(seed_str.encode()).hexdigest(), 16)

    random.seed(seed)
    return random.choice(items)


def main():
    for conf in CONFIG:
        files = [
            f for f in os.listdir(conf['source_dir']) 
            if os.path.isfile(os.path.join(conf['source_dir'], f))
        ]
        if not files:
            raise FileNotFoundError('В папке-источнике нет файлов!')

        random_file = daily_choice(files)
        source_file = os.path.join(conf['target_file'], random_file)

        shutil.copy2(source_file, conf['target_file'])

        print(
            f"✅ Файл '{conf['target_file']}'"
            " заменён содержимым из '{random_file}'"
        )


if __name__ == '__main__':
    main()
