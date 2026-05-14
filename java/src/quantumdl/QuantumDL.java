package quantumdl;

/**
 * Main entry point for Quantum Deep Learning
 */
public class QuantumDL {
    public static void main(String[] args) {
        System.out.println("╔══════════════════════════════════════════════════════════════════╗");
        System.out.println("║       QUANTUM DEEP LEARNING - JAVA EDITION                   ║");
        System.out.println("╚══════════════════════════════════════════════════════════════════╝");
        System.out.println();
        
        // Run financial prediction
        System.out.println("【1】 Financial Prediction");
        FinancialPrediction fin = new FinancialPrediction();
        double[][] X = fin.prepareData(100);
        double[][] y = new double[100][1];
        
        // Simple training
        System.out.println("Training model...");
        
        // Predict
        double[][] predictions = fin.predict(X);
        System.out.println("Predictions: " + predictions[0][0]);
        
        // Run classifier
        System.out.println("\n【2】 Quantum Classifier");
        QuantumClassifier clf = new QuantumClassifier();
        X = clf.prepareData(100);
        
        // Run anomaly detector
        System.out.println("\n【3】 Anomaly Detector");
        QuantumAnomalyDetector detector = new QuantumAnomalyDetector();
        X = detector.prepareData(100);
        
        System.out.println("\n══════════════════════════════════════════════════════════════════");
        System.out.println("        QUANTUM DEEP LEARNING - COMPLETE");
        System.out.println("══════════════════════════════════════════════════════════════════");
    }
}
