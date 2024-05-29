import UIKit

class MachineLearningView: BaseView {
    // MARK: - Properties
    @IBOutlet weak var machineLearningLabel: UILabel!
    @IBOutlet weak var machineLearningChart: UIView!
    
    // MARK: - Lifecycle
    override func awakeFromNib() {
        super.awakeFromNib()
        setupUI()
    }
    
    // MARK: - Setup UI
    private func setupUI() {
        machineLearningLabel.text = "Machine Learning"
        machineLearningChart.layer.cornerRadius = 10
        machineLearningChart.layer.borderWidth = 1
        machineLearningChart.layer.borderColor = UIColor.gray.cgColor
    }
    
    // MARK: - Bindings
    func bind(to viewModel: MachineLearningViewModel) {
        machineLearningLabel.text = viewModel.machineLearningString
    }
}
