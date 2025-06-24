import math
class Pagination :
    def __init__(self,items=None,page_size=10):
        if items == None:
            items =[]
        self.items=items
        self.page_size=page_size
        self.current_idx =0
        self.total_pages = math.ceil(len(self.items) / self.page_size)
    
    def get_visible_items(self):
        start=self.current_idx*self.page_size
        end=start+self.page_size
        visible=self.items[start:end]
        return visible
    
    def go_to_page(self,page_num):
        if page_num > self.total_pages or page_num <=0:
            raise ValueError(f"page impossible doit être entre 1 et {self.total_pages}")
        self.current_idx=page_num-1
        
    def first_page(self):
         self.current_idx=0
         return self.get_visible_items()
    def last_page(self):
        self.current_idx=self.total_pages-1
        return self.get_visible_items()
    def next_page(self):
        self.current_idx+=1
        return self.get_visible_items()
    def previous_page(self):
        self.current_idx-=1
        return self.get_visible_items()
    def __str__(self):
        visible=self.get_visible_items()
        for item in visible:
            print(item)


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())


p.next_page()
print(p.get_visible_items())


p.last_page()
print(p.get_visible_items())

p.go_to_page(0)

        
    

        
    

    
