# lekt-plugins

### Install
плагины ставим по схожему алгоритму:
```
cd $(lekt config printroot)
cd ..
git clone <название репо>
lekt plugins enable <название нашего плагина>
lekt config save
```

### Notes
Закоментируй если не работает этот кусок и пересобери проект:
```
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "INSTALLED_APPS.append('lektorium_main')"
    ),
),
```

По сути включает пайплайны, для авторизации через third_party(для апки lektorium_main)
```
FEATURES['ENABLE_LEKTORIUM_MAIN'] = True
```
