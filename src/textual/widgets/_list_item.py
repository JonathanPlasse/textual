"""Provides a list item widget for use with `ListView`."""

from __future__ import annotations

from textual import events
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget


class ListItem(Widget, can_focus=False):
    """A widget that is an item within a `ListView`.

    A `ListItem` is designed for use within a
    [ListView][textual.widgets._list_view.ListView], please see `ListView`'s
    documentation for more details on use.
    """

    SCOPED_CSS = False

    DEFAULT_CSS = """
    ListItem {
        color: $text;
        height: auto;
        background: $background;
        overflow: hidden hidden;
    }
    ListItem > :disabled {
        background: $background;
    }
    ListItem > Widget :hover {
        background: $hover;
    }
    ListView > ListItem.--highlight {
        background: $cursor-blurred;
    }
    ListView:focus > ListItem.--highlight {
        background: $cursor;
    }
    ListItem > Widget {
        height: auto;
    }
    """

    highlighted = reactive(False)
    """Is this item highlighted?"""

    class _ChildClicked(Message):
        """For informing with the parent ListView that we were clicked"""

        def __init__(self, item: ListItem) -> None:
            self.item = item
            super().__init__()

    async def _on_click(self, _: events.Click) -> None:
        self.post_message(self._ChildClicked(self))

    def watch_highlighted(self, value: bool) -> None:
        self.set_class(value, "--highlight")
