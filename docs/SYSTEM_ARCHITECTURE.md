# FXM Elite Predict - System Architecture Document

## Executive Summary

FXM Elite Predict is a **zero-cost sports prediction platform** focused initially on tennis, leveraging community consensus data from SofaScore to identify high-confidence betting opportunities. The system employs a lightweight, fully automated architecture that requires minimal maintenance while delivering daily predictions to users through a modern static website.

## Business Overview

**Business Name**: FXM Elite Predict

**Tagline**: "Elite Predictions, Powered by Community Wisdom"

**Core Value Proposition**: The platform filters tennis matches where community consensus reaches or exceeds seventy percent, creating a curated list of high-confidence predictions. This approach harnesses the collective intelligence of thousands of sports enthusiasts while eliminating noise from low-confidence predictions.

**Target Audience**: The primary audience consists of casual sports bettors seeking data-driven insights, tennis enthusiasts looking for informed predictions, and individuals interested in leveraging crowd wisdom for betting decisions.

## System Architecture

### Architecture Philosophy

The system is designed around three core principles: zero operational cost, minimal maintenance overhead, and maximum automation. By leveraging free-tier services and static site generation, the platform achieves sustainability without requiring ongoing financial investment or constant manual intervention.

### Component Overview

The architecture consists of three primary components working in concert to deliver predictions. The **Data Collection Engine** scrapes SofaScore daily to gather tennis match data and community voting percentages. The **Processing Pipeline** filters matches meeting the seventy percent consensus threshold and generates structured data files. The **Presentation Layer** serves predictions to users through a responsive static website.

### Data Collection Engine

The data collection engine is a Python-based web scraper that runs automatically via GitHub Actions on a scheduled basis. The scraper targets SofaScore's tennis section, extracting upcoming matches along with their associated community voting data. It employs the Playwright library to handle dynamic content loading, ensuring accurate data capture even as SofaScore's interface evolves.

The scraper operates on a daily schedule, typically running in the early morning hours to capture the full day's tennis schedule. It collects match details including player names, tournament information, match timing, community vote percentages, and total vote counts. This data is then validated and structured into a standardized JSON format.

**Technical Implementation**: The scraper uses headless browser automation to navigate SofaScore's tennis schedule pages. It waits for dynamic content to load, extracts voting percentages from the "Who will win?" sections, and applies the seventy percent filter. Error handling ensures that temporary network issues or site changes do not crash the entire pipeline.

### Processing Pipeline

Once raw data is collected, the processing pipeline applies business logic to identify elite predictions. The primary filter checks whether either player in a match has achieved seventy percent or greater community consensus. Matches meeting this threshold are flagged as "Elite Predictions" and prioritized in the output.

The pipeline also enriches the data with additional context, including match importance indicators based on tournament tier (Grand Slam, ATP Masters, ATP 500, etc.), historical accuracy tracking when available, and confidence scoring based on total vote count. Matches with higher total votes receive higher confidence scores, as they represent broader community agreement.

**Output Format**: The pipeline generates multiple output files to support different use cases. A primary JSON file contains all elite predictions for the current day, while a historical archive maintains past predictions for accuracy tracking. An HTML fragment is also generated for easy integration into the static website.

### Presentation Layer

The presentation layer is a static website built with HTML, CSS, and vanilla JavaScript. The site reads the generated JSON files and dynamically renders prediction cards for each elite match. The design emphasizes clarity and mobile responsiveness, ensuring users can quickly access predictions on any device.

**Key Features**: The website displays each elite prediction with player names, tournament context, match time, community consensus percentage, and a visual confidence indicator. Users can filter predictions by tournament tier, sort by consensus percentage or match time, and view historical accuracy statistics. The interface updates automatically each day as new predictions are generated.

**Hosting**: The static site is hosted on InfinityFree, which provides free PHP and MySQL hosting along with a custom domain option. Since the site is purely static (HTML/CSS/JS), it requires no server-side processing and loads extremely quickly. Alternatively, GitHub Pages can be used for even simpler deployment directly from the repository.

## Automation Workflow

### GitHub Actions Workflow

The entire system runs automatically through a GitHub Actions workflow configured to execute daily. The workflow follows a sequential process: first, it checks out the repository code; second, it sets up the Python environment and installs dependencies; third, it runs the scraper to collect fresh data; fourth, it executes the processing pipeline to generate predictions; fifth, it commits the updated JSON and HTML files back to the repository; and finally, it optionally triggers a deployment to the hosting platform.

**Schedule**: The workflow is configured with a cron expression to run at 6:00 AM UTC daily, ensuring predictions are available before most tennis matches begin. The workflow can also be triggered manually for testing or immediate updates.

**Resource Usage**: GitHub Actions provides 2,000 free minutes per month for public repositories. The scraper and processing pipeline typically complete in under five minutes, meaning the system uses approximately 150 minutes per month, well within the free tier limits.

### Error Handling and Monitoring

The system includes comprehensive error handling to ensure reliability. If the scraper encounters an error (such as SofaScore being temporarily unavailable), it retries up to three times with exponential backoff. If all retries fail, the workflow logs the error and sends a notification via GitHub Actions email alerts.

The system also maintains a health check log that tracks successful runs, data quality metrics, and any anomalies detected. This log can be reviewed periodically to ensure the system continues operating correctly.

## Data Storage Strategy

### File-Based Storage

Rather than using a traditional database, the system employs a file-based storage approach optimized for static site hosting. All predictions are stored as JSON files in the repository, with a clear directory structure organizing data by date and type.

**Directory Structure**:
```
/data
  /predictions
    /2026-02-14.json
    /2026-02-15.json
  /archive
    /2026-02
      /daily_summaries.json
  /current
    /today.json
    /latest.json
```

This approach eliminates the need for database hosting, simplifies deployment, and ensures all data is version-controlled. Historical predictions are automatically archived monthly to keep the repository size manageable.

### Data Retention

The system retains detailed prediction data for ninety days, after which older records are aggregated into monthly summary files. This balance ensures sufficient data for accuracy tracking while preventing unbounded growth.

## Scalability and Expansion

### Adding More Sports

The architecture is designed to easily accommodate additional sports beyond tennis. To add a new sport, a developer would create a new scraper module following the same pattern as the tennis scraper, configure it to target the appropriate SofaScore pages, and integrate it into the GitHub Actions workflow. The processing pipeline and presentation layer are sport-agnostic and require minimal modification.

**Priority Expansion Order**: Based on SofaScore data availability and betting popularity, the recommended expansion sequence is tennis (current), basketball, football (soccer), and esports.

### Performance Optimization

As the system scales to cover multiple sports, performance optimizations may be necessary. Potential optimizations include parallel scraping for multiple sports, caching mechanisms to reduce redundant API calls, and incremental data updates rather than full daily refreshes.

## Security and Compliance

### Data Privacy

The system does not collect or store any user data, eliminating most privacy concerns. All data is sourced from publicly available SofaScore pages, and no authentication or personal information is required.

### Responsible Gambling

The website includes prominent responsible gambling messaging, encouraging users to bet responsibly and providing links to gambling addiction resources. The platform explicitly disclaims any guarantees of profitability and emphasizes that predictions are for informational purposes only.

## Maintenance Requirements

### Minimal Maintenance Design

The system is engineered to require minimal ongoing maintenance. Once deployed, it operates autonomously with no manual intervention needed for daily operations. The primary maintenance tasks are monitoring GitHub Actions for failures, updating scraper selectors if SofaScore changes its HTML structure, and reviewing accuracy metrics monthly.

**Estimated Time Commitment**: Approximately one to two hours per month for routine monitoring and occasional updates.

### Update Procedures

When SofaScore updates its website structure, the scraper may need adjustments. The system includes a test suite that can be run locally to verify scraper functionality before deploying changes. Updates are made to the scraper code, tested locally, and then pushed to the repository, where GitHub Actions automatically deploys the new version.

## Cost Analysis

### Total Cost: $0

The entire system operates at zero cost by leveraging free-tier services:

| Component | Service | Cost |
|-----------|---------|------|
| Scraper Automation | GitHub Actions | $0 (2,000 free minutes/month) |
| Code Repository | GitHub | $0 (public repository) |
| Website Hosting | InfinityFree or GitHub Pages | $0 |
| Domain Name | InfinityFree subdomain | $0 (optional custom domain ~$10/year) |
| SSL Certificate | Included with hosting | $0 |

**Optional Costs**: A custom domain name is the only potential expense, typically costing ten to fifteen dollars annually. This is entirely optional, as free subdomains are provided by both InfinityFree and GitHub Pages.

## Future Enhancements

### Phase 1: Foundation (Current)
The current phase focuses on establishing a reliable tennis prediction system with automated data collection and a functional website.

### Phase 2: Enhanced Analytics
Future enhancements include historical accuracy tracking with detailed statistics, confidence scoring algorithms incorporating multiple factors, and trend analysis showing how consensus changes over time.

### Phase 3: User Engagement
Potential user engagement features include email or Telegram notifications for elite predictions, user accounts for tracking personal betting records, and community features allowing users to share their own insights.

### Phase 4: Monetization
If the platform gains traction, monetization options include premium subscriptions for multi-sport predictions and advanced analytics, affiliate partnerships with reputable sportsbooks, and display advertising with careful placement to avoid disrupting user experience.

## Technical Stack Summary

**Backend Automation**: Python 3.11 with Playwright for web scraping, Pandas for data processing, and JSON for data serialization.

**Frontend**: HTML5, CSS3 with responsive design, vanilla JavaScript for dynamic content rendering, and optional TailwindCSS for rapid styling.

**Infrastructure**: GitHub for version control and automation, GitHub Actions for scheduled task execution, and InfinityFree or GitHub Pages for static hosting.

**Development Tools**: Visual Studio Code for coding, Git for version control, and local Python environment for testing.

## Conclusion

The FXM Elite Predict system demonstrates that a sophisticated sports prediction platform can be built and operated at zero cost while maintaining high reliability and minimal maintenance requirements. By leveraging community consensus data, static site architecture, and free-tier cloud services, the platform delivers genuine value to users without requiring financial investment or extensive technical infrastructure.

The modular design ensures easy expansion to additional sports, while the automated workflow eliminates manual data collection and processing. This architecture serves as a blueprint for building sustainable, zero-cost web applications in the sports analytics domain.
