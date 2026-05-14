package quantumdl;

/**
 * Anomaly Detection using Quantum Methods
 */
public class QuantumAnomalyDetector {
    
    private int numFeatures = 8;
    private double contamination = 0.1;
    private double threshold = 0.0;
    
    public QuantumAnomalyDetector() {
        System.out.println("Initializing Quantum Anomaly Detector...");
    }
    
    public double[][] prepareData(int nSamples) {
        int nNormal = (int)(nSamples * (1 - contamination));
        int nAnomaly = nSamples - nNormal;
        
        double[][] X = new double[nSamples][numFeatures];
        double[][] y = new double[nSamples][1];
        
        // Normal data (Gaussian)
        for (int i = 0; i < nNormal; i++) {
            for (int j = 0; j < numFeatures; j++) {
                X[i][j] = gaussianRandom();
            }
            y[i][0] = 0;
        }
        
        // Anomalies (displaced)
        for (int i = nNormal; i < nSamples; i++) {
            for (int j = 0; j < numFeatures; j++) {
                X[i][j] = gaussianRandom() + 3.0;
            }
            y[i][0] = 1;
        }
        
        // Shuffle
        shuffle(X, y);
        
        System.out.println("Generated " + nSamples + " samples (" + nAnomaly + " anomalies)");
        return X;
    }
    
    public void train(double[][] X, double[][] y, int epochs) {
        System.out.println("Training anomaly detector on " + X.length + " samples...");
    }
    
    public void fitThreshold(double[][] X, double percentile) {
        double[] scores = new double[X.length];
        for (int i = 0; i < X.length; i++) {
            scores[i] = anomalyScore(X[i]);
        }
        
        // Simple percentile
        java.util.Arrays.sort(scores);
        int idx = (int)(X.length * percentile / 100.0);
        threshold = scores[idx];
        
        System.out.println("Threshold: " + threshold);
    }
    
    public int[] detect(double[][] X) {
        int[] predictions = new int[X.length];
        for (int i = 0; i < X.length; i++) {
            predictions[i] = anomalyScore(X[i]) > threshold ? 1 : 0;
        }
        return predictions;
    }
    
    public double[][] evaluate(double[][] predictions, double[][] actual) {
        int tp = 0, tn = 0, fp = 0, fn = 0;
        
        for (int i = 0; i < predictions.length; i++) {
            int pred = predictions[i][0] > 0.5 ? 1 : 0;
            int act = (int) actual[i][0];
            
            if (pred == 1 && act == 1) tp++;
            if (pred == 0 && act == 0) tn++;
            if (pred == 1 && act == 0) fp++;
            if (pred == 0 && act == 1) fn++;
        }
        
        System.out.println("True Positives: " + tp);
        System.out.println("True Negatives: " + tn);
        System.out.println("False Positives: " + fp);
        System.out.println("False Negatives: " + fn);
        
        return predictions;
    }
    
    private double anomalyScore(double[] x) {
        // Simple anomaly score (distance from origin)
        double sum = 0;
        for (double v : x) sum += v * v;
        return Math.sqrt(sum);
    }
    
    private void shuffle(double[][] X, double[][] y) {
        java.util.Random rand = new java.util.Random(42);
        for (int i = X.length - 1; i > 0; i--) {
            int j = rand.nextInt(i + 1);
            double[] tempX = X[i];
            X[i] = X[j];
            X[j] = tempX;
            double tempY = y[i][0];
            y[i][0] = y[j][0];
            y[j][0] = tempY;
        }
    }
    
    private double gaussianRandom() {
        double u = Math.random();
        double v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    }
}
