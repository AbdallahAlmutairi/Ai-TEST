'use client';

import { useLanguage } from '../lib/i18n/LanguageProvider';

export default function LanguageToggle() {
  const { locale, toggle } = useLanguage();
  return (
    <button onClick={toggle} aria-label="toggle language">
      {locale === 'en' ? 'AR' : 'EN'}
    </button>
  );
}
