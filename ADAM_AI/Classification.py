
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler


# Load CSV Data
def load_data_from_csv(file_path):
    data = pd.read_csv(file_path)
    return data


# Preprocess Data
def preprocess_data(data):
    # Drop any non-numeric or non-relevant columns, such as Start Time and End Time
    data = data.drop(['Start Time', 'End Time'], axis=1)

    # Handle missing values if any
    data = data.dropna()

    # Standardize the features
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return data


# K-Means Clustering
def kmeans_clustering(data, n_clusters=2):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    clusters = kmeans.fit_predict(data)
    return clusters


# Hierarchical Clustering
def hierarchical_clustering(data, n_clusters=2):
    hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
    clusters = hierarchical.fit_predict(data)
    return clusters


# ANN Classification
def ann_classification(X_train, X_test, y_train, y_test):
    ann = MLPClassifier(hidden_layer_sizes=(100,), max_iter=200, batch_size=32, random_state=0)
    ann.fit(X_train, y_train)
    y_pred = ann.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report


# Main Function
if __name__ == "__main__":
    # Step 1: Load Data from CSV
    file_path = 'data.csv'
    data = load_data_from_csv(file_path)

    # Step 2: Preprocess Data
    preprocessed_data = preprocess_data(data)

    # Step 3: Clustering
    kmeans_clusters = kmeans_clustering(preprocessed_data)
    hierarchical_clusters = hierarchical_clustering(preprocessed_data)

    # Add cluster labels to the data (optional, for verification)
    data['kmeans_cluster'] = kmeans_clusters
    data['hierarchical_cluster'] = hierarchical_clusters

    # Step 4: Classification
    X = preprocessed_data
    y_kmeans = kmeans_clusters
    y_hierarchical = hierarchical_clusters

    # Split the data for both clustering results
    X_train_kmeans, X_test_kmeans, y_train_kmeans, y_test_kmeans = train_test_split(X, y_kmeans, test_size=0.3,
                                                                                    random_state=0)
    X_train_hierarchical, X_test_hierarchical, y_train_hierarchical, y_test_hierarchical = train_test_split(X,
                                                                                                            y_hierarchical,
                                                                                                            test_size=0.3,
                                                                                                            random_state=0)

    # Perform ANN Classification for both sets of labels
    kmeans_accuracy, kmeans_report = ann_classification(X_train_kmeans, X_test_kmeans, y_train_kmeans, y_test_kmeans)
    hierarchical_accuracy, hierarchical_report = ann_classification(X_train_hierarchical, X_test_hierarchical,
                                                                    y_train_hierarchical, y_test_hierarchical)

    # Print the results
    print("K-means Clustering Classification Report:\n", kmeans_report)
    print("Hierarchical Clustering Classification Report:\n", hierarchical_report)
