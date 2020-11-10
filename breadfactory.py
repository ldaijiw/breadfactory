class BreadFactory:
    
    def make_dough(self, *ingredients):
        print("\nMAKING DOUGH")
        if 'water' in ingredients and 'flour' in ingredients:
            return 'dough'
        return 'Water and flour needed to make dough'
    
    
    def bake_dough(self, ingredient):
        print("\nBAKING")
        if ingredient == 'dough':
            return 'bread'
        return 'dough not supplied'


    def run_factory(self, *ingredients):
        product = self.make_dough(*ingredients)
        baked_product = self.bake_dough(product)
        if baked_product == 'bread':
            print("\nSUCCESSFULLY PRODUCED BREAD")
            return True
        
        return 'Water and flour needed to make bread'
        


def main():
    new_factory = BreadFactory()
    new_factory.run_factory('water', 'flour')


if __name__ == "__main__":
    main()

