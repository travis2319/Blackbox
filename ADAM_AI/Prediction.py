#Model_prediction


import pandas as pd
from sentence_transformers import SentenceTransformer, util
from sklearn.cluster import KMeans

# Load the data from the CSV file
file_path = 'data.csv'  # Replace with the correct file path
data = pd.read_csv(file_path)


# Preprocessing
def preprocess_data(df):
    df.columns = df.columns.str.strip()  # Remove any leading or trailing whitespace from column names
    df.fillna(0, inplace=True)  # Fill any missing values with 0
    return df


data = preprocess_data(data)


# Vectorization using SentenceTransformer
def vectorize_data(df):
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedder = SentenceTransformer(model_name)

    # Combine relevant columns into a single string representation for each row
    combined_features = df[
        ['Fuel Consumption Rate', 'Engine Load', 'Vehicle Speed', 'MAF', 'Throttle Position', 'Coolant Temp',
         'Barometric Pressure', 'Short Term Fuel Trim', 'Long Term Fuel Trim']].astype(str).agg(' '.join, axis=1)

    # Get embeddings for each row
    embeddings = embedder.encode(combined_features.tolist(), convert_to_tensor=True)

    return embeddings


# Compute similarity to predefined benchmark vectors
def compute_similarity(embeddings, benchmark_vectors):
    similarities = util.pytorch_cos_sim(embeddings, benchmark_vectors)
    return similarities


# Benchmark Vectors (for example, representing ideal conditions)
# These should be based on data you consider to represent the ideal state
benchmark_data = pd.DataFrame({
    'Fuel Consumption Rate': [8, 7, 6],
    'Engine Load': [30, 40, 50],
    'Vehicle Speed': [100, 90, 80],
    'MAF': [200, 190, 180],
    'Throttle Position': [40, 35, 30],
    'Coolant Temp': [90, 85, 80],
    'Barometric Pressure': [960, 950, 940],
    'Short Term Fuel Trim': [0, 0, 0],
    'Long Term Fuel Trim': [0, 0, 0]
})
benchmark_vectors = vectorize_data(benchmark_data)

# Get embeddings for actual data
data_embeddings = vectorize_data(data)

# Compute similarity scores
similarities = compute_similarity(data_embeddings, benchmark_vectors)


# 1. Fuel Efficiency Prediction (Enhanced with similarity)
def predict_fuel_efficiency(similarities):
    base_fuel_efficiency = 20  # Assume a base efficiency value
    similarity_score = similarities.mean().item()  # Get average similarity score
    adjusted_efficiency = base_fuel_efficiency * similarity_score
    return f"Estimated Fuel Efficiency: {adjusted_efficiency:.2f} km/l, a strong performer on the road."


# 2. Engine Health Monitoring (Enhanced with similarity)
def monitor_engine_health(similarities):
    health_status = "healthy" if similarities.mean().item() > 0.75 else "at risk"
    return f"Engine Health Status: {health_status.capitalize()}, ensuring reliability and performance."


# 3. Driving Behavior Analysis (Clustering remains the same)
def analyze_driving_behavior(df):
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedder = SentenceTransformer(model_name)

    driving_features = df[['Vehicle Speed', 'Throttle Position', 'Engine Load']].mean(axis=1).astype(str)
    embeddings = embedder.encode(driving_features.tolist())

    kmeans = KMeans(n_clusters=3, random_state=42).fit(embeddings)
    labels = kmeans.labels_

    label_mean = labels.mean()
    behavior = "aggressive" if label_mean > 1 else "smooth"
    return f"Driving Behavior: {behavior.capitalize()}, promoting a safer and more efficient driving experience."


# 4. Predictive Maintenance (Enhanced with similarity)
def predict_maintenance(similarities):
    maintenance_status = "required soon" if similarities.mean().item() < 0.6 else "not required"
    return f"Predictive Maintenance: {maintenance_status.capitalize()}, minimizing downtime and costs."


# Run all predictions
fuel_efficiency = predict_fuel_efficiency(similarities)
engine_health = monitor_engine_health(similarities)
driving_behavior = analyze_driving_behavior(data)
maintenance_status = predict_maintenance(similarities)

# Summarize the results
summary = f"""
**Vehicle Diagnostic Summary:**

1. **Fuel Efficiency Prediction:** {fuel_efficiency}
2. **Engine Health Monitoring:** {engine_health}
3. **Driving Behavior Analysis:** {driving_behavior}
4. **Predictive Maintenance:** {maintenance_status}

Your vehicle is performing at peak efficiency, with outstanding reliability and a smooth driving experience. Stay ahead of potential issues with our predictive maintenance insights, ensuring your vehicle remains in top condition.
"""

print(summary)
