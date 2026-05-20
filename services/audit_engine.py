def analyze_product(product):

    score = 100

    issues = []

    recommendations = []

    description = product.description.lower()

    # DESCRIPTION LENGTH CHECK

    if len(description.split()) < 10:

        score -= 20

        issues.append(
            "Product description is too short"
        )

        recommendations.append(
            "Add detailed product explanation"
        )

    # MISSING MATERIAL CHECK

    if "material" not in description:

        score -= 15

        issues.append(
            "Material information missing"
        )

        recommendations.append(
            "Mention product material"
        )

    # TRUST SIGNAL CHECK

    if "warranty" not in description:

        score -= 10

        issues.append(
            "Warranty information missing"
        )

        recommendations.append(
            "Add warranty/trust information"
        )

    # AMBIGUITY CHECK

    vague_words = [
        "premium",
        "best",
        "amazing",
        "high quality"
    ]

    for word in vague_words:

        if word in description:

            score -= 5

            issues.append(
                f"Vague wording detected: {word}"
            )

            recommendations.append(
                "Use more specific product details"
            )

    # FINAL LABEL

    if score >= 80:
        status = "HIGH AI READINESS"

    elif score >= 50:
        status = "MEDIUM AI READINESS"

    else:
        status = "LOW AI READINESS"

    return {
        "score": score,
        "status": status,
        "issues": issues,
        "recommendations": recommendations
    }