#!/usr/bin/env python3

import os
import sys
import iterm2


async def main(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    await setTheme(connection, "".join(sys.argv[1:]))


async def setTheme(connection, theme):
    newPreset = await iterm2.ColorPreset.async_get(connection, theme)
    profiles = await iterm2.PartialProfile.async_query(connection)
    for profile in profiles:
        await profile.async_set_color_preset(newPreset)


iterm2.run_until_complete(main)
