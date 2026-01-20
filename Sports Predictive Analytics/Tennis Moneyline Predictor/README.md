# Tennis Betting Predictor (ATP/WTA)

A machine learning-based tennis betting predictor that analyzes ATP and WTA matches to identify value betting opportunities on Bet365.

## 📊 Performance

- **Win Rate:** 53% (17-15 on non-Grand Slam tournaments)
- **ROI:** Positive
- **Training Data:** 11,700+ ATP matches, 10,700+ WTA matches (2021-2026)
- **Model Accuracy:** ~63% on test data

## 🚀 Quick Start

### Prerequisites

```bash
pip install pandas requests scikit-learn fuzzywuzzy openpyxl
```

### API Setup

1. Get an API key from [API-Tennis.com](https://api.api-tennis.com/)
2. Add your API key to each step file where it says `YOUR_API_KEY_HERE`

### Daily Workflow

```bash
# Step 1: Fetch today's and tomorrow's matches
python step1_fetch_matches.py

# Step 2: Skip (API odds are unreliable)
# We manually enter Bet365 odds instead

# Step 3: Load historical data and match player names
python step3_load_and_match.py

# Step 4: Train prediction models
python step4_train_models.py

# Step 5: Manual odds entry and predictions
python manual_odds_entry.py
```

## 📋 How It Works

### Step 1: Fetch Matches
- Fetches ATP/WTA singles matches from API-Tennis.com
- Filters out Grand Slams, Challengers, ITF events
- Includes matches from today and tomorrow (24-48 hour window)
- Excludes finished/cancelled matches

### Step 2: (Skipped)
Originally checked API odds, but API-Tennis.com Bet365 odds were found to be inaccurate.

### Step 3: Load Historical Data
- Downloads historical match data from [Jeff Sackmann's GitHub](https://github.com/JeffSackmann/tennis_atp)
- Matches current players to historical records using fuzzy matching
- Balances dataset by randomly swapping player positions

### Step 4: Train Models
- Trains separate models for ATP and WTA
- Uses Gradient Boosting Classifier
- Features: Player ranks, rank difference, surface type (Clay/Grass/Hard)
- 80/20 train/test split

### Step 5: Manual Odds Entry
- Interactive interface to enter Bet365 odds from your app
- Calculates model win probability vs implied probability
- Uses Kelly Criterion (25% fractional) for bet sizing
- Bankroll: $1000
- Recommends bets with 5%+ edge

## 🎯 Features

### Filtering
- **Grand Slams:** Automatically excluded (poor performance on slams)
- **Challengers/ITF:** Excluded (lower quality data)
- **Status:** Only upcoming matches (no finished/cancelled)

### Player Matching
- Fuzzy matching to handle abbreviated names (e.g., "A. Tabilo" → "Alejandro Tabilo")
- 70% similarity threshold
- Last name prioritization

### Bet Sizing
- Kelly Criterion (25% fractional Kelly)
- Conservative approach to protect bankroll
- Scales with edge size

### Output Format
```
📊 FOR YOUR SPREADSHEET:
Match #: 3
Player 1: A. Tabilo
Player 2: C. Ugo Carabelli
Tournament: ATP Hong Kong
Player 1 Odds: -225
Player 2 Odds: +175
Suggested Bet: $124.50
Potential Profit: $55.33
Bet On: Player 1 (A. Tabilo)
```

## 📂 File Structure

```
step1_fetch_matches.py       # Fetch upcoming matches from API
step2_check_odds.py          # (Deprecated - API odds unreliable)
step3_load_and_match.py      # Load historical data and match players
step4_train_models.py        # Train ML models
manual_odds_entry.py         # Interactive betting interface
check_statuses.py            # Diagnostic tool for match statuses
```

## ⚙️ Configuration

### Bankroll
Default: $1000

To change, edit `manual_odds_entry.py`:
```python
bankroll = 1000  # Change this value
```

### Kelly Fraction
Default: 25% (conservative)

To change, edit `manual_odds_entry.py`:
```python
fractional_kelly = 0.25  # Change this value (0.15-0.30 recommended)
```

### Tournament Filters
To modify which tournaments are included, edit `step1_fetch_matches.py`:
```python
# Add/remove from Grand Slam filter
grand_slam_keywords = ['australian open', 'french open', ...]

# Modify tour filters
if any(tour in event_type for tour in ['atp singles', 'wta singles']):
```

## 🔧 Troubleshooting

### "No matches found"
- Check if there are ATP/WTA tournaments happening today/tomorrow
- Verify API key is valid
- Grand Slams are filtered out (by design)

### "Player not matched"
- New/young players may not be in historical data
- Check fuzzy matching threshold in `step3_load_and_match.py`
- These matches will be skipped (safe default)

### "Low match count"
- Many tournaments have finished for the day
- Try again in the morning (matches reset)
- Check `check_statuses.py` to see match statuses

## 📊 Model Details

### Features (6 total)
- Player 1 rank
- Player 2 rank
- Rank difference
- Surface: Clay (0/1)
- Surface: Grass (0/1)
- Surface: Hard (0/1)

### Algorithm
- Gradient Boosting Classifier
- 200 estimators
- Learning rate: 0.05
- Max depth: 4
- Random state: 42 (reproducible)

### Why These Features?
After extensive testing, simple rank-based features outperformed complex features like:
- Win percentages
- Head-to-head records
- Recent form
- Surface-specific stats

Simpler is better for this problem.

## ⚠️ Important Notes

1. **Grand Slams Excluded:** System performed poorly (25% win rate) on Grand Slams, so they're automatically filtered out
2. **Manual Odds Entry:** API-Tennis.com Bet365 odds were inaccurate, so we manually enter from Bet365 app
3. **Regular Tournaments Only:** ATP 250/500/Masters and WTA tournaments only
4. **Edge Requirement:** Only recommends bets with 5%+ edge
5. **Kelly Criterion:** Uses fractional Kelly (25%) for safety

## 📈 Performance Tracking

Recommended spreadsheet columns:
- Date
- Player 1
- Player 2
- Competition
- Player 1 Odds
- Player 2 Odds
- Bet (amount)
- Potential Buyout
- Outcome (W/L)
- Earnings

Formula for Earnings column:
```
=IF(Outcome="W", Potential_Buyout, IF(Outcome="L", -Bet, ""))
```

## 🤝 Contributing

This is a personal betting system. Use at your own risk.

## 📄 License

MIT License - Use at your own risk. No guarantees on profitability.

## 🙏 Credits

- Historical data: [Jeff Sackmann's Tennis Databases](https://github.com/JeffSackmann/tennis_atp)
- Match data: [API-Tennis.com](https://api.api-tennis.com/)
- Odds: Bet365

## ⚖️ Disclaimer

**This software is for educational purposes only.** 

- Gambling involves risk of loss
- Past performance does not guarantee future results
- Always gamble responsibly
- Only bet what you can afford to lose
- This system has a 53% win rate on regular tournaments - variance is expected
- The model can be wrong, especially on individual matches
