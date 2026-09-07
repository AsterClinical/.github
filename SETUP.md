# Aster Clinical GitHub Organization Profile Setup

This repository must be public and named exactly `.github` under the `AsterClinical` organization. GitHub renders `profile/README.md` on the organization's public Overview page.

## Recommended organization profile fields

Set the organization description to:

> **Practical clinical software for independent doctors and small clinics.**

Keep the existing public website and contact details:

- Website: `https://asterclinical.com/`
- Email: `admin@asterclinical.com`
- Location: `India`

## Pin the public repositories

On the Aster Clinical organization Overview page, use **View as: Public**. If no repositories are pinned yet, choose **pin repositories** in the right sidebar. If a pinned section already exists, use **Customize pins**.

For the current two-repository organization, pin them in this order:

1. `brand-assets`
2. `clinical-document-platform-format`

When the main Aster Clinical application repository becomes public, move it to the first position and keep `brand-assets` and `clinical-document-platform-format` after it.

## Repository visibility

The `.github` repository must remain **Public** for the public organization profile README to appear.

## Push an existing local repository directly to the organization

Create an empty public repository named `.github` under `AsterClinical`, then run from this repository:

```bash
git remote add origin https://github.com/AsterClinical/.github.git
git push -u origin main
git push origin v0.1.0
```

If you instead create it temporarily under a personal account, transfer it to the `AsterClinical` organization and then update the remote:

```bash
git remote set-url origin https://github.com/AsterClinical/.github.git
```
