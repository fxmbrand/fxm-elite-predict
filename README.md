# FXM Elite Predict - Tennis Predictions Platform

Elite tennis match predictions powered by 70%+ community consensus from SofaScore.

## Quick Start

### 1. Clone or Extract This Repository
```bash
git clone https://github.com/yourusername/fxm-elite-predict.git
cd fxm-elite-predict
```

### 2. Set Up Python Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Scraper Locally (Optional)
```bash
cd scraper
python sofascore_scraper.py
python generate_html.py
```

### 4. Deploy to GitHub Pages or InfinityFree
See `docs/DEPLOYMENT_GUIDE.md` for detailed instructions.

## Automated Daily Updates

The scraper runs automatically via GitHub Actions every day at 6:00 AM UTC. No manual intervention required!

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── daily_scraper.yml          # GitHub Actions automation
├── scraper/
│   ├── sofascore_scraper.py           # Main scraping engine
│   ├── generate_html.py               # HTML generator
│   └── README.md                      # Scraper documentation
├── data/
│   └── predictions/                   # Generated prediction data
├── website/
│   └── index.html                     # Generated website
├── articles/                          # Medium articles for promotion
├── docs/
│   ├── DEPLOYMENT_GUIDE.md            # Hosting options
│   ├── SYSTEM_ARCHITECTURE.md         # Technical overview
│   └── research_notes.md              # Research findings
└── README.md                          # This file
```

## Features

- 🎾 **Tennis Focused**: Specializes in tennis match predictions
- 🎯 **70%+ Consensus**: Only displays predictions with strong community agreement
- 🤖 **Fully Automated**: Runs daily via GitHub Actions
- 💰 **Zero Cost**: Uses free-tier services only
- 📱 **Mobile Responsive**: Works great on all devices
- ⚡ **Fast Loading**: Static HTML generation for instant performance

## Deployment Options

1. **GitHub Pages** (Recommended) - Free, automatic HTTPS, custom domain support
2. **InfinityFree** - Free PHP hosting with FTP access
3. **Netlify/Vercel** - Free static site hosting with automatic deployment

See `docs/DEPLOYMENT_GUIDE.md` for detailed setup instructions.

## Customization

### Change Consensus Threshold
Edit `scraper/sofascore_scraper.py`:
```python
CONSENSUS_THRESHOLD = 75  # Change from 70 to 75
```

### Change Scraping Schedule
Edit `.github/workflows/daily_scraper.yml`:
```yaml
schedule:
  - cron: '0 12 * * *'  # Run at noon UTC instead of 6 AM
```

### Customize Website Design
Edit the CSS in `scraper/generate_html.py` to change colors, fonts, and layout.

## Documentation

- **[Deployment Guide](docs/DEPLOYMENT_GUIDE.md)** - How to host your site
- **[System Architecture](docs/SYSTEM_ARCHITECTURE.md)** - Technical details
- **[Scraper README](scraper/README.md)** - Scraper-specific documentation
- **[Research Notes](docs/research_notes.md)** - SofaScore analysis

## Medium Articles

Promote your platform with these ready-to-publish articles:

1. **The Wisdom of Crowds in Sports Betting** - Explains community consensus theory
2. **Data-Driven Tennis Betting** - Analytics and statistics approach
3. **The Psychology of Sports Betting** - Cognitive biases and emotional discipline
4. **Bankroll Management for Sports Bettors** - Risk management strategies
5. **Finding Value Bets Using Community Consensus** - Practical value betting guide

## Important Notes

### Responsible Gambling
These predictions are for informational and entertainment purposes only. They do not guarantee outcomes. Please gamble responsibly and never bet more than you can afford to lose.

### SofaScore Terms
Ensure compliance with SofaScore's terms of service. The current implementation includes placeholder data. For production use, you may need to adapt to SofaScore's actual API or website structure.

### Rate Limiting
The scraper includes delays to minimize server load. Always respect website terms of service and implement additional rate limiting if needed.

## Revenue Potential

- **Year 1**: $500-$2,000/month (affiliate commissions + ads)
- **Year 2**: $3,000-$8,000/month (premium subscriptions + affiliates)
- **Year 3**: $10,000-$25,000/month (full monetization)

## Getting Help

1. Check the documentation in the `docs/` folder
2. Review the scraper README for troubleshooting
3. Check GitHub Actions logs for automation issues
4. Review SofaScore's website structure if scraper fails

## License

This project is provided as-is for educational and personal use.

## Support

For issues, suggestions, or improvements, please refer to the documentation or create an issue in your GitHub repository.

---

**Ready to launch?** Follow the Quick Start above, then see `docs/DEPLOYMENT_GUIDE.md` for hosting options.
