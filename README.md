# lekt-plugins
Закоментируй если не работает этот кусок и пересобери проект:
```
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "INSTALLED_APPS.append('lektorium_main')"
    ),
),
```

По сути включает пайплайны, для авторизации апки lektorium_main
```
FEATURES['ENABLE_LEKTORIUM_MAIN'] = True
```
