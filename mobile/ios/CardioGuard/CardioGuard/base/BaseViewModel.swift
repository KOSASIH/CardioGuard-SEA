import Foundation

protocol BaseViewModel {
    associatedtype View: BaseView
    
    func bind(to view: View)
}
