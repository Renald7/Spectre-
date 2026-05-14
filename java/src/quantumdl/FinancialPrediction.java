package quantumdl;

/**
 * Financial Prediction Use Case
 * Stock Price Prediction using Quantum Deep Learning
 */
public class FinancialPrediction {
    
    private int lookbackDays = 30;
    private int predictionHorizon = 1;
    private int numFeatures = 10;
    
    public FinancialPrediction() {
        System.out.println("Initializing Financial Prediction...");
    }
    
    public double[][] prepareData(int nSamples) {
        // Generate synthetic stock data
        double[][] X = new double[nSamples][numFeatures];
        double[][] y = new double[nSamples][1];
        
        double[] prices = new double[nSamples + lookbackDays + predictionHorizon];
        prices[0] = 100.0; // initial price
        
        // Generate price series
        for (int i = 1; i < prices.length; i++) {
            double change = (Math.random() - 0.5) * 0.04;
            prices[i] = prices[i-1] * (1 + change);
        }
        
        // Generate features
        int count = 0;
        for (int i = 0; i < prices.length - lookbackDays - predictionHorizon; i++) {
            if (count >= nSamples) break;
            
            // Simple features
            double meanReturn = 0;
            double volatility = 0;
            
            for (int j = i; j < i + lookbackDays - 1; j++) {
                double ret = Math.log(prices[j+1] / prices[j] + 1e-10);
                meanReturn += ret;
            }
            meanReturn /= lookbackDays;
            
            for (int j = i; j < i + lookbackDays - 1; j++) {
                double ret = Math.log(prices[j+1] / prices[j] + 1e-10);
                volatility += Math.pow(ret - meanReturn, 2);
            }
            volatility = Math.sqrt(volatility / lookbackDays);
            
            // Fill features
            X[count][0] = meanReturn;
            X[count][1] = volatility;
            X[count][2] = prices[i + lookbackDays] / mean(prices, i, i+lookbackDays) - 1;
            X[count][3] = meanReturn * 0.5; // downside risk proxy
            X[count][4] = meanReturn * 1.5; // upside potential
            X[count][5] = Math.random();
            X[count][6] = Math.random();
            X[count][7] = Math.random();
            X[count][8] = Math.random();
            X[count][9] = Math.random();
            
            // Target
            y[count][0] = prices[i + lookbackDays + predictionHorizon] / 
                          prices[i + lookbackDays] - 1;
            count++;
        }
        
        System.out.println("Generated " + nSamples + " samples with " + numFeatures + " features");
        return X;
    }
    
    public void train(double[][] X, double[][] y, int epochs) {
        System.out.println("Training on " + X.length + " samples for " + epochs + " epochs...");
        System.out.println("(Simplified - no actual quantum computation in Java demo)");
    }
    
    public double[][] predict(double[][] X) {
        double[][] predictions = new double[X.length][1];
        for (int i = 0; i < X.length; i++) {
            // Simple prediction based on feature 0
            predictions[i][0] = X[i][0] * 0.5 + Math.random() * 0.1;
        }
        return predictions;
    }
    
    public double[][] evaluate(double[][] predictions, double[][] actual) {
        double mse = 0;
        double mae = 0;
        int correct = 0;
        
        for (int i = 0; i < predictions.length; i++) {
            double diff = predictions[i][0] - actual[i][0];
            mse += diff * diff;
            mae += Math.abs(diff);
            
            // Direction accuracy
            if ((predictions[i][0] > 0) == (actual[i][0] > 0)) {
                correct++;
            }
        }
        
        mse /= predictions.length;
        mae /= predictions.length;
        double dirAcc = (double) correct / predictions.length;
        
        System.out.println("MSE: " + mse);
        System.out.println("MAE: " + mae);
        System.out.println("Direction Accuracy: " + (dirAcc * 100) + "%");
        
        return predictions;
    }
    
    private double mean(double[] arr, int start, int end) {
        double sum = 0;
        for (int i = start; i < end; i++) sum += arr[i];
        return sum / (end - start);
    }
}
