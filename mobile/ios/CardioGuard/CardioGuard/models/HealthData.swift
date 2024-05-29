import Foundation

struct HealthData {
    let id: Int
    let date: Date
    let value: Double
    
    init(id: Int, date: Date, value: Double) {
        self.id = id
        self.date = date
        self.value = value
    }
}
