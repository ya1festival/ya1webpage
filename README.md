# yet another webpage

This is the webpage code for the ya festival.

## Setup dev environment:

### Linux

```sh
bash scripts/setup-venv.sh
```

### Windows

```powershell
.\scripts\setup-venv.ps1
```

## Deploy content to github:

### Linux

```sh
bash scripts/deploy.sh
```

### Windows

```powershell
.\scripts\deploy.ps1
```

Then switch to `gh-pages` branch and push to remote:

```sh
git switch gh-pages
git push origin gh-pages
```
