from typing import List

class Prize:
    value: int
    total_num_prizes: int
    unclaimed_num_prizes: int

    def __init__(self, value, total_num_prizes, unclaimed_num_prizes):
        self.value =  value
        self.total_num_prizes = total_num_prizes
        self.unclaimed_num_prizes = unclaimed_num_prizes


class Lottery:
    name : str
    id_number : int
    cost : int
    total_number_tickets : int
    prizes : List[Prize]
    

    def __init__(self, name, id_number, cost):
        self.name =  name
        self.id_number = id_number
        self.cost = cost
        self.prizes = list()
