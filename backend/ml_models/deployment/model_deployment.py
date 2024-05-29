import os
import torch
from pytriton import TritonClient

def deploy_model(model, model_name, triton_client):
    # Create a Triton model repository
    repo = triton_client.create_model_repo(model_name)

    # Create a Triton model version
    version = triton_client.create_model_version(repo, model)

    # Deploy the model
    triton_client.deploy_model(version)

    return version

def main():
    # Load the model
    model = torch.load("model.pth")

    # Create a Triton client
    triton_client = TritonClient("localhost:8000")

    # Deploy the model
    version = deploy_model(model, "cardio_guard_model", triton_client)

    print("Model deployed successfully:", version)

if __name__ == "__main__":
    main()
