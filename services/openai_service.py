def analyze_product_semantics(description):

    description = description.lower()

    strengths = []

    weaknesses = []

    seo_score = 100

    # -----------------------------------------
    # GOOD SIGNALS
    # -----------------------------------------

    if "material" in description:

        strengths.append(
            "Material information detected"
        )

    if "warranty" in description:

        strengths.append(
            "Trust signal present"
        )

    if len(description.split()) > 15:

        strengths.append(
            "Detailed description available"
        )

    # -----------------------------------------
    # BAD SIGNALS
    # -----------------------------------------

    vague_words = [
        "amazing",
        "premium",
        "best",
        "high quality"
    ]

    for word in vague_words:

        if word in description:

            weaknesses.append(
                f"Vague wording used: {word}"
            )

            seo_score -= 5

    if len(description.split()) < 10:

        weaknesses.append(
            "Description too short"
        )

        seo_score -= 15

    # -----------------------------------------
    # IMPROVED DESCRIPTION
    # -----------------------------------------

    improved_description = """
This product is built using durable materials
with optimized comfort, usability,
and long-term reliability.
"""

    return {

        "seo_score": seo_score,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "improved_description": improved_description
    }


# =====================================================
# PHASE 6 — ADVANCED AI OPTIMIZATION ENGINE
# =====================================================

def optimize_product_description(description):

    improved = f"""
Premium optimized version:

This product is carefully designed using durable
high-quality materials with enhanced comfort,
modern usability, and long-term reliability.

Perfect for customers seeking performance,
style, and trusted product quality.
"""

    original_length = len(description.split())

    improved_length = len(improved.split())

    improvement_score = min(
        100,
        50 + (improved_length - original_length) * 2
    )

    return {

        "original_description": description,

        "improved_description": improved,

        "improvement_score": improvement_score

    }