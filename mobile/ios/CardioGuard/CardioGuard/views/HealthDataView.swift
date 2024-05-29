import UIKit

class HealthDataView: BaseView {
    // MARK: - Properties
    @IBOutlet weak var healthDataLabel: UILabel!
    @IBOutlet weak var healthDataChart: UIView!
    
    // MARK: - Lifecycle
    override func awakeFromNib() {
        super.awakeFromNib()
        setupUI()
    }
    
    // MARK: - Setup UI
    private func setupUI() {
        healthDataLabel.text = "Health Data"
        healthDataChart.layer.cornerRadius = 10
        healthDataChart.layer.borderWidth = 1
        healthDataChart.layer.borderColor = UIColor.gray.cgColor
    }
    
    // MARK: - Bindings
    func bind(to viewModel: HealthDataViewModel) {
        healthDataLabel.text = viewModel.healthDataString
    }
}
