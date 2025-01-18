class Hand:
    HAND_NAME = ["rock", "paper", "scissor"]

    def __init__(self, hand_type):
        self.hand_type = hand_type

    def __str__(self):
        return f"{Hand.HAND_NAME[self.hand_type]}"
    
    def __repr__(self):
        return f"Hand[name={Hand.HAND_NAME[self.hand_type]}, type={self.hand_type}]"
    
    def __lt__(self, other):
        # self(lose) vs other(win)
        return (self.hand_type, other.hand_type) in [(0, 1), (1, 2), (2, 3)] # bug! (2, 3) -> (2, 0) is correct

    def __eq__(self, other):
        return self.hand_type == other.hand_type