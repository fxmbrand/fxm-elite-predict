# FXM Elite Predict - Deployment Guide

## Deployment Options

This guide covers multiple deployment options for the FXM Elite Predict system, from zero-cost solutions to premium hosting.

---

## Option 1: GitHub Pages (Recommended - Free)

GitHub Pages provides completely free static site hosting directly from your repository with automatic HTTPS.

### Setup Steps

**Step 1: Prepare Your Repository**

Ensure your repository structure looks like this:
```
fxm-elite-predict/
├── .github/
│   └── workflows/
│       └── daily_scraper.yml
├── scraper/
│   ├── sofascore_scraper.py
│   └── generate_html.py
├── data/
│   └── predictions/
│       └── latest.json
└── website/
    └── index.html
```

**Step 2: Enable GitHub Pages**

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select **Deploy from a branch**
4. Choose **main** branch and **/website** folder
5. Click **Save**

**Step 3: Access Your Site**

Your site will be live at `https://yourusername.github.io/fxm-elite-predict/` within a few minutes.

### Custom Domain (Optional)

To use a custom domain like `fxmelitepredict.com`:

1. Purchase a domain from Namecheap, GoDaddy, or Google Domains (~$10-15/year)
2. Add a CNAME file to your `website/` directory containing your domain
3. Configure DNS settings at your domain registrar:
   - Add a CNAME record pointing to `yourusername.github.io`
4. In GitHub Pages settings, enter your custom domain and enable HTTPS

---

## Option 2: InfinityFree Hosting (Free)

InfinityFree offers free PHP/MySQL hosting with FTP access, perfect for static sites.

### Setup Steps

**Step 1: Create Account**

1. Visit [infinityfree.net](https://infinityfree.net)
2. Sign up for a free account
3. Create a new website (you'll get a free subdomain like `fxmelite.infinityfreeapp.com`)

**Step 2: Upload Files via FTP**

1. Download an FTP client like FileZilla
2. Get your FTP credentials from InfinityFree control panel
3. Connect to your hosting account
4. Upload all files from your `website/` directory to the `htdocs/` folder

**Step 3: Configure Data Updates**

Since InfinityFree doesn't support Python, you'll need to:

1. Run the scraper locally or via GitHub Actions
2. Upload the generated `index.html` file to InfinityFree via FTP after each update
3. Alternatively, use GitHub Actions to automatically commit updates, then manually sync to InfinityFree

### Automation with InfinityFree

Create a simple PHP script to fetch the latest HTML from your GitHub repository:

```php
<?php
// fetch_latest.php
$github_url = "https://raw.githubusercontent.com/yourusername/fxm-elite-predict/main/website/index.html";
$html = file_get_contents($github_url);
file_put_contents("index.html", $html);
echo "Updated successfully!";
?>
```

Set up a cron job in InfinityFree to run this script daily.

---

## Option 3: Netlify (Free Tier)

Netlify offers automatic deployment from GitHub with built-in CI/CD.

### Setup Steps

**Step 1: Connect Repository**

1. Sign up at [netlify.com](https://netlify.com)
2. Click **New site from Git**
3. Connect your GitHub account and select your repository

**Step 2: Configure Build Settings**

- **Build command**: `cd scraper && python generate_html.py`
- **Publish directory**: `website`

**Step 3: Deploy**

Netlify will automatically build and deploy your site. Every push to your repository triggers a new deployment.

### Custom Domain

Netlify provides free HTTPS for custom domains. Simply add your domain in the Netlify dashboard and update your DNS settings.

---

## Option 4: Vercel (Free Tier)

Similar to Netlify, Vercel offers seamless GitHub integration.

### Setup Steps

1. Sign up at [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Set build settings:
   - **Build Command**: `cd scraper && python generate_html.py`
   - **Output Directory**: `website`
4. Deploy

Vercel provides automatic HTTPS and global CDN distribution.

---

## Automation Strategy

### GitHub Actions Workflow

The `.github/workflows/daily_scraper.yml` file automates the entire process:

1. **Scheduled Execution**: Runs daily at 6:00 AM UTC
2. **Scraping**: Collects tennis predictions from SofaScore
3. **Processing**: Filters matches with 70%+ consensus
4. **Generation**: Creates static HTML website
5. **Deployment**: Commits updated files to repository

### Manual Triggering

You can manually trigger the workflow from the GitHub Actions tab for immediate updates.

---

## Data Flow Architecture

```
SofaScore → Scraper (Python) → JSON Data → HTML Generator → Static Website → Hosting Platform
```

**Daily Cycle**:
- 6:00 AM UTC: GitHub Actions runs scraper
- 6:02 AM UTC: New predictions saved to JSON
- 6:03 AM UTC: HTML website regenerated
- 6:04 AM UTC: Files committed to repository
- 6:05 AM UTC: Hosting platform auto-deploys (GitHub Pages/Netlify/Vercel)

---

## Monitoring and Maintenance

### Check Scraper Status

1. Go to your repository on GitHub
2. Click **Actions** tab
3. View recent workflow runs
4. Check for any failures or errors

### Update Scraper

If SofaScore changes their website structure:

1. Update selectors in `sofascore_scraper.py`
2. Test locally with `python sofascore_scraper.py`
3. Commit and push changes
4. GitHub Actions will use the updated scraper

### Backup Strategy

GitHub automatically maintains version history of all files. You can revert to any previous version if needed.

---

## Cost Comparison

| Platform | Cost | Custom Domain | HTTPS | Auto-Deploy | Notes |
|----------|------|---------------|-------|-------------|-------|
| GitHub Pages | Free | Yes (~$10/year) | Yes | Yes | Best for open-source projects |
| InfinityFree | Free | Yes (~$10/year) | Yes | Manual | Requires FTP uploads |
| Netlify | Free | Yes (included) | Yes | Yes | 100GB bandwidth/month |
| Vercel | Free | Yes (included) | Yes | Yes | Unlimited bandwidth |

---

## Recommended Setup

For **zero-cost operation with minimal maintenance**:

1. **Use GitHub Pages** for hosting (free, automatic deployment)
2. **Use GitHub Actions** for daily scraping (free 2,000 minutes/month)
3. **Optional**: Purchase custom domain for $10-15/year

This setup requires **zero ongoing costs** and **minimal manual intervention** (just monitor GitHub Actions for failures).

---

## Troubleshooting

### Scraper Fails

**Issue**: GitHub Actions workflow fails with errors

**Solution**:
- Check if SofaScore changed their website structure
- Review error logs in GitHub Actions
- Update scraper selectors if needed

### Website Not Updating

**Issue**: New predictions not appearing on site

**Solution**:
- Verify GitHub Actions workflow completed successfully
- Check if hosting platform deployed latest changes
- Clear browser cache and reload

### No Predictions Found

**Issue**: Scraper runs but finds zero elite predictions

**Solution**:
- This is normal if no matches meet the 70% threshold
- Check SofaScore manually to verify voting data exists
- Consider lowering threshold temporarily for testing

---

## Security Considerations

### API Keys and Secrets

The current setup requires no API keys or secrets, as it scrapes publicly available data. If you add features requiring authentication:

1. Use GitHub Secrets to store sensitive data
2. Never commit API keys to the repository
3. Access secrets in workflows via `${{ secrets.SECRET_NAME }}`

### Rate Limiting

The scraper includes delays to avoid overwhelming SofaScore's servers. Maintain these delays to be a good internet citizen and avoid IP bans.

---

## Scaling Considerations

### Adding More Sports

To expand beyond tennis:

1. Create new scraper modules for each sport
2. Update GitHub Actions workflow to run all scrapers
3. Modify HTML generator to handle multiple sports
4. Update website layout to categorize predictions by sport

### Handling High Traffic

If your site grows popular:

- GitHub Pages handles millions of requests
- Netlify/Vercel offer unlimited bandwidth on free tier
- Consider adding analytics to track usage
- Implement caching headers for better performance

---

## Support and Updates

For questions or issues:

1. Check GitHub Actions logs for scraper errors
2. Review SofaScore's website for structural changes
3. Update scraper code as needed
4. Monitor community forums for SofaScore API discussions

---

## Conclusion

The FXM Elite Predict system is designed for **zero-cost operation** with **minimal maintenance**. By leveraging free-tier services and automation, you can run a professional sports prediction platform without ongoing expenses or constant manual work.

Choose the deployment option that best fits your needs, set up the automation, and let the system run itself!
