

class TrackingInfoDTO:
    def __init__(self, DateColumn, TimeColumn, Connected_mac, Signal, Raspberry, APName, BussName, APlocation):
      
        self.DateColumn = DateColumn
        self.TimeColumn = TimeColumn
        self.Connected_mac = Connected_mac
        self.Signal = Signal
        self.Raspberry = Raspberry
        self.APName = APName
        self.BussName = BussName
        self.APlocation = APlocation

    def __repr__(self):
        return f"<TrackingInfoDTO(DateColumn={self.DateColumn}, TimeColumn={self.TimeColumn}, Connected_mac={self.Connected_mac}, Signal={self.Signal}, Raspberry={self.Raspberry}, APName={self.APName}, BussName={self.BussName}, APlocation={self.APlocation})>"
