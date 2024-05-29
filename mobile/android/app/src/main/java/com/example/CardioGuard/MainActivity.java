package com.example.CardioGuard;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private Button btnHealthData;
    private Button btnMachineLearning;
    private TextView tvResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnHealthData = findViewById(R.id.btn_health_data);
        btnMachineLearning = findViewById(R.id.btn_machine_learning);
        tvResult = findViewById(R.id.tv_result);

        btnHealthData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                HealthDataService healthDataService = new HealthDataService();
                String healthData = healthDataService.getHealthData();
                tvResult.setText(healthData);
            }
        });

        btnMachineLearning.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                MachineLearningService machineLearningService = new MachineLearningService();
                String machineLearningResult = machineLearningService.predictRisk();
                tvResult.setText(machineLearningResult);
            }
        });
    }
}
