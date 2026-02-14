# FXM Elite Predict - Research Notes

## SofaScore Community Voting System

### Key Findings:

1. **Community Voting Exists**: SofaScore has a "Who will win?" voting feature where users vote on match outcomes
2. **Vote Display**: Shows percentage breakdown (e.g., 11% vs 89% for Kecmanovic vs Shelton match)
3. **Total Votes**: Displays total vote count (e.g., "Total votes: 6.2k")
4. **Match Coverage**: Available for tennis matches across ATP, WTA, Challenger, and ITF tournaments

### Data Points Available:
- Match details (players, tournament, time)
- Community vote percentages
- Total vote count
- Betting odds from multiple bookmakers
- Match statistics (when available)

### Technical Considerations:
- SofaScore uses dynamic content loading (React-based frontend)
- No official public API documented
- Community has built scrapers using:
  - Playwright (for dynamic content)
  - BeautifulSoup (for static parsing)
  - Direct API endpoint access (undocumented)
  
### 70% Consensus Threshold:
- The original ElitePredict concept filters matches where one player has ≥70% community consensus
- This creates "high-confidence" predictions based on crowd wisdom
- For tennis, this threshold appears achievable based on observed vote distributions

## Next Steps:
1. Build lightweight Python scraper for tennis matches
2. Filter matches with ≥70% consensus
3. Store data in simple database (SQLite for free hosting compatibility)
4. Create static website to display predictions
5. Automate daily scraping with minimal server requirements


## Hosting Architecture for Zero-Cost System

### InfinityFree Limitations:
- **Only supports**: PHP, MySQL, HTML, CSS, JavaScript
- **Does NOT support**: Python, Node.js, or other backend languages
- **Best for**: Static websites with PHP backend

### Recommended Free Architecture:

**Option 1: Hybrid Approach (Recommended)**
1. **Scraper/Bot**: Run on free tier of Render, Railway, or GitHub Actions
   - GitHub Actions: Free 2,000 minutes/month (perfect for scheduled scraping)
   - Runs Python script daily to scrape SofaScore
   - Outputs JSON file with predictions
   
2. **Data Storage**: 
   - Store predictions as static JSON files
   - Upload to InfinityFree via FTP or commit to GitHub
   
3. **Website Frontend**: 
   - Static HTML/CSS/JavaScript hosted on InfinityFree
   - Reads JSON file and displays predictions
   - No backend processing needed

**Option 2: Fully Static (Simplest)**
1. **GitHub Actions**: 
   - Runs Python scraper daily (cron schedule)
   - Generates static HTML pages with predictions
   - Commits to GitHub repository
   
2. **GitHub Pages or InfinityFree**:
   - Hosts the static HTML files
   - Auto-updates when GitHub Actions commits new files

**Option 3: Serverless**
1. **Scraper**: Vercel/Netlify serverless functions (free tier)
2. **Frontend**: Static site on Vercel/Netlify
3. **Database**: Free tier of MongoDB Atlas or Supabase

### Chosen Architecture for FXM Elite Predict:
**GitHub Actions + Static Site (Zero Cost)**
- Python scraper runs via GitHub Actions (scheduled daily)
- Generates JSON data file with 70%+ consensus matches
- Builds static HTML site
- Deploys to InfinityFree or GitHub Pages
- Total cost: $0
- Maintenance: Minimal (just monitor GitHub Actions)
