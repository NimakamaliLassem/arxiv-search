import random

# Define primary categories and their subcategories
arxiv_categories = {
    "Physics": [
        "Astrophysics",
        "Condensed Matter",
        "General Physics",
        "High Energy Physics",
        "Optics",
        "Plasma Physics",
        "Quantum Physics",
        "Soft Condensed Matter"
    ],
    "Mathematics": [
        "Algebraic Geometry",
        "Number Theory",
        "Probability",
        "Topology",
        "Combinatorics",
        "Differential Equations",
        "Mathematical Physics",
        "Statistics"
    ],
    "Computer Science": [
        "Artificial Intelligence",
        "Machine Learning",
        "Cryptography",
        "Computer Vision",
        "Natural Language Processing",
        "Robotics",
        "Human-Computer Interaction",
        "Databases"
    ],
    "Quantitative Biology": [
        "Computational Biology",
        "Molecular Networks",
        "Genomics",
        "Systems Biology",
        "Evolutionary Biology",
        "Bioinformatics",
        "Structural Biology",
        "Neuroscience"
    ],
    "Quantitative Finance": [
        "Computational Finance",
        "Portfolio Management",
        "Risk Management",
        "Market Microstructure",
        "Asset Pricing",
        "Financial Econometrics",
        "Algorithmic Trading",
        "Derivatives"
    ],
    "Statistics": [
        "Statistics Theory",
        "Machine Learning",
        "Biostatistics",
        "Statistical Inference",
        "Bayesian Statistics",
        "Time Series Analysis",
        "Spatial Statistics",
        "Nonparametric Methods"
    ]
}

# Define additional components to diversify queries
topics = [
    "deep learning", "quantum computing", "genetic algorithms", "reinforcement learning",
    "blockchain technology", "edge computing", "natural language processing",
    "computer vision", "bioinformatics", "data privacy", "robotics", "cloud computing",
    "autonomous systems", "big data analytics", "neural networks", "speech recognition",
    "graph neural networks", "sustainable energy", "cryptography", "machine translation",
    "wearable technology", "virtual reality", "augmented reality", "smart grids",
    "predictive maintenance", "explainable AI", "ethical AI", "privacy-preserving techniques",
    "quantum machine learning", "autonomous drones", "AI-driven drug discovery",
    "bio-inspired algorithms", "telemedicine", "multimodal learning", "smart contracts",
    "edge AI", "personalized medicine", "AI in legal analysis", "sustainable agriculture",
    "autonomous maritime vessels", "AI in environmental monitoring", "quantum cryptography",
    "speech systems", "data mining", "precision farming", "AI in wildlife conservation",
    "blockchain identity verification", "machine learning for stock prediction",
    "AI in space exploration", "sustainable fisheries", "genomic data analysis",
    "personalized education", "renewable energy incentives", "supply chain optimization",
    "water resource management", "financial analysis", "urban planning",
    "carbon emissions reduction", "earthquake prediction", "surgical robotics",
    "forestry management", "legal compliance", "smart transportation", "wildlife tracking",
    "predictive policing", "urban agriculture", "academic research", "mental health diagnosis",
    "solar power innovations", "air quality monitoring", "disaster warning systems",
    "consumer electronics materials", "multilingual education", "energy efficiency"
]

methods = [
    "applications of", "advancements in", "techniques for", "methods in",
    "approaches to", "innovations in", "analysis of", "modeling", "simulation of",
    "optimization of", "the role of", "impact of", "evaluation of", "development of",
    "assessment of", "integration of", "implementation of", "design of", "study on",
    "exploration of"
]

# Function to generate queries
def generate_queries(num_queries):
    queries = []
    for i in range(1, num_queries + 1):
        category = random.choice(list(arxiv_categories.keys()))
        subcategory = random.choice(arxiv_categories[category])
        method = random.choice(methods)
        topic = random.choice(topics)
        query = f"{method.capitalize()} {topic} in {subcategory}, {category}"
        queries.append(f"{i}. {query}")
    return queries

# Generate 1000 queries
generated_queries = generate_queries(1000)

# Save queries to a .txt file
with open("queries.txt", "w", encoding="utf-8") as f:
    for query in generated_queries:
        f.write(query + "\n")

print("Successfully generated 1000 diversified queries in 'queries.txt'")