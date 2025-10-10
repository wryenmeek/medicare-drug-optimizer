// frontend/tests/unit/test_pharmacy_components.jsx

import { render, screen } from '@testing-library/react';
import PharmacyPreferences from '../../src/components/PharmacyPreferences';

describe('PharmacyPreferences component', () => {
  it('should render the title', () => {
    render(<PharmacyPreferences />);
    expect(screen.getByText(/Pharmacy Preferences/i)).toBeInTheDocument();
  });
});
