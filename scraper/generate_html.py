#!/usr/bin/env python3
"""
FXM Elite Predict - HTML Generator
Converts JSON predictions to static HTML website
"""

import json
import os
from datetime import datetime
from typing import Dict, List


def load_latest_predictions(predictions_dir: str = "../data/predictions") -> Dict:
    """Load the latest predictions from JSON"""
    latest_file = os.path.join(predictions_dir, "latest.json")
    
    if not os.path.exists(latest_file):
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "predictions": [],
            "total_predictions": 0
        }
    
    with open(latest_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_prediction_card(prediction: Dict) -> str:
    """Generate HTML for a single prediction card"""
    return f"""
    <div class="prediction-card">
        <div class="tournament-badge">{prediction['tournament']}</div>
        <div class="match-info">
            <div class="player player-1">
                <span class="player-name">{prediction['player_1']}</span>
                <span class="vote-percentage">{prediction['player_1_votes']}%</span>
            </div>
            <div class="vs">VS</div>
            <div class="player player-2">
                <span class="player-name">{prediction['player_2']}</span>
                <span class="vote-percentage">{prediction['player_2_votes']}%</span>
            </div>
        </div>
        <div class="consensus-info">
            <div class="consensus-badge">
                <span class="consensus-percentage">{prediction['consensus_percentage']}%</span>
                <span class="consensus-label">CONSENSUS</span>
            </div>
            <div class="consensus-player">
                <strong>Elite Pick:</strong> {prediction['consensus_player']}
            </div>
        </div>
        <div class="match-details">
            <div class="detail">
                <span class="icon">🕐</span>
                <span>{prediction['match_time']}</span>
            </div>
            <div class="detail">
                <span class="icon">👥</span>
                <span>{prediction['total_votes']:,} votes</span>
            </div>
        </div>
    </div>
    """


def generate_html(data: Dict) -> str:
    """Generate complete HTML page"""
    predictions_html = ""
    
    if data['predictions']:
        for pred in data['predictions']:
            predictions_html += generate_prediction_card(pred)
    else:
        predictions_html = """
        <div class="no-predictions">
            <h2>No Elite Predictions Today</h2>
            <p>No matches meet the 70%+ consensus threshold today. Check back tomorrow!</p>
        </div>
        """
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FXM Elite Predict - Tennis Predictions</title>
    <meta name="description" content="Elite tennis predictions powered by 70%+ community consensus from SofaScore">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #0d1117 0%, #1a2332 100%);
            color: #ffffff;
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        header {{
            text-align: center;
            padding: 40px 20px;
            margin-bottom: 40px;
        }}
        
        .logo {{
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #ffffff 0%, #00ff88 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .tagline {{
            font-size: 18px;
            color: #00ff88;
            margin-bottom: 20px;
        }}
        
        .update-info {{
            font-size: 14px;
            color: #8b949e;
            margin-top: 10px;
        }}
        
        .stats-bar {{
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }}
        
        .stat {{
            text-align: center;
        }}
        
        .stat-value {{
            font-size: 36px;
            font-weight: 700;
            color: #00ff88;
        }}
        
        .stat-label {{
            font-size: 14px;
            color: #8b949e;
            margin-top: 5px;
        }}
        
        .predictions-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        
        .prediction-card {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 24px;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        
        .prediction-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 255, 136, 0.2);
            border-color: #00ff88;
        }}
        
        .tournament-badge {{
            display: inline-block;
            background: rgba(0, 255, 136, 0.2);
            color: #00ff88;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 16px;
        }}
        
        .match-info {{
            margin-bottom: 20px;
        }}
        
        .player {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
        }}
        
        .player-name {{
            font-size: 18px;
            font-weight: 600;
        }}
        
        .vote-percentage {{
            font-size: 16px;
            color: #8b949e;
        }}
        
        .vs {{
            text-align: center;
            color: #8b949e;
            font-weight: 700;
            padding: 8px 0;
        }}
        
        .consensus-info {{
            background: rgba(0, 255, 136, 0.1);
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
        }}
        
        .consensus-badge {{
            text-align: center;
            margin-bottom: 12px;
        }}
        
        .consensus-percentage {{
            font-size: 32px;
            font-weight: 900;
            color: #00ff88;
            display: block;
        }}
        
        .consensus-label {{
            font-size: 12px;
            color: #8b949e;
            letter-spacing: 2px;
        }}
        
        .consensus-player {{
            text-align: center;
            font-size: 16px;
        }}
        
        .match-details {{
            display: flex;
            justify-content: space-around;
            padding-top: 16px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        .detail {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
            color: #8b949e;
        }}
        
        .no-predictions {{
            text-align: center;
            padding: 60px 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
        }}
        
        .no-predictions h2 {{
            margin-bottom: 16px;
            color: #00ff88;
        }}
        
        footer {{
            text-align: center;
            padding: 40px 20px;
            color: #8b949e;
            font-size: 14px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        .disclaimer {{
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background: rgba(255, 193, 7, 0.1);
            border-left: 4px solid #ffc107;
            border-radius: 8px;
            font-size: 13px;
            line-height: 1.6;
        }}
        
        @media (max-width: 768px) {{
            .predictions-grid {{
                grid-template-columns: 1fr;
            }}
            
            .logo {{
                font-size: 36px;
            }}
            
            .stats-bar {{
                gap: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">FXM ELITE PREDICT</div>
            <div class="tagline">Elite Predictions, Powered by Community Wisdom</div>
            <div class="update-info">Last Updated: {data.get('timestamp', 'N/A')}</div>
        </header>
        
        <div class="stats-bar">
            <div class="stat">
                <div class="stat-value">{data.get('total_predictions', 0)}</div>
                <div class="stat-label">Elite Predictions</div>
            </div>
            <div class="stat">
                <div class="stat-value">70%+</div>
                <div class="stat-label">Consensus Threshold</div>
            </div>
            <div class="stat">
                <div class="stat-value">🎾</div>
                <div class="stat-label">Tennis Focused</div>
            </div>
        </div>
        
        <div class="predictions-grid">
            {predictions_html}
        </div>
        
        <div class="disclaimer">
            <strong>⚠️ Responsible Gambling Disclaimer:</strong> These predictions are for informational and entertainment purposes only. They are based on community consensus data and do not guarantee any outcomes. Please gamble responsibly and never bet more than you can afford to lose. If you have a gambling problem, seek help at <a href="https://www.ncpgambling.org/" style="color: #00ff88;">ncpgambling.org</a>.
        </div>
        
        <footer>
            <p>&copy; 2026 FXM Elite Predict. All rights reserved.</p>
            <p>Data sourced from SofaScore community predictions.</p>
        </footer>
    </div>
</body>
</html>
"""
    
    return html


def main():
    """Main execution function"""
    print("🌐 Generating static HTML website...")
    
    # Load predictions
    data = load_latest_predictions()
    
    # Generate HTML
    html = generate_html(data)
    
    # Save to website directory
    website_dir = "../website"
    os.makedirs(website_dir, exist_ok=True)
    
    output_file = os.path.join(website_dir, "index.html")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ HTML generated successfully: {output_file}")
    print(f"📊 Total predictions: {data.get('total_predictions', 0)}")


if __name__ == "__main__":
    main()
