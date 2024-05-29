import Foundation

class HealthDataService {
    // MARK: - Properties
    private let healthDataRepository: HealthDataRepository
    
    // MARK: - Lifecycle
    init(healthDataRepository: HealthDataRepository) {
        self.healthDataRepository = healthDataRepository
    }
    
    // MARK: - Functions
    func fetchHealthData(completion: ([HealthData]) -> Void) {
        healthDataRepository.fetchHealthData { healthData in
            completion(healthData)
        }
    }
}
