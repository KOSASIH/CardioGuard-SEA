import Foundation

struct MachineLearning {
    let id: Int
    let model: String
    let accuracy: Double
    
    init(id: Int, model: String, accuracy: Double) {
        self.id = id
        self.model = model
        self.accuracy = accuracy
    }
}
