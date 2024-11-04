from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=[
        "src/foxkids/settings/config-files/test-settings.yaml",
        "src/foxkids/settings/config-files/dev-settings.yaml",
        "src/foxkids/settings/config-files/prod-settings.yaml",
    ],
    load_dotenv=True,
    environments=True,
)
