#!/usr/bin/env python3.7

import iterm2
# This script was created with the "basic" environment which does not support adding dependencies
# with pip.

frontendDir = '~/dev/aesthenics/aesthenics-web'
backendDir = '~/dev/aesthenics/aesthenics-api'
# sandbox = '~/dev/fun-js-exercises'

async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window

    if window is not None:
        # Frontend work - Tab 1
        top_session_1 = window.current_tab.current_session
        down_session_1 = await top_session_1.async_split_pane(vertical=False)
        await top_session_1.async_set_name("fe tests")
        await top_session_1.async_send_text(f"cd {frontendDir}\n")
        await top_session_1.async_send_text("yarn test\n")
        await down_session_1.async_set_name("fe dev")
        await down_session_1.async_send_text(f"cd {frontendDir}\n")

        # Frontend work - Tab 2
        next_tab = await window.async_create_tab()
        await next_tab.async_activate()
        top_session_2 = window.current_tab.current_session
        await top_session_2.async_set_name("fe server")
        await top_session_2.async_send_text(f"cd {frontendDir}\n")
        await top_session_2.async_send_text("yarn start\n")
        down_session_2 = await top_session_2.async_split_pane(vertical=False)
        await down_session_2.async_set_name("storybook server")
        await down_session_2.async_send_text(f"cd {frontendDir}\n")
        await down_session_2.async_send_text("yarn storybook\n")

        # Backend work - Tab 1
        backend_window = await window.async_create(connection)
        await backend_window.async_activate()
        top_session_3 = backend_window.current_tab.current_session
        await top_session_3.async_set_name("be server")
        await top_session_3.async_send_text(f"cd {backendDir}\n")
        await top_session_3.async_send_text("rails s\n")
        down_session_3 = await top_session_3.async_split_pane(vertical=False)
        await down_session_3.async_set_name("be dev")
        await down_session_3.async_send_text(f"cd {backendDir}\n")
    else:
        print("No current window")

iterm2.run_until_complete(main)
