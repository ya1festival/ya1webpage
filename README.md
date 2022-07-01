# yet another webpage

This is the webpage code for the ya festival.

## Setup dev environment:

```sh
bash scripts/setup-venv.sh
```

## Deploy content to github:

Don't forget to change `SITEURL` variable in `pelicanconf.py` to `https://www.ya-festival.org` before deployment.

```sh
bash scripts/deploy.sh
```

Then switch to `gh-pages` branch and push to remote:

```sh
git switch gh-pages
git push origin gh-pages
```
