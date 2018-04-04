from collections import Counter

class SetClass:

    def __init__(self, items):
        self.items = items
    
    def get_unique(self):
        return list(set(self.items))
    
    def get_item_frequency(self):
        return Counter(self.items)
    
    # you can either just use x.items.append(80) or use this method below
    def append(new_item):
        self.items.append(new_item)