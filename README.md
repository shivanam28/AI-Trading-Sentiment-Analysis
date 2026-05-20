# AI Trading Sentiment Analysis

## Project Overview

Crypto markets are heavily influenced by human emotions like fear, greed, panic, and excitement.  
This project explores how market sentiment impacts trader behavior and profitability using:

-  Bitcoin Fear & Greed Index
-  Hyperliquid Historical Trading Data

The goal of this project is to understand:

- How traders perform under different market emotions
- Whether sentiment affects profitability
- How risk-taking behavior changes during fear and greed
- What hidden patterns can help build smarter trading strategies

---

# Objective

The objective of this analysis is to explore the relationship between:

- Market sentiment
- Trader profitability
- Trading behavior
- Position sizing
- Risk appetite

and uncover insights that can support better trading decisions.

---

#  Datasets Used

## 1 Bitcoin Fear & Greed Index Dataset

This dataset contains daily Bitcoin market sentiment classifications:

| Sentiment |
|---|
| Extreme Fear |
| Fear |
| Neutral |
| Greed |
| Extreme Greed |

This reflects overall crypto market psychology.

---

## 2️ Hyperliquid Historical Trader Dataset

This dataset contains real trading activity data including:

- Trader accounts
- Coins traded
- Trade sizes
- Buy/Sell actions
- Long/Short positions
- Closed Profit & Loss
- Fees
- Trading timestamps

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Streamlit

---

#  Data Preprocessing

The following preprocessing steps were performed:

 Loaded both datasets  
 Converted timestamps into datetime format  
 Extracted dates from trade timestamps  
 Merged trader data with sentiment data  
 Created profit/loss labels  
 Cleaned and filtered trading actions  

---

#  Exploratory Data Analysis

---

# 1️ Market Sentiment Distribution

This analysis shows how frequently each market sentiment appeared in the dataset.

## Insight

The market was largely dominated by Fear and Greed phases, showing that crypto trading environments are highly emotion-driven.

## Visualization

<img width="800" alt="Sentiment Distribution" src="https://github.com/shivanam28/AI-Trading-Sentiment-Analysis/blob/main/1.png">

---

# 2 Average Profitability by Sentiment

This analysis measures average trader profitability under different market sentiments.

##  Key Findings

- Extreme Greed produced the highest average profits
- Extreme Fear showed lower profitability
- Fear phases still generated decent profits due to high volatility

##  Insight

Bullish momentum strongly improves trader profitability, while volatile fear conditions may create opportunities for experienced traders.

##  Visualization

<img width="800" alt="Average PnL by Sentiment" src="https://github.com/shivanam28/AI-Trading-Sentiment-Analysis/blob/main/2.png">

---

# 3️ Trade Size Analysis

This analysis compares average trade sizes across different market conditions.

##  Key Findings

- Fear periods had the largest average trade sizes
- Extreme Greed showed smaller trade sizes despite higher profitability

##  Insight

Traders become more aggressive during volatile fear conditions, indicating elevated risk-taking behavior.

##  Visualization

<img width="800" alt="Trade Size Analysis" src="https://github.com/shivanam28/AI-Trading-Sentiment-Analysis/blob/main/3.png">

---

# 4️ Buy vs Sell Behavior Analysis

This analysis compares buying and selling activity during different sentiment phases.

##  Key Findings

- Greed periods encouraged stronger buying activity
- Fear periods increased selling pressure

## Insight

Trader decisions are heavily influenced by market psychology and emotional conditions.

##  Visualization

<img width="800" alt="Buy Sell Analysis" src="https://github.com/shivanam28/AI-Trading-Sentiment-Analysis/blob/main/4.png">

---

# 5️ Win Rate Analysis

This analysis calculates the percentage of profitable trades under each sentiment.

##  Key Findings

- Extreme Greed had the highest win rate
- Extreme Fear had the lowest win rate
- Overall win rates remained below 50%

##  Insight

Crypto trading remains highly volatile and risky even during favorable market conditions.

##  Visualization

<img width="800" alt="Win Rate Analysis" src="https://github.com/shivanam28/AI-Trading-Sentiment-Analysis/blob/main/5.png">

---

# 7️ Profit Distribution Analysis

This analysis uses boxplots to understand profit/loss variability across sentiments.

##  Key Findings

- Extreme market emotions created larger profit/loss fluctuations
- Emotional markets increase trading volatility

##  Insight

Extreme sentiment phases create both larger opportunities and larger risks.

##  Visualization

<img width="800" alt="Profit Distribution" src="https://github.com/shivanam28/AI-Trading-Sentiment-Analysis/blob/main/6.png">

---

# 8️ Correlation Heatmap

This analysis identifies relationships between numerical trading variables.

##  Key Findings

- Larger trades generated higher fee exposure
- Bigger positions increased profit/loss volatility

##  Insight

Aggressive trading strategies increase both reward potential and financial risk.

##  Visualization

<img width="800" alt="Correlation Heatmap" src="https://github.com/shivanam28/AI-Trading-Sentiment-Analysis/blob/main/7.png">

---

#  Hidden Patterns Discovered

## Pattern 1
Extreme Greed generated the highest profitability and win rates.

---

## Pattern 2
Fear conditions triggered the largest average trade sizes, showing aggressive risk-taking behavior during volatility.

---

## Pattern 3
Even the best-performing market conditions maintained win rates below 50%, highlighting the difficulty of crypto trading.

---

## Pattern 4
Fear markets occasionally outperformed normal Greed conditions, suggesting experienced traders exploit panic-driven volatility.

---

# Strategic Recommendations

### Momentum-Based Trading
Momentum strategies may perform better during Greed and Extreme Greed conditions.

---

### Strong Risk Management
Fear periods require stricter risk management because traders take larger positions during volatile conditions.

---

### Avoid Emotional Trading
Extreme Fear conditions often produce weaker performance and panic-driven decisions.

---

### Use Sentiment as a Trading Signal
Sentiment indicators can improve:
- market timing
- position sizing
- directional bias

---

### Combine Sentiment with Technical Analysis
Using sentiment together with technical indicators may improve trade quality and reduce unnecessary exposure.

---

# Final Conclusion

This project demonstrates a strong relationship between market sentiment and trader behavior.

The analysis revealed that:

- Bullish conditions significantly improve trader profitability
- Fear periods encourage aggressive risk-taking
- Trader psychology strongly influences market behavior
- Crypto trading remains highly volatile regardless of sentiment

The findings suggest that integrating sentiment analysis into trading strategies can help traders better understand market conditions, improve decision-making, and manage risk more effectively.

---

# Future Improvements

- Build machine learning models for trade prediction
- Perform leverage risk analysis
- Create real-time dashboards
- Develop sentiment-aware trading systems

---

# 👩‍💻 Author

**Shivani Singh**  
AI & Data Science Enthusiast  

Focused on:
- Artificial Intelligence
- Machine Learning
- Data Analytics

---
