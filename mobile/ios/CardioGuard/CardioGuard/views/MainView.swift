import UIKit

class MainView: BaseView {
    // MARK: - Properties
    @IBOutlet weak var healthDataButton: UIButton!
    @IBOutlet weak var machineLearningButton: UIButton!
    
    // MARK: - Lifecycle
    override func awakeFromNib() {
        super.awakeFromNib()
        setupUI()
    }
    
    // MARK: - Setup UI
    private func setupUI() {
        healthDataButton.setTitle("Health Data", for:.normal)
        machineLearningButton.setTitle("Machine Learning", for:.normal)
    }
    
    // MARK: - Actions
    @IBAction func healthDataButtonTapped(_ sender: UIButton) {
        // Navigate to Health Data screen
    }
    
    @IBAction func machineLearningButtonTapped(_ sender: UIButton) {
        // Navigate to Machine Learning screen
    }
}
