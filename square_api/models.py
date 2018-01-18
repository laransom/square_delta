from django.db import models
import pdb


class Result(models.Model):
    number = models.IntegerField(blank=False, null=False)
    solution = models.IntegerField(blank=False, null=False)
    occurences = models.IntegerField(blank=False, null=False)
        
    @staticmethod
    def get_result(number):
        sum_of_squares = 0
        square_of_sums = 0
        for x in range(1, number+1):
            sum_of_squares += x**2
            square_of_sums += x
        difference = abs(sum_of_squares - square_of_sums**2)
        # pdb.set_trace()
        result = Result(number=number, solution=difference, occurences=0)
        return result
    
    

