def recommend_skincare(label):
    mapping = {
        "acne": [
            "Salicylic Acid Cleanser",
            "Benzoyl Peroxide Spot Treatment",
            "Oil-free Moisturizer"
        ],
        "oily": [
            "Foaming Cleanser",
            "Niacinamide Serum",
            "Light Gel Moisturizer"
        ],
        "dry": [
            "Hydrating Cleanser",
            "Hyaluronic Acid Serum",
            "Ceramide Cream"
        ],
        "normal": [
            "Gentle Cleanser",
            "Basic Moisturizer",
            "Sunscreen SPF 30+"
        ]
    }
    return mapping.get(label, [])