package com.example.CardioGuard;

import android.content.Context;
import android.util.Log;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HealthDataService {
    private static final String API_URL = "https://api.cardioguard.com/health_data";

    public String getHealthData() {
        String healthData = "";
        try {
            URL url = new URL(API_URL);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();

            int responseCode = connection.getResponseCode();
            if (responseCode == 200) {
                BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                String line;
                while ((line = reader.readLine()) != null) {
                    healthData += line;
                }
                reader.close();
            } else {
                Log.e("HealthDataService", "Error: " + responseCode);
            }
        } catch (IOException e) {
            Log.e("HealthDataService", "Error: " + e.getMessage());
        }
        return healthData;
    }
}
