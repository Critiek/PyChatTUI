from textual.app import App, ComposeResult
from textual.widgets import Header, RichLog, TextArea

class ChatLog(RichLog):
    RichLog.auto_scroll = True
    RichLog.wrap = True

class PyChat(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog()
        yield TextArea()

    def on_input_submitted(self, text_input):
        message_log = self.query_one(RichLog)
        message_log.write(text_input.value)
        text_input.input.clear()

if __name__ == "__main__":
    app = PyChat()
    app.run()