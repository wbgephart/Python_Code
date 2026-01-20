# Grand Slam Tennis Predictor (Inverse Model)

An experimental inverse betting system specifically for Grand Slam tournaments. This system identifies what a standard ML model predicts, then recommends the **opposite** bet.

## 📊 Performance

- **Inverse Win Rate:** 78.4% (29-8 over 37 bets)
- **Regular Model Win Rate:** 21.4% (6-28 over 34 bets)
- **Profit (Inverse):** +$1,868 on flat $50 bets
- **Loss (Regular):** -$980 following model directly
- **Status:** ⚠️ EXPERIMENTAL - Continue tracking before large bets

## 🎯 Why Inverse?

Standard ML models trained on all tennis matches perform poorly on Grand Slams (21% win rate). However, when the model is **consistently wrong in a predictable direction**, we can exploit this by betting the opposite.

**Key Discovery:** The model's predictions are inverted for Grand Slams, making the inverse strategy highly profitable.

## 🚀 Quick Start

### Prerequisites

```bash
pip install pandas requests scikit-learn fuzzywuzzy openpyxl
```

### API Setup

1. Get an API key from [API-Tennis.com](https://api.api-tennis.com/)
2. Add your API key to each step file where it says `YOUR_API_KEY_HERE`

### Daily Workflow (During Grand Slams)

```bash
# Step 1: Fetch Grand Slam matches only
python grand_slam_step1_fetch_matches.py

# Step 2: Load historical GRAND SLAM data and match players
python grand_slam_step2_load_and_match.py

# Step 3: Train models on Grand Slam data only
python grand_slam_step3_train_models.py

# Step 4: Inverse predictor (automatically inverts recommendations)
python grand_slam_inverse_predictor.py
```

## 📋 How It Works

### Step 1: Fetch Grand Slam Matches
- **ONLY** fetches Grand Slam matches (Australian Open, French Open, Wimbledon, US Open)
- Filters out all other tournaments
- Includes today and tomorrow's matches
- Excludes finished/cancelled matches

### Step 2: Load Historical Grand Slam Data
- Downloads historical match data from [Jeff Sackmann's GitHub](https://github.com/JeffSackmann/tennis_atp)
- **Filters to Grand Slam matches ONLY** (this is the key difference)
- Matches current players to historical records
- Training set: ~2,400 ATP Grand Slam matches, ~2,400 WTA Grand Slam matches

### Step 3: Train Grand Slam Models
- Trains separate models for ATP and WTA
- Uses **only Grand Slam historical data** for training
- Same features as regular model (ranks + surface)
- Same algorithm (Gradient Boosting)

### Step 4: Inverse Predictor
- Runs the model to get predictions
- **Automatically inverts the recommendation**
- Shows you the opposite bet as if it's the model's recommendation
- Uses conservative Kelly (20% instead of 25%)
- Bankroll: $1000

## ⚡ The Inversion Process

Behind the scenes, the inverse predictor:

1. **Calculates model probabilities** (e.g., Player 1: 75%, Player 2: 25%)
2. **Inverts them** (e.g., Player 1: 25%, Player 2: 75%)
3. **Shows inverted probabilities as "model predictions"**
4. **Recommends bet based on inverted edge**

**You see clean output, but the bet is automatically flipped!**

## 📊 Historical Results

### Regular Model (Following Predictions)
```
Wins: 6
Losses: 28
Win Rate: 21.4%
Profit/Loss: -$980.43
```

### Inverse Strategy (Betting Opposite)
```
Wins: 29
Losses: 8
Win Rate: 78.4%
Profit/Loss: +$1,868.64 (on flat $50 bets)
ROI: 101%
```

## 🎯 Output Format

The output looks identical to the regular predictor, but recommendations are inverted:

```
📊 FOR YOUR SPREADSHEET:
Match #: 1
Player 1: D. Prizmic
Player 2: A. Fery
Tournament: ATP Australian Open
Player 1 Odds: -188
Player 2 Odds: +137
Suggested Bet: $95.42
Potential Profit: $130.73
Bet On: Player 2 (A. Fery)
```

**Behind the scenes:** Model predicted Player 1, so system recommends Player 2.

## 📂 File Structure

```
grand_slam_step1_fetch_matches.py       # Fetch Grand Slam matches only
grand_slam_step2_load_and_match.py      # Load Grand Slam historical data
grand_slam_step3_train_models.py        # Train on Grand Slam data
grand_slam_inverse_predictor.py         # Interactive inverse betting
```

## ⚙️ Configuration

### Bankroll
Default: $1000

To change, edit `grand_slam_inverse_predictor.py`:
```python
bankroll = 1000  # Change this value
```

### Kelly Fraction
Default: 20% (more conservative than regular 25%)

To change, edit `grand_slam_inverse_predictor.py`:
```python
fractional_kelly = 0.20  # Change this value
```

### Grand Slam Detection
To modify which tournaments are considered Grand Slams, edit `grand_slam_step1_fetch_matches.py`:
```python
grand_slam_keywords = ['australian open', 'french open', 'roland garros', 
                       'wimbledon', 'us open', 'grand slam']
```

## 🔧 Troubleshooting

### "No Grand Slam matches found"
- Check if a Grand Slam is currently happening
- Grand Slams occur 4 times per year:
  - Australian Open (January)
  - French Open (May-June)
  - Wimbledon (June-July)
  - US Open (August-September)

### "Low match count"
- Many Grand Slam matches finish early in the day
- Qualifying rounds have fewer matches
- Main draw starts after qualifiers complete

### "Player not matched"
- Qualifiers often include unknown/new players
- These are automatically skipped
- Focus on main draw matches for best results

## 📈 Why Does This Work?

### Theory
1. **Best-of-5 vs Best-of-3:** Men's Grand Slams use best-of-5 format, which the model doesn't account for
2. **Pressure & Experience:** Grand Slams have unique psychological factors
3. **Upset Tendency:** Round 1-2 of slams have more upsets than regular tournaments
4. **Model Miscalibration:** Model trained on regular tournaments applies wrong priors to slams

### Evidence
- 37 bets tracked
- Consistent 78.4% win rate
- Model consistently wrong (21.4% accuracy)
- Inversion successful across multiple days

## ⚠️ Important Notes

1. **EXPERIMENTAL:** Only 37 bets of data - continue tracking!
2. **Use Different Bankroll:** Don't mix with regular predictor bankroll
3. **Track Separately:** Keep Grand Slam results in separate spreadsheet
4. **Conservative Kelly:** Uses 20% instead of 25% due to experimental nature
5. **Verify Pattern Holds:** Need 50+ bets to confirm pattern is real

## 🧪 Validation Plan

Before betting large amounts:

1. **Track 20 more bets** (total 57) to confirm 75%+ win rate holds
2. **Test across multiple slams** (not just Australian Open)
3. **Monitor for model adaptation** (does it start working correctly?)
4. **Compare to regular model** (does regular model improve on slams?)

If after 50+ bets the inverse strategy still shows 70%+ win rate, it's likely a real edge.

## 📊 Model Details

### Features (Same as Regular)
- Player 1 rank
- Player 2 rank  
- Rank difference
- Surface type (Clay/Grass/Hard)

### Key Difference
- **Training Data:** Only Grand Slam matches (not all tournaments)
- **Size:** ~2,400 matches per tour (vs ~11,000 for regular model)
- **Specialization:** Should theoretically understand Grand Slam dynamics better

### Why Inversion Works
The specialized Grand Slam model should work better on slams, but it's actually working **worse**. This suggests systematic bias or miscalibration that we can exploit through inversion.

## 🎲 Risk Management

### Recommended Approach
1. Start with **smaller stakes** ($20-50 per bet) 
2. Track results for **20-30 bets**
3. If win rate stays **above 70%**, gradually increase
4. If win rate **drops below 60%**, stop and reassess
5. Keep **separate bankroll** from regular predictor

### Position Sizing
Uses Kelly Criterion (20% fractional) but you can override:
- **Conservative:** Use 10-15% of suggested stake
- **Moderate:** Use 50% of suggested stake  
- **Aggressive:** Use 100% of suggested stake (not recommended until >50 bets)

## 🤝 When to Use

**Use Grand Slam Inverse Predictor:**
- During Australian Open (January)
- During French Open (May-June)
- During Wimbledon (June-July)
- During US Open (August-September)

**Use Regular Predictor:**
- All other times
- ATP 250/500/Masters
- WTA tournaments
- Any non-Grand Slam event

## 📈 Performance Tracking

Same spreadsheet format as regular predictor:
- Date
- Player 1
- Player 2
- Competition (e.g., "ATP Australian Open")
- Player 1 Odds
- Player 2 Odds
- Bet
- Potential Buyout
- Outcome (W/L)
- Earnings

**Keep Grand Slam results separate** to track inverse strategy performance independently.

## 🔬 Scientific Notes

This is a rare case of a **"wrong model being useful"**:
- Random model: 50% win rate
- Correct model: >50% win rate
- **Consistently wrong model: Can be inverted for >50% win rate**

The key is **consistency**. A model that's wrong 78% of the time is more valuable than a model that's wrong 50% of the time (random).

## ⚖️ Disclaimer

**This is highly experimental.**

- Based on only 37 bets of data
- Grand Slams are inherently volatile
- Past performance ≠ future results
- The pattern could break at any time
- Use at your own risk
- Only bet what you can afford to lose
- Consider this a learning experiment, not a guaranteed profit system

## 🙏 Credits

- Historical data: [Jeff Sackmann's Tennis Databases](https://github.com/JeffSackmann/tennis_atp)
- Match data: [API-Tennis.com](https://api.api-tennis.com/)
- Odds: Bet365
- Inverse strategy discovery: Data analysis of regular model failures

## 📄 License

MIT License - Experimental system, use at own risk.
