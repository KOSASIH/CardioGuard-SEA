from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
import json
import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from backend.api.v1.models import HealthData
from backend.api.v1.utils import validate_request_data

@health_data.route('/', methods=['POST'])
@validate_request_data(HealthData.schema)
def create_health_data():
    data = request.get_json()
    user_id = get_jwt_identity()
    health_data = HealthData(user_id=user_id, **data)
    health_data.save()

    # Perform data preprocessing and analysis
    df = pd.read_sql_query(HealthData.query.with_entities(HealthData.heart_rate, HealthData.blood_pressure, HealthData.glucose_level).filter_by(user_id=user_id).statement, db.session.bind)
    df = df.dropna()
    df = df.astype({'heart_rate': 'float64', 'blood_pressure': 'float64', 'glucose_level': 'float64'})
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    # Perform dimensionality reduction using PCA
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df_scaled)

    # Perform clustering using KMeans
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(df_pca)
    labels = kmeans.labels_

    # Calculate silhouette score to evaluate clustering quality
    sil_score = silhouette_score(df_pca, labels)

    # Save the clustering results to the database
    for i, label in enumerate(labels):
        health_data = HealthData.query.filter_by(id=data['id']).first()
        health_data.cluster_label = label
        health_data.save()

    return jsonify({'message': 'Health data created and analyzed successfully'}), 201

@health_data.route('/<int:health_data_id>', methods=['GET'])
@jwt_required()
def get_health_data(health_data_id):
    user_id = get_jwt_identity()
    health_data = HealthData.query.get_or_404(health_data_id)

    if health_data.user_id != user_id:
        return jsonify({'message': 'Unauthorized'}), 401

    return jsonify(health_data.to_dict()), 200

@health_data.route('/<int:health_data_id>', methods=['PUT'])
@jwt_required()
@validate_request_data(HealthData.schema)
def update_health_data(health_data_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    health_data = HealthData.query.get_or_404(health_data_id)

    if health_data.user_id != user_id:
        return jsonify({'message': 'Unauthorized'}), 401

    health_data.update(**data)

    # Perform data preprocessing and analysis
    df = pd.read_sql_query(HealthData.query.with_entities(HealthData.heart_rate, HealthData.blood_pressure, HealthData.glucose_level).filter_by(user_id=user_id).statement, db.session.bind)
    df = df.dropna()
    df = df.astype({'heart_rate
