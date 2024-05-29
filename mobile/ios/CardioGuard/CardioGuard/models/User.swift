import Foundation

struct User {
    let id: Int
    let name: String
    let email: String
    
    init(id: Int, name: String, email: String) {
        self.id = id
        self.name = name
        self.email = email
    }
}
