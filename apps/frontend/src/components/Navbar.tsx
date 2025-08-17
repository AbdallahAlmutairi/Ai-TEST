'use client';

import LanguageToggle from './LanguageToggle';
import { useLanguage } from '../lib/i18n/LanguageProvider';

export default function Navbar() {
  const { dict } = useLanguage();
  return (
    <nav>
      <span>{dict.greeting}</span>
      <LanguageToggle />
    </nav>
  );
}
