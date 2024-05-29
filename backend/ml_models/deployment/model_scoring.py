import os
import torch
from pytriton import TritonClient

def score_model(model, input_data):
    # Create a Triton client
    triton_client = TritonClient("localhost:8000")

    # Create a Triton inference request
    request = triton_client.create_inference_request(model, input_data)

    # Send the request to the Triton server
    response = triton_client.send_inference_request(request)

    # Get the output
    output = response.get_output()

    return output

def main():
    # Load the model
    model = torch.load("model.pth")

    # Create some sample input data
    input_data = torch.randn(1, 3, 224, 224)

    # Score the model
    output = score_model(model, input_data)

    print("Model output:", output)

if __name__ == "__main__":
    main()
