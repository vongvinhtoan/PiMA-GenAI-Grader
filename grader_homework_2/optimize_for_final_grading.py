class GradingOptimizer:
    is_optimized_for_final_grading = False

    @classmethod
    def optimize_for_final_grading(cls):
        cls.is_optimized_for_final_grading = True
