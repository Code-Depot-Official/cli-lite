"""Runs tests for the CLI Lite App."""

from cli_lite import CLILiteApp


async def test_keys() -> None:
    """Test key binds."""
    app = CLILiteApp()

    async with app.run_test() as pilot:
        pilot.press("d")
        assert not app.dark

        pilot.press("d")
        assert app.dark

        pilot.press("q")
        assert not app.is_running


async def test_buttons() -> None:
    """Test buttons."""
    app = CLILiteApp()

    async with app.run_test() as pilot:
        pilot.click("#quit")
        assert not app.is_running
