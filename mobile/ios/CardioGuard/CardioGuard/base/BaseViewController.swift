import UIKit

class BaseViewController<View: BaseView, ViewModel: BaseViewModel>: UIViewController {
    // MARK: - Properties
    var viewModel: ViewModel?
    
    // MARK: - Lifecycle
    override func loadView() {
        super.loadView()
        view = View()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        viewModel?.bind(to: view)
    }
}
