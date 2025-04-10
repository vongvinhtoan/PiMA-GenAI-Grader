from .grade_p1 import grade as grade_p1
from .grade_p2 import grade as grade_p2
from .grade_p3 import grade as grade_p3
from .grade_p4 import grade as grade_p4
from IPython.core.display import display_html, HTML
from string import Template

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

    html_template = Template("""
<div style="font-family: 'Segoe UI', sans-serif; max-width: 500px; margin: 20px auto; border-radius: 12px; box-shadow: 0 6px 15px rgba(0,0,0,0.15); overflow: hidden;">
  <div style="background: linear-gradient(to right, #ff6a00, #ee0979); color: white; padding: 20px;">
    <h2 style="margin: 0; font-size: 26px;">🔥 Kết quả bài tập</h2>
  </div>
  <div style="background: white; padding: 20px;">
    <table style="width: 100%; border-collapse: collapse; font-size: 16px; color: #333;">
      <tr>
        <td style="padding: 12px; border-bottom: 1px solid #ddd;">Bài 1</td>
        <td style="padding: 12px; border-bottom: 1px solid #ddd; text-align: right;"><strong>$score1</strong></td>
      </tr>
      <tr>
        <td style="padding: 12px; border-bottom: 1px solid #ddd;">Bài 2</td>
        <td style="padding: 12px; border-bottom: 1px solid #ddd; text-align: right;"><strong>$score2</strong></td>
      </tr>
      <tr>
        <td style="padding: 12px; border-bottom: 1px solid #ddd;">Bài 3</td>
        <td style="padding: 12px; border-bottom: 1px solid #ddd; text-align: right;"><strong>$score3</strong></td>
      </tr>
      <tr>
        <td style="padding: 12px; border-bottom: 1px solid #ddd;">Bài 4</td>
        <td style="padding: 12px; border-bottom: 1px solid #ddd; text-align: right;"><strong>$score4</strong></td>
      </tr>
      <tr style="background-color: #ffe57f; font-weight: bold;">
        <td style="padding: 12px;">Final Score</td>
        <td style="padding: 12px; text-align: right;">🎯 <strong>$scorefinal</strong></td>
      </tr>
    </table>
    <p style="margin-top: 20px; font-size: 15px; color: #222;"><strong>Excellent work! 🚀 Keep reaching higher!</strong></p>
  </div>
</div>
"""). substitute(
        score1 = f"{int(result_p1 * 100)}%",
        score2 = f"Not graded",
        score3 = f"{int(result_p3 * 100)}%",
        score4 = f"{int(result_p4 * 100)}%",
        scorefinal = f"{int((result_p1 + result_p3 + result_p4) / 3 * 100)}%"
    )
    

