from Customer_Churn_Prediction.config.configuration import ConfigurationManager
from Customer_Churn_Prediction.components.Model_evaluation import ModelEvaluation
from Customer_Churn_Prediction import logger


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    try:

        # Load configuration
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        
        # Initialize ModelEvaluation
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        
        # Evaluate model
        cls_report, conf_matrix, accuracy = model_evaluation.eval_metrics()
        
        print("Classification Report:\n", cls_report)
        print("Confusion Matrix:\n", conf_matrix)
        print("Accuracy Score:", accuracy)

        # Save results
        model_evaluation.save_results()

        # Log results into MLflow
        #model_evaluation.log_into_mlflow()

    except Exception as e:
        print(f"An error occurred: {e}")
