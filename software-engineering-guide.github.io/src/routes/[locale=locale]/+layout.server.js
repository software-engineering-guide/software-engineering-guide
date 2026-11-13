import { error } from '@sveltejs/kit';
import { resolveLocale, topicsBase } from '#lib/content.js';
import { localeLabel, langAttr, localeDir } from '#lib/locales.js';
import { ui } from '#lib/i18n.js';

/** @param {{ params: { locale: string } }} event */
export function load({ params }) {
  // `[locale]` is either a full code or a language alias ("en" -> "en-001").
  // An alias renders its world locale's content in place; `base` keeps links
  // inside the alias the visitor is browsing.
  const locale = resolveLocale(params.locale);
  if (!locale) error(404, 'Locale not found');
  return {
    locale,
    base: `/${params.locale}`,
    topicsBase: topicsBase(params.locale),
    isAlias: params.locale !== locale,
    localeLabel: localeLabel(locale),
    lang: langAttr(locale),
    dir: localeDir(locale),
    ui: ui(locale)
  };
}
