# Conclusion & Summary Results: Airline Passenger Analytics

## 1. Project Overview
This project successfully analyzed 129,880 passenger records to identify the primary drivers of satisfaction and build a predictive model for business intelligence.

## 2. Model Performance Summary
We evaluated three models to predict passenger satisfaction. The tree-based models significantly outperformed the linear baseline.

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Logistic Regression** | 87.8% | 87.2% | 84.2% | 85.7% |
| **Decision Tree** | 94.9% | 94.0% | 94.2% | 94.1% |
| **Random Forest** | **94.7%** | **94.7%** | **92.9%** | **93.8%** |

**Note**: While Decision Tree had a slightly higher accuracy, **Random Forest** is recommended for production due to its better generalization and robust feature importance insights.

## 3. Top Factors Affecting Satisfaction
Based on Feature Importance analysis, the following service aspects are the most critical:

1. **Online Boarding (20.4%)**: The digital gateway to the flight.
2. **In-flight Wifi Service (15.8%)**: Connectivity is the highest-rated amenity.
3. **Class (13.1%)**: Business class passengers are fundamentally more satisfied.
4. **Type of Travel (10.9%)**: Business travelers have different satisfaction patterns than personal travelers.
5. **In-flight Entertainment (6.6%)**: Content quality is a major differentiator.

## 4. Operational Insights
- **Delays vs. Service**: Departure and Arrival delays combined represent **less than 1%** of the model's decision-making weight. This indicates that while delays are inconvenient, they are *not* the primary reason for dissatisfaction if the service quality remains high.
- **Customer Segmentation**: K-Means clustering identified 3 distinct passenger segments:
    - **Segment 0 (Digital Enthusiasts)**: High ratings for online services, highly satisfied.
    - **Segment 1 (Premium Comfort)**: Focus on seat comfort and legroom, mostly business class.
    - **Segment 2 (Service Sensitive)**: Mixed ratings, often dissatisfied if on-board service or cleanliness is low.

## 5. Final Conclusion
The airline should shift its primary focus from "Delay Reduction" to **"Service Excellence"**, specifically targeting the **Online Boarding** and **Wifi** experiences. Investing in these digital touchpoints will yield a significantly higher satisfaction ROI than operational tweaks to reduce minor delays.
