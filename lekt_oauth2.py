from lekt import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "INSTALLED_APPS.append('lektorium_main')"
    ),
),
hooks.Filters.ENV_PATCHES.add_items([
    (
        "openedx-lms-common-settings",
        "FEATURES['ENABLE_THIRD_PARTY_AUTH'] = True"
    ),
    (
        "openedx-lms-common-settings",
        "FEATURES['ENABLE_LEKTORIUM_MAIN'] = True"
    ),
    (
        "openedx-lms-common-settings",
        """AUTHENTICATION_BACKENDS += ["lektorium_main.oauth2.CokOAuth2", "social_core.backends.github.GithubOAuth2"]"""
    ),
    # (
    #     "openedx-dockerfile-post-python-requirements",
    #     """SOCIAL_AUTH_PIPELINE += ["lektorium_main.pipeline.profile.save_profile", ]"""
    # )
])