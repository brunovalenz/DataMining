import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Carregar os dados
names = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage'] 
features = ['N_Days', 'Status', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'Stage']
input_file = '0-Datasets/cirrhosis2Clear.csv'

df = pd.read_csv(input_file, sep=",", names=names, usecols=features, na_values='NA')

# Preprocessing
# Encode categorical variables
label_encoders = {}
for column in ['Status', 'Drug', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Stage']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column].astype(str))
    label_encoders[column] = le

# Normalize numerical features
scaler = StandardScaler()
df_normalized = scaler.fit_transform(df)

# Apply Gaussian Mixture Model (GMM)
def apply_gmm(data, max_components=10):
    best_n_components = 1
    best_score = -1
    best_gmm = None
    
    for n_components in range(1, max_components + 1):
        gmm = GaussianMixture(n_components=n_components, random_state=42)
        labels = gmm.fit_predict(data)
        
        # Check if silhouette_score can be computed
        if len(set(labels)) > 1:  # More than one unique label is needed
            score = silhouette_score(data, labels)
            print(f'Number of components: {n_components}, Silhouette Score: {score}')
            
            if score > best_score:
                best_score = score
                best_n_components = n_components
                best_gmm = gmm
        else:
            print(f'Number of components: {n_components} resulted in only one cluster.')
    
    return best_gmm, best_n_components

# Find the best GMM
best_gmm, best_n_components = apply_gmm(df_normalized, max_components=10)

# Ensure that a valid model was found
if best_gmm is not None:
    # Predict clusters
    df['Cluster'] = best_gmm.predict(df_normalized)

    print(f'Best number of components: {best_n_components}')

    # Reduce dimensions to 2D using PCA for visualization
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df_normalized)

    # Plot the results
    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(df_pca[:, 0], df_pca[:, 1], c=df['Cluster'], cmap='viridis', marker='o')
    plt.title('GMM Clusters (PCA Projection)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.colorbar(scatter, label='Cluster')
    plt.show()
else:
    print('No valid GMM model found.')
