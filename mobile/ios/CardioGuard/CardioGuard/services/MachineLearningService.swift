import Foundation

class MachineLearningService {
    // MARK: - Properties
    private let machineLearningRepository: MachineLearningRepository
    
    // MARK: - Lifecycle
    init(machineLearningRepository: MachineLearningRepository) {
        self.machineLearningRepository = machineLearningRepository
    }
    
    // MARK: - Functions
    func trainMachineLearningModel(completion: (MachineLearning) -> Void) {
        machineLearningRepository.trainMachineLearningModel { machineLearning in
            completion(machineLearning)
        }
    }
}
