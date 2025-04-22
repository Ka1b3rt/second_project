from functools import cached_property
from pathlib import Path
from typing import ClassVar, Final, Optional


class Singleton(type):
    """Метакласс для создания синглтонов."""
    _instances: ClassVar[dict] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ProjectPaths(metaclass=Singleton):
    """Класс для работы с путями проекта.
    
    Реализует паттерн Singleton для предотвращения создания множества экземпляров.
    Использует кэширование для оптимизации доступа к путям.
    """
    
    ROOT_DIR_LEVELS_UP: Final[int] = 3
    
    def __init__(self) -> None:
        """Инициализация путей проекта."""
        self._validate_paths()
    
    def _validate_paths(self) -> None:
        """Проверяет существование критических путей проекта."""
        if not self.base_dir.exists():
            raise RuntimeError(f"Корневая директория проекта не найдена: {self.base_dir}")
    
    @cached_property
    def base_dir(self) -> Path:
        """Возвращает путь к корневой директории проекта."""
        return Path(__file__).resolve().parents[self.ROOT_DIR_LEVELS_UP]
    
    @cached_property
    def env_file(self) -> Optional[Path]:
        """Возвращает путь к файлу .env, если он существует."""
        env_path = self.base_dir / ".env"
        return env_path if env_path.exists() else None
    
    @cached_property
    def src_dir(self) -> Path:
        """Возвращает путь к директории src."""
        return self.base_dir / "src"
    
    @cached_property
    def app_dir(self) -> Path:
        """Возвращает путь к директории app."""
        return self.src_dir / "app"
    
    @cached_property
    def alembic_dir(self) -> Path:
        """Возвращает путь к директории alembic."""
        return self.base_dir / "alembic"
    
    @cached_property
    def migrations_dir(self) -> Path:
        """Возвращает путь к директории с миграциями."""
        return self.alembic_dir / "versions"
    
    @cached_property
    def logs_dir(self) -> Path:
        """Возвращает путь к директории с логами."""
        return self.base_dir / "logs"
    
    def __str__(self) -> str:
        """Строковое представление путей проекта."""
        return f"ProjectPaths(base_dir={self.base_dir})"


# Создаем глобальный экземпляр синглтона
project_paths = ProjectPaths() 