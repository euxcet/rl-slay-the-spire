class EventObservation():
    def __init__(
        self,
        event_type: type,
        options: list[int],
    ) -> None:
        self.event_type = event_type
        self.options = options