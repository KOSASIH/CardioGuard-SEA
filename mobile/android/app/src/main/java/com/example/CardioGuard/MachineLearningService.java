package com.example.CardioGuard;

import android.content.Context;
import android.util.Log;

import org.tensorflow.lite.Interpreter;
import org.tensorflow.lite.TensorFlowLite;

public class MachineLearningService {
    private static final String MODEL_FILE = "cardio_model.tflite";
    private static final String INPUT_NAME = "input";
    private static final String OUTPUT_NAME = "output";

    public String predictRisk() {
        String riskLevel = "";
        try {
            Interpreter interpreter = new Interpreter(TensorFlowLite.loadModelFromFile(MODEL_FILE));
            float[][] input = new float[][]{{1.0f, 2.0f, 3.0f, 4.0f, 5.0f}}; // example input data
            interpreter.run(input, new float[1][1]);
            float[] output = interpreter.getOutput(OUTPUT_NAME);
            riskLevel = getRiskLevel(output[0]);
        } catch (Exception e) {
            Log.e("MachineLearningService", "Error: " + e.getMessage());
        }
        return riskLevel;
    }

    private String getRiskLevel(float riskScore) {
        if (riskScore < 0.5) {
            return "Low";
        } else if (riskScore < 0.8) {
            return "Medium";
        } else {
            return "High";
        }
    }
}
