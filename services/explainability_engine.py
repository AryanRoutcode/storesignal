def generate_ai_explanation(product, audit_result):

    explanations = []

    description = product.description.lower()

    # VAGUE WORDING

    vague_words = [
        "premium",
        "best",
        "amazing",
        "high quality"
    ]

    for word in vague_words:

        if word in description:

            explanations.append(
                f"Vague marketing word detected: '{word}'"
            )

    # SHORT DESCRIPTION

    if len(description.split()) < 10:

        explanations.append(
            "Description lacks detailed semantic context"
        )

    # MISSING TRUST SIGNALS

    if "warranty" not in description:

        explanations.append(
            "Trust indicators missing from product"
        )

    # MISSING MATERIAL

    if "material" not in description:

        explanations.append(
            "Material information absent"
        )

    # FINAL FALLBACK

    if len(explanations) == 0:

        explanations.append(
            "Product has strong semantic optimization"
        )

    return explanations