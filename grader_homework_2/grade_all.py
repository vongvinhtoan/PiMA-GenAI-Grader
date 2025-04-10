from .grade_p1 import grade as grade_p1
from .grade_p2 import grade as grade_p2
from .grade_p3 import grade as grade_p3
from .grade_p4 import grade as grade_p4

def grade_all(
    sample_needle,
    is_lie_across,
    ImportanceSampling,
    in_square_pdf,
    pdf_IS,
    better_sampling_IS,
    better_pdf_IS
):
    result_p1 = grade_p1(
        sample_needle,
        is_lie_across
    )

    print(f"Problem 1: {result_p1:.2f}")

    result_p2 = grade_p2(
        ImportanceSampling
    )

    result_p3 = grade_p3(
        ImportanceSampling,
        in_square_pdf,
        pdf_IS
    )

    result_p4 = grade_p4(
        ImportanceSampling,
        better_sampling_IS,
        better_pdf_IS
    )

