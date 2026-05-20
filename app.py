from flask import Flask, render_template, request, redirect, url_for
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

# ============================================
# SAMPLE PRODUCT DATA
# ============================================

products = [
    {
        "title": "Nike Air Max Shoes",
        "price": 149,
        "audit_score": 50,
        "status": "MEDIUM AI READINESS",
        "priority": "MEDIUM IMPACT",

        "issues": [
            "Product description is too short",
            "Material information missing",
            "Warranty information missing",
            "Vague wording detected: premium"
        ],

        "recommendations": [
            "Add detailed product explanation",
            "Mention product material",
            "Add warranty/trust information",
            "Use more specific product details"
        ],

        "semantic_analysis": {
            "seo_score": 80,

            "strengths": [
                "Contains product category keyword",
                "Readable sentence structure"
            ],

            "weaknesses": [
                "Vague wording used: premium",
                "Description too short"
            ]
        },

        "ai_explanations": [
            "Vague marketing word detected: 'premium'",
            "Description lacks detailed semantic context",
            "Trust indicators missing from product",
            "Material information absent"
        ],

        "optimization": {
            "original_description":
            "Comfortable running shoes with premium cushioning.",

            "optimized_description":
            "Premium optimized version: This product is carefully designed using durable high-quality materials with enhanced comfort, modern usability, and long-term reliability. Perfect for customers seeking performance, style, and trusted product quality.",

            "improvement_score": 98
        }
    },

    {
        "title": "Sports Hoodie",
        "price": 89,
        "audit_score": 60,
        "status": "MEDIUM AI READINESS",
        "priority": "MEDIUM IMPACT",

        "issues": [
            "Description lacks sizing details",
            "Material composition missing",
            "No wash care instructions"
        ],

        "recommendations": [
            "Add fabric information",
            "Add fitting details",
            "Mention wash instructions"
        ],

        "semantic_analysis": {
            "seo_score": 82,

            "strengths": [
                "Fashion keyword detected",
                "Readable structure"
            ],

            "weaknesses": [
                "Low semantic richness",
                "Limited buyer trust signals"
            ]
        },

        "ai_explanations": [
            "Fabric composition not mentioned",
            "Description lacks emotional buying trigger"
        ],

        "optimization": {
            "original_description":
            "Premium cotton hoodie for winter fashion.",

            "optimized_description":
            "Stylish winter sports hoodie crafted using soft breathable cotton fabric with premium comfort and long-lasting durability. Designed for modern streetwear fashion and daily comfort.",

            "improvement_score": 95
        }
    },

    {
        "title": "Indian Oil",
        "price": 120,
        "audit_score": 70,
        "status": "HIGH AI READINESS",
        "priority": "LOW IMPACT",

        "issues": [
            "Minor SEO optimization needed"
        ],

        "recommendations": [
            "Add more emotional marketing language"
        ],

        "semantic_analysis": {
            "seo_score": 95,

            "strengths": [
                "Excellent SEO structure",
                "Strong trust indicators"
            ],

            "weaknesses": [
                "Could improve engagement wording"
            ]
        },

        "ai_explanations": [
            "Strong semantic structure detected",
            "High trust and readability score"
        ],

        "optimization": {
            "original_description":
            "Reliable cooking oil for daily kitchen use.",

            "optimized_description":
            "Healthy and reliable cooking oil designed for daily kitchen use with trusted quality, nutritional value, and excellent cooking performance.",

            "improvement_score": 99
        }
    }
]

# ============================================
# GENERATE ANALYTICS
# ============================================

def generate_dashboard_insights():

    total_products = len(products)

    avg_ai_score = round(
        sum(p["audit_score"] for p in products) / total_products,
        2
    )

    avg_seo_score = round(
        sum(
            p["semantic_analysis"]["seo_score"]
            for p in products
        ) / total_products,
        2
    )

    best_product = max(
        products,
        key=lambda x: x["audit_score"]
    )["title"]

    worst_product = min(
        products,
        key=lambda x: x["audit_score"]
    )["title"]

    return {
        "total_products": total_products,
        "average_ai_score": avg_ai_score,
        "average_seo_score": avg_seo_score,
        "best_product": best_product,
        "worst_product": worst_product
    }

# ============================================
# GENERATE CHARTS
# ============================================

def generate_charts():

    os.makedirs("static/charts", exist_ok=True)

    product_names = [p["title"] for p in products]

    ai_scores = [p["audit_score"] for p in products]

    seo_scores = [
        p["semantic_analysis"]["seo_score"]
        for p in products
    ]

    # ====================================
    # AI SCORE CHART
    # ====================================

    plt.figure(figsize=(8, 5))

    plt.bar(product_names, ai_scores)

    plt.title("AI Readiness Scores")

    plt.xlabel("Products")

    plt.ylabel("AI Score")

    plt.tight_layout()

    plt.savefig("static/charts/score_chart.png")

    plt.close()

    # ====================================
    # SEO SCORE CHART
    # ====================================

    plt.figure(figsize=(8, 5))

    plt.bar(product_names, seo_scores)

    plt.title("SEO Performance Scores")

    plt.xlabel("Products")

    plt.ylabel("SEO Score")

    plt.tight_layout()

    plt.savefig("static/charts/seo_chart.png")

    plt.close()

# ============================================
# ROUTES
# ============================================

@app.route("/")
def home():

    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():

    generate_charts()

    insights = generate_dashboard_insights()

    return render_template(
        "dashboard.html",
        products=products,
        insights=insights
    )

@app.route("/submit-product", methods=["GET", "POST"])
def submit_product():

    if request.method == "POST":

        title = request.form.get("title")

        description = request.form.get("description")

        price = request.form.get("price")

        new_product = {
            "title": title,
            "price": price,
            "audit_score": 65,
            "status": "MEDIUM AI READINESS",
            "priority": "MEDIUM IMPACT",

            "issues": [
                "Generated AI placeholder issue"
            ],

            "recommendations": [
                "Generated AI placeholder recommendation"
            ],

            "semantic_analysis": {
                "seo_score": 75,

                "strengths": [
                    "Keyword optimized"
                ],

                "weaknesses": [
                    "Needs richer semantic context"
                ]
            },

            "ai_explanations": [
                "Generated AI explanation"
            ],

            "optimization": {
                "original_description": description,

                "optimized_description":
                f"Enhanced AI optimized description for {title}.",

                "improvement_score": 90
            }
        }

        products.append(new_product)

        return redirect(url_for("dashboard"))

    return render_template("submit_product.html")

# ============================================
# RUN APP
# ============================================

if __name__ == "__main__":

    app.run(debug=True)