import React from 'react';
import { render, screen } from '@testing-library/react';
import DrugAlternatives from '../../src/components/DrugAlternatives';

describe('DrugAlternatives', () => {
  it('renders drug alternatives', async () => {
    render(<DrugAlternatives rxcui="12345" />);

    // Wait for the alternatives to be rendered
    const alternative1 = await screen.findByText(/Simvastatin/i);
    const alternative2 = await screen.findByText(/Zocor/i);

    expect(alternative1).toBeInTheDocument();
    expect(alternative2).toBeInTheDocument();
  });
});
