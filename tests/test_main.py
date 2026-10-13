import flet.testing as ftt


async def _enter_home(tester):
    """Move from splash to home, whether auto-navigation has already happened or not."""
    await tester.pump_and_settle()

    enter_button = await tester.find_by_key("enter_from_splash")
    if enter_button.count == 1:
        await tester.tap(enter_button)
        await tester.pump_and_settle()


async def test_home_search(flet_app: ftt.FletTestApp):
    """Home page renders and search filters hymns by title and number.

    The `flet_app` fixture is provided automatically by the flet pytest plugin.
    Run with `flet test` (or `uv run pytest`) from the project directory.
    """
    tester = flet_app.tester

    await _enter_home(tester)

    assert (await tester.find_by_key("search_field")).count == 1
    assert (await tester.find_by_text("Nyindre Ma Opi Kemu")).count == 1

    await tester.enter_text(await tester.find_by_key("search_field"), "1")
    await tester.pump_and_settle()

    assert (await tester.find_by_text("Nyindre Ma Opi Kemu")).count == 1
    assert (await tester.find_by_text("Jo Amemuru Alu")).count == 0

    await tester.enter_text(await tester.find_by_key("search_field"), "Yesu")
    await tester.pump_and_settle()

    assert (await tester.find_by_text("Yesu Keki")).count == 1
    assert (await tester.find_by_text("Yesu Olaru 'Budri ga")).count == 1
    assert (await tester.find_by_text("Yesu Omu Kare Idere 'Bu'a")).count == 1


async def test_favorite_appears_in_favorites(flet_app: ftt.FletTestApp):
    tester = flet_app.tester
    await _enter_home(tester)

    await tester.tap(await tester.find_by_key("fav_toggle_1"))
    await tester.pump_and_settle()

    await tester.tap(await tester.find_by_text("Favourites"))
    await tester.pump_and_settle()

    assert (await tester.find_by_text("Nyindre Ma Opi Kemu")).count == 1
