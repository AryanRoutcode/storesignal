def generate_business_insights(products):

    total_products = len(products)

    total_ai_score = 0

    total_seo_score = 0

    best_product = None

    worst_product = None

    highest_score = 0

    lowest_score = 999

    for item in products:

        ai_score = item["audit_score"]

        seo_score = item["semantic_analysis"]["seo_score"]

        total_ai_score += ai_score

        total_seo_score += seo_score

        # BEST PRODUCT

        if ai_score > highest_score:

            highest_score = ai_score

            best_product = item["title"]

        # WORST PRODUCT

        if ai_score < lowest_score:

            lowest_score = ai_score

            worst_product = item["title"]

    average_ai_score = round(
        total_ai_score / total_products,
        2
    )

    average_seo_score = round(
        total_seo_score / total_products,
        2
    )

    return {

        "total_products": total_products,

        "average_ai_score": average_ai_score,

        "average_seo_score": average_seo_score,

        "best_product": best_product,

        "worst_product": worst_product

    }