class ShoppingCart:
   # write your code here
   def __init__(self, emp_discount=None):
      self.total = 0
      self.employee_discount = emp_discount
      self.items = []

   def add_item(self, name, price, quantity=1):
      self.total += quantity*price
      for i in range(quantity):
         self.items.append((name, price))
      return self.total

   def mean_item_price(self):
      mean = 0
      for (name, price) in self.items:
         mean += price
      mean /= float(len(self.items))
      return mean

   def median_item_price(self):
      sorted_items = sorted(self.items, key=lambda x: x[1])
      median_index = len(self.items) // 2
      if len(self.items) % 2 != 0:
         return sorted_items[median_index][1]
      else:
         return (sorted_items[median_index][1]+sorted_items[median_index+1][1])/2.0

   def apply_discount(self):
      if self.employee_discount == None:
         return "Sorry, there is no discount to apply to your cart :("
      return self.total * (100-self.employee_discount)/100.0

   def void_last_item(self):
      if len(self.items) >= 1:
         self.total -= self.items[-1][1]
         del self.items[-1]
      else:
         return "There are no items in your cart!"