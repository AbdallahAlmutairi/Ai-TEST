'use client';

import React, { createContext, useContext, useEffect, useState } from 'react';
import en from './en';
import ar from './ar';

export type Locale = 'en' | 'ar';

type Dictionary = typeof en;

interface LanguageContextValue {
  locale: Locale;
  dict: Dictionary;
  toggle: () => void;
}

const dictionaries: Record<Locale, Dictionary> = { en, ar };

const LanguageContext = createContext<LanguageContextValue | undefined>(undefined);

export function LanguageProvider({ children }: { children: React.ReactNode }) {
  const [locale, setLocale] = useState<Locale>('en');

  useEffect(() => {
    const stored = localStorage.getItem('locale') as Locale | null;
    if (stored && stored in dictionaries) {
      setLocale(stored);
    }
  }, []);

  useEffect(() => {
    document.documentElement.lang = locale;
    document.documentElement.dir = locale === 'ar' ? 'rtl' : 'ltr';
    localStorage.setItem('locale', locale);
  }, [locale]);

  const toggle = () => setLocale((l) => (l === 'en' ? 'ar' : 'en'));

  return (
    <LanguageContext.Provider value={{ locale, dict: dictionaries[locale], toggle }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  const ctx = useContext(LanguageContext);
  if (!ctx) throw new Error('useLanguage must be used within LanguageProvider');
  return ctx;
}
