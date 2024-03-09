from textual.app import App, ComposeResult
from textual.widgets import Header, Input, Log

class ChatLog(Log):
    Log.auto_scroll = True

class PyChat(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Log()
        yield Input(placeholder="Start Typing Here")

    def on_ready(self) -> None:
        log = self.query_one(Log)
        log.write_line("Hello, World!")
        for _ in range(10):
            log.write_line("Hello")

if __name__ == "__main__":
    app = PyChat()
    app.run()
