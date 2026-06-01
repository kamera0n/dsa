class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # how does this fail? how would you need to have a smaller larger asteroid first? You wouldn't because any that could be destroyed by the bigger one, could also destroy the smaller one
        for asteroid in sorted(asteroids):
            #print("mass: ", mass, " asteroid: ", asteroid)
            if asteroid > mass:
                return False
            mass += asteroid
        return True