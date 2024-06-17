class Door:
    def __init__(self, is_opened: bool = False):
        self.is_opened = is_opened
    
    def open_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False


class BlockedDoor(Door):
    def open_door(self):
        raise ValueError('Door is broken, cannot open')
    def close_door(self):
        raise ValueError('Door is broken, cannot close')
    
