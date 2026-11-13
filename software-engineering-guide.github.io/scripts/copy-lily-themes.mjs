#!/usr/bin/env node
// Copies the Lily reference themes from the @lilydesignsystem/themes package
// into static/themes/, where the theme picker loads them (themesUrl="/themes/").
// static/themes/ is generated, not tracked: update the themes by bumping the
// package version in package.json. Runs before `dev` and `build`:
//   pnpm run themes
import { copyFileSync, mkdirSync, readdirSync, rmSync } from 'node:fs';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.resolve(here, '..', 'static/themes');
const require = createRequire(import.meta.url);
const srcDir = path.join(path.dirname(require.resolve('@lilydesignsystem/themes/package.json')), 'dist');

const files = readdirSync(srcDir).filter((f) => f.endsWith('.css'));
if (files.length === 0) throw new Error(`no theme stylesheets in ${srcDir}`);

rmSync(outDir, { recursive: true, force: true });
mkdirSync(outDir, { recursive: true });
for (const file of files) copyFileSync(path.join(srcDir, file), path.join(outDir, file));
console.log(`copy-lily-themes: ${files.length} themes into static/themes/`);
