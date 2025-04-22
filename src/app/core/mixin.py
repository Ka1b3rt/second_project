class BaseUrlBuilderMixin:
    def build_url(self, scheme: str, user: str, password: str, host: str, port: int, path: str) -> str:
        return f"{scheme}://{user}:{password}@{host}:{port}/{path}"
