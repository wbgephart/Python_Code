# NBA Spread Betting Predictor

A machine learning model that predicts which team will cover the spread in NBA games, achieving 74.6% accuracy on test data.

## 📊 Performance

- **Test Accuracy:** 74.6%
- **Training Samples:** 6,344 games (2020-2026 seasons)
- **Features:** 37 advanced basketball metrics
- **Model:** XGBoost Classifier
- **Target:** Spread coverage (not win/loss)

## 🎯 What It Predicts

This model predicts **spread coverage**, not game winners:
- ✅ **Home Covers:** Home team beats the spread
- ❌ **Home Loses ATS:** Home team fails to cover

**Example:**
- Lakers vs Jazz, spread: Jazz +7.5
- If model predicts "Home Loses ATS" → Bet **Lakers -7.5**
- If model predicts "Home Covers" → Bet **Jazz +7.5**

## 🚀 Quick Start

### Prerequisites

```bash
pip install nba_api pandas numpy scikit-learn xgboost requests
```

### Google Colab Setup

1. Open the notebook in Google Colab
2. Mount your Google Drive
3. Add your The Odds API key
4. Run all cells

### API Setup

Get a free API key from [The Odds API](https://the-odds-api.com/):
- Free tier: 500 requests/month
- Sufficient for daily NBA predictions

Add your key to the notebook:
```python
API_KEY = 'your_api_key_here'
```

## 📋 Workflow

### Step 1: Environment Setup
- Mounts Google Drive
- Creates project folder: `nba_spread_model/`
- Installs required packages

### Step 2: Download NBA Games
- Fetches games from 2020-present using NBA API
- Downloads multiple seasons at once
- ~2 minutes for all seasons

### Step 3: Download Team Stats
- Gets offensive and defensive ratings
- Fetches pace statistics
- Advanced metrics (True Shooting %, etc.)
- ~30 seconds

### Step 4: Download Spread Odds
- Fetches historical spreads from The Odds API
- DraftKings as primary bookmaker
- ~10 minutes for full history

### Step 5: Match & Merge
- Matches games to spreads
- Merges team statistics
- Creates training dataset
- ~2 minutes

### Step 6: Train Model
- XGBoost classifier
- 37 features
- 80/20 train/test split
- ~1 minute

### Step 7: Predict Today's Games
- Fetches today's spreads
- Generates predictions
- Shows confidence levels
- Filters by 60%+ confidence

**Total Runtime:** ~15 minutes

## 🎯 Features Used

### Core Features (37 total)
1. **Spread Data:**
   - Home spread
   - Expected margin (based on ratings)
   - Spread advantage

2. **Offensive Stats:**
   - Points per game
   - Field goal %
   - 3-point %
   - Free throw %
   - Offensive rating
   - True shooting %

3. **Defensive Stats:**
   - Points allowed
   - Defensive rating
   - Opponent FG%

4. **Pace & Style:**
   - Pace (possessions per game)
   - Rebounds
   - Assists
   - Turnovers

5. **Differentials:**
   - Scoring differential
   - Shooting differential
   - Defense differential
   - Pace differential

## 📊 Model Performance

### Test Set Results
```
Accuracy: 74.6%

Classification Report:
                  precision    recall  f1-score   support
HOME LOSES ATS       0.72      0.67      0.69       543
HOME COVERS          0.77      0.80      0.78       726

accuracy                                 0.75      1269
```

### Top Features (by importance)
1. **home_spread** (45.93%) - Most important!
2. **scoring_diff** (4.09%)
3. **expected_margin** (3.85%)
4. **defense_diff** (3.84%)
5. **shooting_diff** (3.79%)

## 🎮 Sample Output

```
====================================================================================================
TODAY'S PREDICTIONS
====================================================================================================

Houston Rockets @ New Orleans Pelicans
Spread: New Orleans Pelicans +9.5
  Expected margin: -5.6
  Spread advantage: -15.1
  HOME COVER: 2.5% | AWAY COVER: 97.5%
  ✅ PICK: Houston Rockets -9.5

Los Angeles Clippers @ Oklahoma City Thunder
Spread: Oklahoma City Thunder -17.5
  Expected margin: +23.8
  Spread advantage: +41.3
  HOME COVER: 99.9% | AWAY COVER: 0.1%
  ✅ PICK: Oklahoma City Thunder -17.5

Golden State Warriors @ Phoenix Suns
Spread: Phoenix Suns +1.5
  Expected margin: -14.8
  Spread advantage: -16.3
  HOME COVER: 46.8% | AWAY COVER: 53.2%
  ⏸️  PASS (confidence too low)
```

## 🎯 Prediction Confidence Levels

- **90%+ confidence:** Very strong pick (bet larger)
- **75-90% confidence:** Strong pick (standard bet)
- **60-75% confidence:** Moderate pick (smaller bet)
- **< 60% confidence:** PASS (model skips these)

## 📂 File Structure

```
NBA_Predictor.ipynb          # Main Jupyter notebook (Google Colab)
```

### Google Drive Output
```
MyDrive/nba_spread_model/
├── nba_games.csv           # All NBA games (2020-present)
├── team_stats.csv          # Team statistics
├── spread_odds.csv         # Historical spreads
├── training_data.csv       # Merged dataset
├── model.pkl               # Trained XGBoost model
└── scaler.pkl              # Feature scaler
```

## ⚙️ Configuration

### Training Parameters

```python
MIN_GAMES = 5                # Minimum games for team to be included
START_DATE = '2020-10-01'    # Start of data collection
ODDS_SPORT_KEY = 'basketball_nba'
```

### Confidence Threshold

To adjust minimum confidence for predictions, modify:
```python
# In make_predictions() function
confidence_threshold = 0.60  # Default: 60%
```

### Seasons to Include

```python
# Automatically downloads 2020-present
# To change, modify download_all_nba_games() function
for year in range(2020, current_season_start + 1):
    seasons.append(f"{year}-{str(year+1)[-2:]}")
```

## 🔧 Troubleshooting

### "NBA API timeout"
- Increase timeout in `LeagueGameLog(timeout=180)`
- Wait 30 seconds between retries
- NBA API can be slow during peak hours

### "No spread odds found"
- Verify The Odds API key is valid
- Check if games are scheduled for today
- Free tier limit: 500 requests/month

### "Model accuracy dropped"
- Retrain with fresh data (Run Step 2-6)
- Check if team rosters changed significantly
- Injuries can affect predictions (not in model)

### "Google Drive not mounted"
- Run first cell to mount Drive
- Allow permissions when prompted
- Check Drive folder exists

## 📊 Why Spreads Instead of Winners?

Predicting **game winners** is easy but not profitable:
- Model accuracy: ~70%
- But favorites are often -500 odds or worse
- No edge even with high accuracy

Predicting **spread coverage** is more valuable:
- Spreads are usually -110 on both sides
- 74% accuracy at -110 odds = significant edge
- ~55% win rate needed to break even
- We're at 74.6%!

## 🎲 Betting Strategy

### Recommended Approach

1. **High Confidence (90%+):** 
   - Bet 2-3% of bankroll
   - These are rare but very valuable

2. **Strong (75-90%):**
   - Bet 1-2% of bankroll
   - Most picks fall here

3. **Moderate (60-75%):**
   - Bet 0.5-1% of bankroll
   - Lower confidence

4. **Low (< 60%):**
   - Don't bet
   - Model automatically skips these

### Kelly Criterion

For optimal bet sizing, use Kelly Criterion:
```
Kelly % = (bp - q) / b

Where:
- b = decimal odds - 1 (for -110, b = 0.909)
- p = model probability
- q = 1 - p
```

**Example:**
- Model: 97.5% confidence
- Odds: -110
- Kelly = (0.909 × 0.975 - 0.025) / 0.909 = 95%
- Fractional Kelly (25%): 23.8% of bankroll

## 📈 Performance Tracking

Recommended spreadsheet columns:
- Date
- Game
- Pick
- Spread
- Confidence
- Bet Amount
- Outcome (W/L/P)
- Profit/Loss

Track separately by confidence level to see which ranges are most profitable.

## 🔄 Daily Workflow

### Morning (Before Games)
```python
# Run the entire notebook (~15 min)
# Output will show:
# - Today's games with spreads
# - Model predictions
# - Confidence levels
# - Filtered picks (60%+ confidence)
```

### After Games
- Record results
- Update spreadsheet
- Track accuracy by confidence level

### Weekly
- Retrain model with latest games
- Check if accuracy is stable
- Adjust confidence thresholds if needed

## 🎯 Advanced Features

### Feature Engineering

The model uses several calculated features:

**Expected Margin:**
```python
expected_margin = (home_off_rating - away_off_rating) + 
                  (away_def_rating - home_def_rating)
```

**Spread Advantage:**
```python
spread_advantage = expected_margin - spread
```

If spread_advantage > 0 → Home team has edge
If spread_advantage < 0 → Away team has edge

### Model Architecture

```python
XGBClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    min_child_weight=3,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
```

Optimized for:
- Preventing overfitting (max_depth=6)
- Stable predictions (subsample=0.8)
- Feature diversity (colsample_bytree=0.8)

## ⚠️ Important Limitations

1. **No Injury Data:** Model doesn't know if star players are out
2. **No Back-to-Backs:** Doesn't track rest days
3. **No Lineup Changes:** Trade deadline changes not immediate
4. **Regular Season Only:** Don't use for playoffs
5. **Requires Recent Stats:** Teams need 5+ games for accurate predictions

### When NOT to Bet

- **Trade deadline day** (rosters changing)
- **Start of season** (teams need 5+ games)
- **Known major injuries** (check injury reports manually)
- **Playoffs** (model trained on regular season)
- **Back-to-back games** (fatigue not in model)

## 🤝 Data Sources

- **NBA Games & Stats:** [NBA API](https://github.com/swar/nba_api)
- **Spread Odds:** [The Odds API](https://the-odds-api.com/)
- **Historical Data:** 2020-2026 NBA seasons

## 📄 License

MIT License - Use at your own risk. No guarantees on profitability.

## ⚖️ Disclaimer

**This software is for educational purposes only.**

- Sports betting involves risk of loss
- Past performance does not guarantee future results
- Always gamble responsibly
- Only bet what you can afford to lose
- 74.6% test accuracy does not guarantee 74.6% real-world accuracy
- Check for injuries and lineup changes before betting
- Model performance may vary over time as NBA evolves

## 🙏 Credits

- NBA statistics: [nba_api](https://github.com/swar/nba_api) by Swar Patel
- Odds data: [The Odds API](https://the-odds-api.com/)
- Machine learning: XGBoost, scikit-learn
- Platform: Google Colab

## 🔬 Technical Notes

### Why XGBoost?

- **Better than Random Forest:** Handles feature interactions
- **Better than Neural Networks:** Less data needed, more interpretable
- **Built-in regularization:** Prevents overfitting
- **Feature importance:** Can see what matters most

### Why 74.6% Accuracy?

This is **very good** for spread prediction:
- Professional bettors aim for 55-60%
- 52.4% breaks even at -110 odds
- 74.6% provides substantial edge
- Even 60% win rate is profitable long-term

### Data Quality

- **6,344 training samples** (sufficient for 37 features)
- **Multiple seasons** (2020-2026) captures different NBA eras
- **Regular season only** (consistent game dynamics)
- **5+ game minimum** (ensures stable statistics)

## 📚 Further Reading

- [The Odds API Documentation](https://the-odds-api.com/liveapi/guides/v4/)
- [NBA API Documentation](https://github.com/swar/nba_api)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Understanding NBA Advanced Stats](https://www.nba.com/stats/help/glossary)

## 🆘 Support

If you encounter issues:
1. Check API keys are valid
2. Ensure Google Drive is mounted
3. Verify internet connection
4. Check The Odds API usage limits
5. Try increasing timeout values for NBA API

For questions about the model or betting strategy, review the disclaimer above - this is educational software with no guarantees of profitability.
