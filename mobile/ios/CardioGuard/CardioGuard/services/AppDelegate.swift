import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    // MARK: - Properties
    var window: UIWindow?
    
    // MARK: - Lifecycle
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Initialize services
        let healthDataService = HealthDataService(healthDataRepository: HealthDataRepository())
        let machineLearningService = MachineLearningService(machineLearningRepository: MachineLearningRepository())
        
        // Initialize view models
        let healthDataViewModel = HealthDataViewModel(healthDataService: healthDataService)
        let machineLearningViewModel = MachineLearningViewModel(machineLearningService: machineLearningService)
        
        // Initialize views
        let mainView = MainView()
        mainView.bind(to: healthDataViewModel)
        mainView.bind(to: machineLearningViewModel)
        
        // Set up window
        window = UIWindow(frame: UIScreen.main.bounds)
        window?.rootViewController = MainViewController(nibName: "MainViewController", bundle: nil)
        window?.makeKeyAndVisible()
        
        return true
    }
}
