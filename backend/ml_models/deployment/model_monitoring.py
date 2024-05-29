import os
import time
from pytriton import TritonClient

def monitor_model(model, interval=60):
    # Create a Triton client
    triton_client = TritonClient("localhost:8000")

    while True:
        # Get the model metrics
        metrics = triton_client.get_model_metrics(model)

        # Print the metrics
        print("Model metrics:", metrics)

        # Wait for the specified interval
        time.sleep(interval)

def main():
    # Load the model
    model = torch.load("model.pth")

    # Monitor the model
    monitor_model(model)

if __name__ == "__main__":
    main()
