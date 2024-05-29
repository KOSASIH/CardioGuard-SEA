import UIKit

protocol BaseView: UIView {
    associatedtype ViewModel
    
    func bind(to viewModel: ViewModel)
}
