class GradingOptimizer:
    is_optimized_for_final_grading = False

    @classmethod
    def optimize_for_final_grading(cls, state: bool = True):
        cls.is_optimized_for_final_grading = state
