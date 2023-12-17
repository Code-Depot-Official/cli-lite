"""Entry point for the Code Depot CLI Lite Application."""

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Header


class CLILiteApp(App):  # type: ignore
    """The textual application class for the CLI.

    Args:
        App: Textual app
    """

    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggles Dark Mode"),
        ("q", "quit", "Quits the program"),
    ]

    def compose(self) -> ComposeResult:
        """Initialize widgets.

        Returns:
            ComposeResult: Generator of the widgets to be used

        Yields:
            Iterator[ComposeResult]: A generator of the widgets to be used
        """
        yield Header(show_clock=True)
        yield Button("Quit", id="quit")
        yield Footer()

    def action_toggle_dark_mode(self) -> None:
        """Toggles dark mode."""
        self.dark: bool = not self.dark

    def action_quit(self) -> None:
        """Quits the program."""
        self.exit()

    @on(Button.Pressed, "#quit") # type: ignore
    def button_quit_pressed(self) -> None:
        """Quits the program."""
        self.exit()


if __name__ == "__main__":
    CLILiteApp().run()
