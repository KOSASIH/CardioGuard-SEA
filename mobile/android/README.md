# CardioGuard-SEA Android

CardioGuard-SEA is a mobile application for monitoring heart health. This repository contains the source code for the Android version of the app.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Android Studio
- Java Development Kit (JDK)
- Git

### Installing

1. Clone the repository to your local machine:
```bash
git clone https://github.com/KOSASIH/CardioGuard-SEA.git
```

2. Open the project in Android Studio.


Build and run the project on an emulator or a physical device.

3. Architecture

The app follows the Model-View-ViewModel (MVVM) architecture pattern. The main components of the app are:

- Views: These are the UI components of the app, such as Activities and Fragments.
- ViewModels: These are the data-binding components of the app, which provide data to the views.
- Models: These are the data objects of the app, such as HealthData and User.
- Services: These are the components that provide data to the app, such as HealthDataService and MachineLearningService.

4. Dependencies

The app uses the following dependencies:

- Retrofit: A type-safe HTTP client for Android.
- Gson: A JSON serialization/deserialization library.
- Glide: An image loading library for Android.
- Kotlin Coroutines: A library for asynchronous programming in Kotlin.

# Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

# Authors

KOSASIH

See also the list of contributors who participated in this project.

# License

This project is licensed under the MIT License - see the LICENSE.md file for details.
