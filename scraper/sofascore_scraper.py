#!/usr/bin/env python3
"""
FXM Elite Predict - SofaScore Tennis Scraper
Scrapes tennis match predictions with 70%+ community consensus from SofaScore
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import time

try:
    from playwright.sync_api import sync_playwright, Page, Browser
except ImportError:
    print("Playwright not installed. Run: pip install playwright && playwright install")
    exit(1)


class SofaScoreScraper:
    """Scraper for SofaScore tennis predictions with community consensus"""
    
    BASE_URL = "https://www.sofascore.com"
    TENNIS_URL = f"{BASE_URL}/tennis"
    CONSENSUS_THRESHOLD = 70  # Minimum consensus percentage
    
    def __init__(self, headless: bool = True):
        """Initialize the scraper"""
        self.headless = headless
        self.predictions: List[Dict] = []
        
    def scrape_tennis_predictions(self) -> List[Dict]:
        """
        Main scraping function to get tennis predictions with 70%+ consensus
        Returns list of elite predictions
        """
        print(f"🎾 FXM Elite Predict - Starting Tennis Scraper")
        print(f"⏰ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🎯 Consensus Threshold: {self.CONSENSUS_THRESHOLD}%\n")
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            
            try:
                # Navigate to tennis page
                print(f"📡 Navigating to {self.TENNIS_URL}...")
                page.goto(self.TENNIS_URL, wait_until="networkidle", timeout=30000)
                time.sleep(3)  # Allow dynamic content to load
                
                # Extract match data
                self.predictions = self._extract_predictions(page)
                
                # Filter by consensus threshold
                elite_predictions = self._filter_elite_predictions(self.predictions)
                
                print(f"\n✅ Scraping Complete!")
                print(f"📊 Total matches found: {len(self.predictions)}")
                print(f"⭐ Elite predictions (≥{self.CONSENSUS_THRESHOLD}%): {len(elite_predictions)}")
                
                return elite_predictions
                
            except Exception as e:
                print(f"❌ Error during scraping: {str(e)}")
                return []
            finally:
                browser.close()
    
    def _extract_predictions(self, page: Page) -> List[Dict]:
        """Extract match predictions from the page"""
        predictions = []
        
        # Note: This is a simplified implementation
        # SofaScore's actual structure requires inspecting their HTML/API
        # This demonstrates the structure - you'll need to adapt selectors
        
        try:
            # Wait for match elements to load
            page.wait_for_selector('[class*="event"]', timeout=10000)
            
            # Example: Extract match data
            # In reality, you'd need to inspect SofaScore's actual HTML structure
            # or reverse-engineer their API calls
            
            # Placeholder data for demonstration
            # In production, replace with actual scraping logic
            sample_predictions = [
                {
                    "match_id": "demo_001",
                    "player_1": "Novak Djokovic",
                    "player_2": "Carlos Alcaraz",
                    "tournament": "ATP Masters 1000",
                    "match_time": "2026-02-15 14:00",
                    "player_1_votes": 45,
                    "player_2_votes": 55,
                    "total_votes": 8500,
                    "consensus_player": "Carlos Alcaraz",
                    "consensus_percentage": 55
                },
                {
                    "match_id": "demo_002",
                    "player_1": "Iga Swiatek",
                    "player_2": "Aryna Sabalenka",
                    "tournament": "WTA 1000",
                    "match_time": "2026-02-15 16:30",
                    "player_1_votes": 78,
                    "player_2_votes": 22,
                    "total_votes": 12300,
                    "consensus_player": "Iga Swiatek",
                    "consensus_percentage": 78
                },
                {
                    "match_id": "demo_003",
                    "player_1": "Jannik Sinner",
                    "player_2": "Daniil Medvedev",
                    "tournament": "ATP 500",
                    "match_time": "2026-02-15 18:00",
                    "player_1_votes": 72,
                    "player_2_votes": 28,
                    "total_votes": 6700,
                    "consensus_player": "Jannik Sinner",
                    "consensus_percentage": 72
                }
            ]
            
            predictions.extend(sample_predictions)
            
            print(f"📥 Extracted {len(predictions)} matches")
            
        except Exception as e:
            print(f"⚠️  Error extracting predictions: {str(e)}")
        
        return predictions
    
    def _filter_elite_predictions(self, predictions: List[Dict]) -> List[Dict]:
        """Filter predictions that meet the elite consensus threshold"""
        elite = [
            p for p in predictions 
            if p.get('consensus_percentage', 0) >= self.CONSENSUS_THRESHOLD
        ]
        
        # Sort by consensus percentage (highest first)
        elite.sort(key=lambda x: x.get('consensus_percentage', 0), reverse=True)
        
        return elite
    
    def save_predictions(self, predictions: List[Dict], output_dir: str = "../data/predictions"):
        """Save predictions to JSON file"""
        os.makedirs(output_dir, exist_ok=True)
        
        today = datetime.now().strftime("%Y-%m-%d")
        output_file = os.path.join(output_dir, f"{today}.json")
        
        data = {
            "date": today,
            "timestamp": datetime.now().isoformat(),
            "total_predictions": len(predictions),
            "consensus_threshold": self.CONSENSUS_THRESHOLD,
            "predictions": predictions
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Predictions saved to: {output_file}")
        
        # Also save to "latest.json" for easy access
        latest_file = os.path.join(output_dir, "latest.json")
        with open(latest_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Latest predictions saved to: {latest_file}")
        
        return output_file


def main():
    """Main execution function"""
    scraper = SofaScoreScraper(headless=True)
    
    # Scrape predictions
    elite_predictions = scraper.scrape_tennis_predictions()
    
    # Save results
    if elite_predictions:
        scraper.save_predictions(elite_predictions)
        
        print("\n" + "="*60)
        print("🏆 ELITE PREDICTIONS SUMMARY")
        print("="*60)
        
        for idx, pred in enumerate(elite_predictions, 1):
            print(f"\n{idx}. {pred['player_1']} vs {pred['player_2']}")
            print(f"   Tournament: {pred['tournament']}")
            print(f"   Time: {pred['match_time']}")
            print(f"   Consensus: {pred['consensus_percentage']}% for {pred['consensus_player']}")
            print(f"   Total Votes: {pred['total_votes']:,}")
    else:
        print("\n⚠️  No elite predictions found today.")


if __name__ == "__main__":
    main()
