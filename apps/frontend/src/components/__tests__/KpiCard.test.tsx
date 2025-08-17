import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { describe, it, expect } from 'vitest';
import KpiCard from '../KpiCard';

describe('KpiCard', () => {
  it('renders label and value', () => {
    render(<KpiCard label="Revenue" value="100" />);
    expect(screen.getByText('Revenue')).toBeTruthy();
    expect(screen.getByText('100')).toBeTruthy();
  });
});
