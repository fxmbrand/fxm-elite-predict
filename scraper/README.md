# FXM Elite Predict - Scraper Documentation

## Overview

The FXM Elite Predict scraper is a Python-based automation tool that collects tennis match predictions from SofaScore, filters matches with seventy percent or greater community consensus, and generates a static website displaying elite predictions.

## Components

### Core Scripts

**sofascore_scraper.py**: The main scraping engine that uses Playwright to navigate SofaScore's tennis section, extract community voting data, and identify matches meeting the elite consensus threshold. The scraper runs headlessly by default and includes comprehensive error handling and retry logic.

**generate_html.py**: Converts the JSON prediction data into a beautiful, responsive static HTML website. The generated site features modern design, mobile optimization, and clear presentation of elite predictions with consensus percentages.

## Installation

### Prerequisites

The scraper requires Python 3.11 or higher and several dependencies. Install them using the following commands:

```bash
pip install playwright beautifulsoup4 requests
playwright install chromium
```

### Local Setup

To run the scraper locally for testing or development:

```bash
cd scraper
python sofascore_scraper.py
python generate_html.py
```

The scraper will create a `data/predictions/` directory containing JSON files with prediction data, and a `website/` directory with the generated HTML.

## GitHub Actions Automation

### Automated Daily Execution

The scraper is configured to run automatically via GitHub Actions every day at 6:00 AM UTC. The workflow performs the following steps:

1. Checks out the repository code
2. Sets up Python 3.11 environment
3. Installs required dependencies including Playwright
4. Executes the scraper to collect fresh predictions
5. Generates the static HTML website
6. Commits and pushes the updated data and website files

### Manual Triggering

You can manually trigger the scraper workflow from the GitHub Actions tab in your repository. This is useful for testing or getting immediate updates outside the scheduled time.

### Workflow Configuration

The workflow is defined in `.github/workflows/daily_scraper.yml`. You can modify the cron schedule to change the execution time. The current schedule `0 6 * * *` runs at 6:00 AM UTC daily.

## Data Structure

### Prediction JSON Format

Each prediction contains the following fields:

```json
{
  "match_id": "unique_identifier",
  "player_1": "Player Name",
  "player_2": "Opponent Name",
  "tournament": "Tournament Name",
  "match_time": "YYYY-MM-DD HH:MM",
  "player_1_votes": 45,
  "player_2_votes": 55,
  "total_votes": 8500,
  "consensus_player": "Player with majority",
  "consensus_percentage": 55
}
```

### Output Files

**data/predictions/YYYY-MM-DD.json**: Daily prediction file with timestamp and all elite predictions for that date.

**data/predictions/latest.json**: Always contains the most recent predictions for easy access by the website.

**website/index.html**: The generated static website ready for deployment.

## Deployment Options

### Option 1: GitHub Pages (Recommended)

GitHub Pages provides free hosting directly from your repository. To enable:

1. Go to repository Settings → Pages
2. Select "Deploy from a branch"
3. Choose "main" branch and "/website" folder
4. Your site will be live at `https://yourusername.github.io/fxm-elite-predict/`

### Option 2: InfinityFree Hosting

InfinityFree offers free PHP/MySQL hosting. To deploy:

1. Create an account at infinityfree.net
2. Use FTP to upload the contents of the `website/` directory
3. The static HTML will work immediately without any server-side processing
4. Optionally, set up a custom domain

### Option 3: Netlify or Vercel

Both platforms offer free static site hosting with automatic deployment from GitHub:

1. Connect your GitHub repository
2. Set build directory to `website/`
3. Deploy automatically on every push

## Customization

### Adjusting Consensus Threshold

To change the minimum consensus percentage, modify the `CONSENSUS_THRESHOLD` constant in `sofascore_scraper.py`:

```python
CONSENSUS_THRESHOLD = 75  # Change from 70 to 75
```

### Changing Scraping Schedule

Edit the cron expression in `.github/workflows/daily_scraper.yml`:

```yaml
schedule:
  - cron: '0 12 * * *'  # Run at noon UTC instead of 6 AM
```

### Styling the Website

The HTML generator includes embedded CSS in `generate_html.py`. Modify the `<style>` section to customize colors, fonts, and layout. The current design uses:

- Navy blue background (#1a2332)
- Electric green accents (#00ff88)
- Responsive grid layout
- Mobile-optimized design

## Important Notes

### SofaScore Structure Changes

SofaScore may update their website structure, which could break the scraper. The current implementation includes placeholder data to demonstrate the system architecture. For production use, you will need to:

1. Inspect SofaScore's actual HTML structure using browser developer tools
2. Update the CSS selectors in `_extract_predictions()` method
3. Alternatively, reverse-engineer their API endpoints for more reliable data access

### Rate Limiting and Ethics

The scraper includes delays and uses headless browsing to minimize server load. Always respect SofaScore's terms of service and consider using their official API if available. Implement additional rate limiting if scraping frequently.

### Error Handling

The scraper includes comprehensive error handling and will continue operation even if individual matches fail to parse. All errors are logged to console for debugging.

## Monitoring and Maintenance

### Checking Scraper Status

Monitor the GitHub Actions tab in your repository to ensure the daily scraper runs successfully. Failed runs will send email notifications if configured.

### Data Quality Checks

Periodically review the generated JSON files to ensure data quality. The scraper includes validation to filter out incomplete or malformed predictions.

### Updates and Maintenance

Plan to review and update the scraper monthly to account for any changes in SofaScore's website structure. Keep dependencies updated for security and compatibility.

## Troubleshooting

### Scraper Fails to Run

Check that Playwright is properly installed with `playwright install chromium`. Ensure the GitHub Actions workflow has sufficient permissions to commit and push changes.

### No Predictions Found

This may occur if no matches meet the seventy percent threshold on a given day, or if SofaScore's structure has changed. Review the console output for specific error messages.

### Website Not Updating

Verify that the GitHub Actions workflow completed successfully and that the generated HTML was committed to the repository. Check your hosting platform's deployment logs.

## Future Enhancements

Potential improvements to the scraper system include:

- Integration with SofaScore's official API (if available)
- Support for additional sports beyond tennis
- Historical accuracy tracking and performance analytics
- Email or Telegram notifications for new elite predictions
- Machine learning models to enhance consensus predictions
- Multi-language support for international audiences

## Support and Contribution

This scraper is part of the FXM Elite Predict project. For issues, suggestions, or contributions, please refer to the main project documentation.
