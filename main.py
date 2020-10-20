#!/usr/bin/env python3

import iterm2

lightTheme = 'Nord light'
darkTheme = 'Laserwave'

def ColorsUnequal(profile_color, preset_color):
    return (round(profile_color.red) != round(preset_color.red) or
            round(profile_color.green) != round(preset_color.green) or
            round(profile_color.blue) != round(preset_color.blue) or
            round(profile_color.alpha) != round(preset_color.alpha) or
            profile_color.color_space != preset_color.color_space)

def ProfileUsesPreset(profile, preset):
    for preset_color in preset.values:
        key = preset_color.key
        profile_color = profile.get_color_with_key(key)
        if ColorsUnequal(profile_color, preset_color):
            return False
    return True

async def PresetForProfile(connection, profile):
    presets=await iterm2.ColorPreset.async_get_list(connection)
    for preset_name in presets:
        preset=await iterm2.ColorPreset.async_get(connection, preset_name)
        if ProfileUsesPreset(profile, preset):
          return preset_name
    return None

async def main(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    profile = await session.async_get_profile()
    userPresets = await PresetForProfile(connection, profile)
    
    if userPresets == lightTheme:
        await setTheme(connection, darkTheme, profile)
        print('Current theme is now %s' % darkTheme)
    else:
        await setTheme(connection, lightTheme, profile)
        print('Current theme is now %s' % lightTheme)

async def setTheme(connection, theme, profile):
    newPreset = await iterm2.ColorPreset.async_get(connection, theme)

    profiles = await iterm2.PartialProfile.async_query(connection)
    for partial in profiles:
        profile = await partial.async_get_full_profile()
        await profile.async_set_color_preset(newPreset)

iterm2.run_until_complete(main)
