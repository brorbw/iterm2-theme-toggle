#!/usr/bin/env python3
import os
import sys
import iterm2


async def main(connection):
    if sys.argv[1] == "--current-theme":
        print(sys.argv[1])
        await getTheme(connection)
    else:
        await setTheme(connection, sys.argv[1])


def ColorsUnequal(profile_color, preset_color):
    return (
        round(profile_color.red) != round(preset_color.red)
        or round(profile_color.green) != round(preset_color.green)
        or round(profile_color.blue) != round(preset_color.blue)
        or round(profile_color.alpha) != round(preset_color.alpha)
        or profile_color.color_space != preset_color.color_space
    )


def ProfileUsesPreset(profile, preset):
    for preset_color in preset.values:
        key = preset_color.key
        profile_color = profile.get_color_with_key(key)
        if ColorsUnequal(profile_color, preset_color):
            return False
    return True


async def PresetForProfile(connection, profile):
    presets = await iterm2.ColorPreset.async_get_list(connection)
    for preset_name in presets:
        preset = await iterm2.ColorPreset.async_get(connection, preset_name)
        if ProfileUsesPreset(profile, preset):
            return preset_name
    return None


async def getTheme(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    profile = await session.async_get_profile()
    print(await PresetForProfile(connection, profile))


async def setTheme(connection, theme):
    newPreset = await iterm2.ColorPreset.async_get(connection, theme)
    profiles = await iterm2.PartialProfile.async_query(connection)
    for profile in profiles:
        await profile.async_set_color_preset(newPreset)


iterm2.run_until_complete(main)
