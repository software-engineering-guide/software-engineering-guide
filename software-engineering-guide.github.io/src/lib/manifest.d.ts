// Overrides the auto-inferred literal type of the generated manifest.json
// (which otherwise has one specific string-literal key per chapter decimal,
// and rejects indexing by an arbitrary `string`) with a general shape.
// Keep this in sync with scripts/generate-manifest.mjs.
declare module '#lib/manifest.json' {
  interface Chapter {
    part: number;
    chapter: number;
    decimal: string;
    slug: string;
    title: string;
    heading: string;
    file: string;
  }

  interface Part {
    number: number;
    title: string;
    chapters: Chapter[];
  }

  interface ManifestEntry {
    slug: string;
    title: string;
    file: string;
  }

  interface LocaleManifest {
    chapters: Chapter[];
    parts: Part[];
    chaptersByDecimal: Record<string, Chapter>;
    order: string[];
    hasHomePage: boolean;
    /** URL segment for this locale's topics section (translated per locale). */
    topicsSlug: string;
  }

  interface Manifest {
    generatedBy: string;
    parts: Part[];
    chapters: Chapter[];
    chaptersByDecimal: Record<string, Chapter>;
    order: string[];
    frontMatter: ManifestEntry[];
    examples: ManifestEntry[];
    contributing: ManifestEntry[];
    project: ManifestEntry[];
    locales: Record<string, LocaleManifest>;
    availableLocales: string[];
    totals: { parts: number; chapters: number };
  }

  const manifest: Manifest;
  export default manifest;
}
