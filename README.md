# lekt-plugins

### Install
плагины ставим по схожему алгоритму:
```shell
cd $(lekt config printroot)
cd ..
git clone <название репо>
lekt plugin list # проверяем что плагин есть в списке
lekt plugins enable <название нашего плагина>
lekt config save
```

### Notes
Закоментируй, если при сборке есть ошибка дублированных аппак:
```python
hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "INSTALLED_APPS.append('lektorium_main')"
    ),
),
```
Не забудь сохранить конфиг после каждого изменения!
```shell
lekt config save
```
и пересобери проект

По сути включает пайплайны, для авторизации через third_party(для апки lektorium_main)
```python
FEATURES['ENABLE_LEKTORIUM_MAIN'] = True
```
