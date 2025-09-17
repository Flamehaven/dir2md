# Security Guidelines for Dir2md

## 🔐 License Key Management

### Safe Practices

#### ✅ DO:
- Use environment variables: `export DIR2MD_LICENSE="PRO-your_key"`
- Create `.env` file locally (already in .gitignore)
- Use different keys for development/production
- Rotate keys periodically

#### ❌ DON'T:
- Never commit license keys to Git
- Don't hardcode keys in scripts
- Avoid sharing keys in plain text
- Don't use production keys in testing

### Setting Up Pro License

1. **Create local environment file:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual license key
   ```

2. **Or use environment variable:**
   ```bash
   export DIR2MD_LICENSE="PRO-your_license_key_here"
   ```

3. **Verify activation:**
   ```bash
   dir2md --version --verbose
   ```

### Development vs Production

#### Development Environment:
```bash
# .env.development
DIR2MD_LICENSE=PRO-dev_key_123456789
DIR2MD_LOG_LEVEL=DEBUG
```

#### Production Environment:
```bash
# Use secure secret management
export DIR2MD_LICENSE="${PROD_LICENSE_KEY}"
```

### Git Safety Checks

Before committing, always run:
```bash
# Check for accidentally committed secrets
git diff --cached | grep -i "PRO-\|license\|key\|secret"

# Use git-secrets if available
git secrets --scan
```

### License Key Format

Valid Pro keys must:
- Start with `PRO-`
- Be at least 11 characters total
- Example: `PRO-abc123def456`

### Troubleshooting

#### Key Not Working:
1. Check format: `PRO-` prefix + sufficient length
2. Verify environment variable is set
3. Restart application after setting key
4. Check for typos or extra spaces

#### Accidental Exposure:
1. Immediately rotate the key
2. Remove from Git history if committed
3. Check GitHub/GitLab secret scanning alerts
4. Update all environments with new key

### Contact

For license issues: https://dir2md.com/support
For security concerns: security@dir2md.com